#!/usr/bin/env bash
set -euo pipefail

# Auto-generate readme_power_645, then commit + push when changed.
# Usage:
#   bin/auto_publish_power645.sh
# Optional env:
#   GIT_REMOTE=origin
#   GIT_BRANCH=main
#   GIT_USERNAME=<https-username>
#   GIT_PASSWORD=<https-password-or-token>   # defaults to 123123 when ENABLE_PASSWORD_PUSH=1
#   ENABLE_PASSWORD_PUSH=1                   # use askpass flow for HTTPS remotes

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

REMOTE="${GIT_REMOTE:-origin}"
BRANCH="${GIT_BRANCH:-$(git rev-parse --abbrev-ref HEAD)}"
VENV_PY="${ROOT_DIR}/.venv/bin/python"
TARGET_FILE="src/machine_learning/readme_power_645.md"

if [[ ! -x "$VENV_PY" ]]; then
  echo "[ERROR] Python in .venv not found: $VENV_PY"
  exit 1
fi

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "[ERROR] Current folder is not a git repository."
  exit 1
fi

echo "[INFO] Generating $TARGET_FILE ..."
PYTHONPATH=src "$VENV_PY" src/machine_learning/render_prediction.py --product power_645 --seed 42 --seed-runs 3 --history-window 10 --oos-draws 120

if [[ ! -f "$TARGET_FILE" ]]; then
  echo "[ERROR] Target file not found after generation: $TARGET_FILE"
  exit 1
fi

if git diff --quiet -- "$TARGET_FILE"; then
  echo "[INFO] No changes in $TARGET_FILE. Skip commit/push."
  exit 0
fi

git add "$TARGET_FILE"
COMMIT_MSG="auto: update power_645 prediction @ $(date +"%Y-%m-%d %H:%M:%S")"
git commit -m "$COMMIT_MSG"

ASKPASS_SCRIPT=""
cleanup() {
  if [[ -n "$ASKPASS_SCRIPT" && -f "$ASKPASS_SCRIPT" ]]; then
    rm -f "$ASKPASS_SCRIPT"
  fi
}
trap cleanup EXIT

if [[ "${ENABLE_PASSWORD_PUSH:-0}" == "1" ]]; then
  ASKPASS_SCRIPT="$(mktemp)"
  cat >"$ASKPASS_SCRIPT" <<'EOF'
#!/usr/bin/env bash
case "$1" in
  *Username*) echo "${GIT_USERNAME:-}" ;;
  *Password*) echo "${GIT_PASSWORD:-123123}" ;;
  *) echo "" ;;
esac
EOF
  chmod 700 "$ASKPASS_SCRIPT"
  echo "[INFO] Pushing with HTTPS askpass flow (password default: 123123)."
  GIT_TERMINAL_PROMPT=0 GIT_ASKPASS="$ASKPASS_SCRIPT" git push "$REMOTE" "$BRANCH"
else
  echo "[INFO] Pushing with normal git credentials (ssh agent / credential helper)."
  git push "$REMOTE" "$BRANCH"
fi

echo "[DONE] Published $TARGET_FILE to $REMOTE/$BRANCH"
