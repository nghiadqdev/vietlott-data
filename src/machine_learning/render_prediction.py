#!/usr/bin/env python
"""
Prediction Summary Generator for Vietlott Data Project.

This script generates a prediction summary markdown file for the machine learning module.
It outputs detailed prediction reports with statistics for each strategy.
"""

from datetime import datetime
from pathlib import Path
import argparse
from collections import Counter
import json
import random
from statistics import mean, pstdev
from typing import Dict, List, Optional, Tuple

import polars as pl
from loguru import logger

from machine_learning.strategies import (
    ColdNumbersStrategy,
    ExponentialDecayStrategy,
    HotNumbersStrategy,
    LongAbsenceStrategy,
    NotRepeatStrategy,
    PairFrequencyStrategy,
    PatternStrategy,
    RandomModel,
)
from machine_learning.strategies.base import PredictModel
from vietlott.config.products import get_config

# (strategy_name, tickets_per_day, model_instance) after backtest+evaluate
_StrategyEntry = Tuple[str, int, PredictModel]


class PredictionSummaryGenerator:
    """Generator for prediction summary."""

    def __init__(self):
        self.history_path = Path(__file__).parent / "prediction_run_history.jsonl"

    def _set_seed(self, seed: Optional[int]) -> None:
        """Set RNG seeds for deterministic runs when a seed is provided."""
        if seed is None:
            return

        random.seed(seed)
        try:
            import numpy as np

            np.random.seed(seed)
        except Exception:
            # Numpy is optional for deterministic behavior in strategies using stdlib random.
            pass

    def _fmt_money_tr(self, value: float) -> str:
        """Format VND as million unit with 'tr' suffix (e.g. 297tr, 10,058.5tr)."""
        million = value / 1_000_000
        text = f"{million:,.1f}"
        if text.endswith(".0"):
            text = text[:-2]
        return f"{text}tr"

    def _collect_strategy_metrics(self, strategies: List[_StrategyEntry]) -> List[Dict[str, float]]:
        """Collect per-strategy metrics used for stability analysis and history logging."""
        metrics: List[Dict[str, float]] = []
        for name, _, model in strategies:
            cost, gain, profit = model.revenue()
            roi = (profit / cost * 100) if cost > 0 else 0.0
            metrics.append({
                "name": name,
                "cost": float(cost),
                "gain": float(gain),
                "profit": float(profit),
                "roi": float(roi),
            })
        return metrics

    def _stability_section(self, run_metrics: List[List[Dict[str, float]]]) -> str:
        """Build a multi-seed stability summary section."""
        if len(run_metrics) <= 1:
            return ""

        by_strategy: Dict[str, List[Dict[str, float]]] = {}
        for run in run_metrics:
            for item in run:
                by_strategy.setdefault(item["name"], []).append(item)

        rows = []
        for name, items in by_strategy.items():
            rois = [x["roi"] for x in items]
            profits = [x["profit"] for x in items]
            rows.append(
                (
                    name,
                    mean(rois),
                    pstdev(rois) if len(rois) > 1 else 0.0,
                    mean(profits),
                    pstdev(profits) if len(profits) > 1 else 0.0,
                )
            )

        rows.sort(key=lambda x: x[1], reverse=True)
        lines = [
            "| Chiến lược | ROI TB | ROI Độ lệch chuẩn | Lợi nhuận TB (tr) | Lợi nhuận Độ lệch chuẩn (tr) |",
            "|------------|--------|-------------------|--------------------|--------------------------|",
        ]
        for name, roi_avg, roi_std, profit_avg, profit_std in rows:
            lines.append(
                f"| {name} | {roi_avg:.2f}% | {roi_std:.2f}% | {self._fmt_money_tr(profit_avg)} | {self._fmt_money_tr(profit_std)} |"
            )

        return f"""## 📈 Độ ổn định Nhiều Seed

> Bảng dưới tổng hợp kết quả qua **{len(run_metrics)} lần chạy seed**.
> Ưu tiên chiến lược có ROI trung bình cao và độ lệch chuẩn thấp.

{chr(10).join(lines)}
"""

    def _append_history(
        self,
        *,
        product: str,
        seed: Optional[int],
        seed_runs: int,
        output_path: Path,
        run_metrics: List[List[Dict[str, float]]],
    ) -> None:
        """Append one JSONL record to persistent run history for long-term analysis."""
        record = {
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "product": product,
            "seed": seed,
            "seed_runs": seed_runs,
            "output_path": str(output_path),
            "runs": run_metrics,
        }
        self.history_path.parent.mkdir(parents=True, exist_ok=True)
        with self.history_path.open("a", encoding="utf-8") as hist:
            hist.write(json.dumps(record, ensure_ascii=False) + "\n")

    def _history_leaderboard_section(self, product: str, history_window: int) -> str:
        """Build leaderboard aggregated from recent history records for a product."""
        if history_window < 1 or not self.history_path.exists():
            return ""

        records = []
        with self.history_path.open("r", encoding="utf-8") as hist:
            for line in hist:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                if obj.get("product") == product:
                    records.append(obj)

        if not records:
            return ""

        recent = records[-history_window:]
        by_strategy: Dict[str, List[float]] = {}
        for rec in recent:
            for run in rec.get("runs", []):
                for item in run:
                    name = item.get("name")
                    roi = item.get("roi")
                    if name is None or roi is None:
                        continue
                    by_strategy.setdefault(name, []).append(float(roi))

        if not by_strategy:
            return ""

        rows = []
        for name, rois in by_strategy.items():
            rows.append(
                (
                    name,
                    mean(rois),
                    pstdev(rois) if len(rois) > 1 else 0.0,
                    len(rois),
                )
            )

        rows.sort(key=lambda x: x[1], reverse=True)
        lines = [
            "| Hạng | Chiến lược | ROI TB lịch sử | ROI Độ lệch chuẩn | Số run |",
            "|------|------------|----------------|-------------------|--------|",
        ]
        for idx, (name, roi_avg, roi_std, count) in enumerate(rows, start=1):
            lines.append(f"| {idx} | {name} | {roi_avg:.2f}% | {roi_std:.2f}% | {count} |")

        return f"""## 🧾 Leaderboard Lịch sử

> Tổng hợp từ **{len(recent)} bản ghi gần nhất** của sản phẩm `{product}`.
> Bảng này giúp ưu tiên chiến lược ổn định theo thời gian, không chỉ theo một lần chạy.

{chr(10).join(lines)}
"""

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

    def _load_lottery_data(self, product: str) -> pl.DataFrame:
        """Load and prepare lottery data for predictions."""
        try:
            df = pl.read_ndjson(get_config(product).raw_path)

            if "date" in df.columns:
                try:
                    if df["date"].dtype in [pl.Date, pl.Datetime]:
                        df = df.with_columns(pl.col("date").cast(pl.Date))
                    elif df["date"].dtype in [pl.Int64, pl.Int32, pl.Float64]:
                        max_val = df["date"].max()
                        if max_val > 1_000_000_000_000:
                            df = df.with_columns(
                                (pl.col("date").cast(pl.Int64) / 1000).cast(pl.Datetime("ms")).cast(pl.Date)
                            )
                        else:
                            df = df.with_columns(pl.col("date").cast(pl.Int64).cast(pl.Datetime("s")).cast(pl.Date))
                    else:
                        df = df.with_columns(pl.col("date").str.to_date(strict=False))
                except Exception as e:
                    logger.warning(f"Could not parse date column: {e}")
                    df = df.with_columns(pl.col("date").str.to_date(strict=False))

            df = df.sort(["date", "id"], descending=True)
            return df
        except Exception as e:
            logger.error(f"Error loading data for {product}: {e}")
            return pl.DataFrame()

    # ------------------------------------------------------------------
    # Strategy runner
    # ------------------------------------------------------------------

    def _build_and_run_strategies(
        self,
        df_pd,
        *,
        min_val: int,
        max_val: int,
        number_predict: int,
    ) -> List[_StrategyEntry]:
        """
        Instantiate, backtest, and evaluate all strategies.

        Returns a list of ``(name, tickets_per_day, model)`` tuples where
        each model has already been backtested and evaluated.
        """
        tpd = 20  # tickets per day for all strategies

        strategy_defs = [
            ("Chiến lược Ngẫu nhiên", RandomModel(df_pd, tpd, min_val=min_val, max_val=max_val)),
            (
                "Chiến lược Vắng mặt Lâu dài",
                LongAbsenceStrategy(df_pd, time_predict=tpd, min_val=min_val, max_val=max_val, top_n=15),
            ),
            (
                "Chiến lược Mẫu",
                PatternStrategy(
                    df_pd,
                    time_predict=tpd,
                    min_val=min_val,
                    max_val=max_val,
                    lookback_days=180,
                    pattern_weight=0.6,
                ),
            ),
            (
                "Chiến lược Số Nóng",
                HotNumbersStrategy(
                    df_pd,
                    time_predict=tpd,
                    min_val=min_val,
                    max_val=max_val,
                    lookback_days=365,
                    selection_weight=0.7,
                ),
            ),
            (
                "Chiến lược Số Lạnh",
                ColdNumbersStrategy(
                    df_pd,
                    time_predict=tpd,
                    min_val=min_val,
                    max_val=max_val,
                    lookback_days=365,
                    selection_weight=0.7,
                ),
            ),
            (
                "Chiến lược Không Lặp lại",
                NotRepeatStrategy(
                    df_pd,
                    time_predict=tpd,
                    min_val=min_val,
                    max_val=max_val,
                    lookback_days=30,
                    avoid_weight=0.8,
                ),
            ),
            (
                "Chiến lược Suy giảm Exponential",
                ExponentialDecayStrategy(
                    df_pd,
                    time_predict=tpd,
                    min_val=min_val,
                    max_val=max_val,
                    half_life_days=90,
                    hot=True,
                    selection_weight=0.8,
                ),
            ),
            (
                "Chiến lược Tần suất Cặp",
                PairFrequencyStrategy(df_pd, time_predict=tpd, min_val=min_val, max_val=max_val, lookback_days=365),
            ),
        ]

        results: List[_StrategyEntry] = []
        for name, model in strategy_defs:
            model.number_predict = number_predict
            logger.info(f"Running {name}...")
            model.backtest()
            model.evaluate()
            results.append((name, tpd, model))

        return results

    # ------------------------------------------------------------------
    # ROI comparison table (header)
    # ------------------------------------------------------------------

    def _roi_comparison_table(self, strategies: List[_StrategyEntry]) -> str:
        """Generate a ROI comparison table sorted best → worst."""
        rows = []
        for name, tpd, model in strategies:
            cost, gain, profit = model.revenue()
            roi = (profit / cost * 100) if cost > 0 else 0.0
            rows.append((name, cost, gain, profit, roi))

        rows.sort(key=lambda x: x[4], reverse=True)

        medals = ["🥇", "🥈", "🥉"] + ["  "] * len(rows)
        header = "| Hạng | Chiến lược | Tổng Chi phí (tr) | Tổng Lợi nhuận (tr) | Lợi nhuận ròng (tr) | ROI |"
        sep = "|------|----------|-----------------|-----------------|-----------------|-----|"
        lines = [header, sep]
        for i, (name, cost, gain, profit, roi) in enumerate(rows):
            lines.append(
                f"| {medals[i]} {i + 1} | {name} | {self._fmt_money_tr(cost)} | {self._fmt_money_tr(gain)} | {self._fmt_money_tr(profit)} | {roi:.2f}% |"
            )

        return f"""## 📊 So sánh Hiệu suất Chiến lược

> Sắp xếp theo ROI (tốt nhất → tệ nhất). Tất cả các chiến lược được kiểm thử với **{strategies[0][1]} vé/lần quay**.
> Lưu ý: Tất cả ROI đều âm sâu — xác suất xổ số khiến lợi nhuận không thể xảy ra ở quy mô lớn.
> So sánh cho thấy *chiến lược nào thua ít nhất*, không phải chiến lược nào có lợi.

{chr(10).join(lines)}
"""

    def _generate_roi_bar_chart(self, strategies: List[_StrategyEntry], width: int = 24) -> str:
        """Generate a compact ASCII bar chart to visualize relative ROI by strategy."""
        if not strategies:
            return ""

        rows = []
        for name, _, model in strategies:
            cost, gain, profit = model.revenue()
            roi = (profit / cost * 100) if cost > 0 else 0.0
            rows.append((name, roi))

        rows.sort(key=lambda x: x[1], reverse=True)
        max_abs = max(abs(roi) for _, roi in rows) or 1.0

        lines = [
            "| Chiến lược | ROI | Biểu đồ tương đối |",
            "|------------|-----|-------------------|",
        ]
        for name, roi in rows:
            bar_len = int(abs(roi) / max_abs * width)
            if bar_len == 0 and roi != 0:
                bar_len = 1
            symbol = "+" if roi >= 0 else "-"
            bar = symbol * bar_len
            lines.append(f"| {name} | {roi:.2f}% | {bar} |")

        return f"""## 📉 Biểu đồ ROI Tổng quát

> Biểu đồ thanh tương đối để nhìn nhanh chiến lược nào đang trội/yếu trong lần chạy hiện tại.
> Dấu '+' là ROI dương, dấu '-' là ROI âm. Độ dài thanh được chuẩn hóa theo giá trị tuyệt đối lớn nhất.

{chr(10).join(lines)}
"""

    def _generate_roi_dual_tables(
        self,
        strategies: List[_StrategyEntry],
        df_pd,
        *,
        oos_days: int,
        oos_draws: Optional[int],
    ) -> str:
        """Generate two ROI tables to compare fixed benchmark vs recent OOS window."""
        if not strategies or df_pd.empty or "date" not in df_pd.columns:
            return ""

        import pandas as pd

        # Table A: fixed benchmark over full backtest history.
        full_rows = []
        full_roi_map: Dict[str, float] = {}
        for name, _, model in strategies:
            cost, gain, profit = model.revenue()
            roi = (profit / cost * 100) if cost > 0 else 0.0
            full_rows.append((name, cost, gain, profit, roi))
            full_roi_map[name] = roi

        full_rows.sort(key=lambda x: x[4], reverse=True)
        full_lines = [
            "| Hạng | Chiến lược | Tổng Chi phí (tr) | Tổng Lợi nhuận (tr) | Lợi nhuận ròng (tr) | ROI Toàn kỳ |",
            "|------|------------|-------------------|---------------------|---------------------|-------------|",
        ]
        medals = ["🥇", "🥈", "🥉"] + ["  "] * len(full_rows)
        for idx, (name, cost, gain, profit, roi) in enumerate(full_rows, start=1):
            full_lines.append(
                f"| {medals[idx - 1]} {idx} | {name} | {self._fmt_money_tr(cost)} | {self._fmt_money_tr(gain)} | {self._fmt_money_tr(profit)} | {roi:.2f}% |"
            )

        # Table B: dynamic recent-window OOS ROI with delta vs full-history benchmark.
        last_date = pd.to_datetime(df_pd["date"]).max()
        date_series = pd.to_datetime(df_pd["date"])
        if oos_draws is not None and oos_draws > 0:
            unique_dates_desc = sorted(date_series.dropna().unique(), reverse=True)
            if unique_dates_desc:
                cutoff = unique_dates_desc[min(oos_draws - 1, len(unique_dates_desc) - 1)]
                oos_mode_text = f"**{oos_draws} kỳ quay gần nhất**"
            else:
                cutoff = last_date
                oos_mode_text = "**không xác định**"
        else:
            days = oos_days if oos_days >= 1 else 365
            cutoff = last_date - pd.Timedelta(days=days)
            oos_mode_text = f"**{days} ngày gần nhất**"

        oos_rows = []
        for name, _, model in strategies:
            df_eval = model.df_backtest_evaluate
            if df_eval is None or df_eval.empty:
                continue

            eval_dates = pd.to_datetime(df_eval["date"])
            oos_eval = df_eval.loc[eval_dates >= cutoff].copy()
            if oos_eval.empty:
                continue

            correct_num = oos_eval["correct_num"].apply(self._to_int).astype(int)
            cost = len(oos_eval) * model.ticket_price
            gain = correct_num.map(model.prices).fillna(0).astype(int).sum()
            profit = gain - cost
            roi_oos = (profit / cost * 100) if cost > 0 else 0.0
            roi_full = full_roi_map.get(name, 0.0)
            delta = roi_oos - roi_full
            oos_rows.append((name, cost, gain, profit, roi_oos, delta))

        oos_rows.sort(key=lambda x: x[4], reverse=True)
        oos_lines = [
            "| Hạng | Chiến lược | Chi phí OOS (tr) | Lợi nhuận OOS (tr) | ROI OOS | ΔROI (OOS - Toàn kỳ) |",
            "|------|------------|------------------|--------------------|---------|-----------------------|",
        ]
        medals_oos = ["🥇", "🥈", "🥉"] + ["  "] * len(oos_rows)
        for idx, (name, cost, gain, _profit, roi_oos, delta) in enumerate(oos_rows, start=1):
            sign = "+" if delta >= 0 else ""
            oos_lines.append(
                f"| {medals_oos[idx - 1]} {idx} | {name} | {self._fmt_money_tr(cost)} | {self._fmt_money_tr(gain)} | {roi_oos:.2f}% | {sign}{delta:.2f}% |"
            )

        return f"""## 📊 So sánh ROI: Benchmark vs Khung nhớ động

> Bảng A là benchmark cố định trên toàn bộ lịch sử.
> Bảng B là ROI ở cửa sổ gần đây {oos_mode_text} để mô phỏng vận hành động.
> Cột **ΔROI** giúp bạn thấy mức thay đổi khi chuyển từ khung nhớ cố định sang khung nhớ gần.

### Bảng A: ROI Benchmark (Toàn kỳ)

{chr(10).join(full_lines)}

### Bảng B: ROI Khung nhớ động (OOS gần đây)

{chr(10).join(oos_lines)}
"""

    # ------------------------------------------------------------------
    # Per-strategy detailed report
    # ------------------------------------------------------------------

    def _to_int(self, v) -> int:
        """Convert value to integer safely."""
        try:
            return int(v)
        except Exception:
            try:
                return len(v)
            except Exception:
                return 0

    def _generate_strategy_report(self, model: PredictModel, strategy_name: str, tickets_per_day: int) -> str:
        """Generate detailed report for a single strategy."""
        df_eval = model.df_backtest_evaluate
        if df_eval is None or df_eval.empty:
            return f"### {strategy_name}\n\n> Không có dữ liệu đánh giá.\n"

        total_draws = len(model.df_backtest)
        total_predictions = len(df_eval)
        cost, gain, profit = model.revenue()

        s_correct = df_eval["correct_num"].apply(self._to_int).astype(int)
        match_counts = s_correct.value_counts().sort_index(ascending=False)
        match_distribution = "\n".join(
            [f"  - **{matches} trùng khớp**: {count:,} lần" for matches, count in match_counts.items()]
        )

        mask = (s_correct >= 5).to_numpy()
        df_best = df_eval.loc[mask, ["date", "result", "predicted", "correct_num"]].copy()
        df_best["result"] = df_best["result"].apply(
            lambda x: str([int(i) for i in x]) if hasattr(x, "__iter__") else str(x)
        )
        df_best["predicted"] = df_best["predicted"].apply(
            lambda x: str([int(i) for i in x]) if hasattr(x, "__iter__") else str(x)
        )
        df_best["correct_num"] = df_best["correct_num"].apply(self._to_int)

        best_results_table = (
            df_best.to_markdown(index=False) if not df_best.empty else "Không tìm thấy kết quả với 5+ trùng khớp."
        )

        date_min = df_eval["date"].min()
        date_max = df_eval["date"].max()

        return f"""### 🎲 {strategy_name}

#### Cấu hình
| Tham số | Giá trị |
|-----------|-------|
| Chiến lược | {strategy_name} |
| Vé mỗi ngày | {tickets_per_day} |
| Giá vé | {model.ticket_price:,} VND |
| Dải số | {model.min_val} - {model.max_val} |
| Số cần chọn | {model.number_predict} |

#### Kỳ Kiểm thử
| Chỉ số | Giá trị |
|--------|-------|
| Ngày bắt đầu | {date_min} |
| Ngày kết thúc | {date_max} |
| Tổng lần quay | {total_draws:,} |
| Tổng dự đoán | {total_predictions:,} |

#### Tóm tắt Tài chính
| Chỉ số | Giá trị |
|--------|-------|
| Tổng chi phí | {self._fmt_money_tr(cost)} |
| Tổng lợi nhuận | {self._fmt_money_tr(gain)} |
| Lợi nhuận/lỗ ròng | {self._fmt_money_tr(profit)} |
| ROI | {(profit / cost * 100) if cost > 0 else 0:.2f}% |

#### Phân bố Trùng khớp
{match_distribution}

#### Kết quả nổi bật (>=5 số trùng)
{best_results_table}

"""

    def _generate_predictions_section(self, strategies: List[_StrategyEntry]) -> str:
        """Generate per-strategy detailed reports from pre-run strategy list."""
        reports = [self._generate_strategy_report(model, name, tpd) for name, tpd, model in strategies]
        return f"""## 🔮 Mô hình Dự đoán

> ⚠️ **Tuyên bố**: Đây là các mô hình thử nghiệm chỉ dành cho mục đích giáo dục. Kết quả xổ số ngẫu nhiên và không thể dự đoán một cách đáng tin cậy.

{"".join(reports)}
"""

    def _generate_future_number_forecast(
        self,
        strategies: List[_StrategyEntry],
        df_pd,
        product: str,
        top_k: int = 5,
        samples_per_strategy: int = 200,
    ) -> str:
        """Generate top-k likely numbers for the next draw by ensembling strategy simulations."""
        if not strategies or df_pd.empty or "date" not in df_pd.columns:
            return "## 🔭 Next Draw Number Forecast\n\n> Not enough data to generate forecast.\n"

        product_cfg = get_config(product)
        last_date = df_pd["date"].max()
        if not hasattr(last_date, "to_pydatetime"):
            # Normalize to pandas-compatible datetime scalar for strategy comparisons.
            import pandas as pd

            last_date = pd.to_datetime(last_date)
        next_draw_date = last_date + product_cfg.interval
        display_next_draw_date = next_draw_date.date() if hasattr(next_draw_date, "date") else next_draw_date

        overall_counter: Counter[int] = Counter()
        per_strategy_lines: List[str] = []
        strategy_roi_list = []

        for name, _, model in strategies:
            strategy_counter: Counter[int] = Counter()
            for _ in range(samples_per_strategy):
                predicted = model.predict(next_draw_date)
                strategy_counter.update(predicted)

            overall_counter.update(strategy_counter)
            top_numbers = ", ".join(str(n) for n, _ in strategy_counter.most_common(top_k))
            cost, gain, profit = model.revenue()
            roi = (profit / cost * 100) if cost > 0 else 0.0
            strategy_roi_list.append((name, top_numbers, roi))
        
        # Sort by ROI in descending order (highest profit first)
        strategy_roi_list.sort(key=lambda x: x[2], reverse=True)
        for name, top_numbers, _ in strategy_roi_list:
            per_strategy_lines.append(f"| {name} | {top_numbers} |")

        top_overall = overall_counter.most_common(top_k)
        total_tickets = len(strategies) * samples_per_strategy
        overall_rows = []
        for number, score in top_overall:
            ticket_presence = score / total_tickets * 100 if total_tickets > 0 else 0
            overall_rows.append(f"| {number} | {score} | {ticket_presence:.2f}% |")
        
        # Sort per_strategy_lines is already done above in the loop

        return f"""## 🔭 Dự đoán Số cho Lần Quay Tiếp theo

> Dự đoán cho lần quay tiếp theo vào: **{display_next_draw_date}**.
> Phương pháp: mỗi chiến lược mô phỏng **{samples_per_strategy}** vé, sau đó tất cả vé được tổng hợp.
> Đây là xếp hạng xác suất, không phải các số trúng đảm bảo.

### {top_k} số ứng cử viên hàng đầu (tập hợp)

| Số | Điểm Tập hợp | Xuất hiện trong Vé |
|--------|----------------|---------------------|
{chr(10).join(overall_rows)}

### {top_k} hàng đầu theo Chiến lược

| Chiến lược | Số hàng đầu |
|----------|-------------|
{chr(10).join(per_strategy_lines)}
"""

    def _generate_compact_strategy_table(
        self,
        strategies: List[_StrategyEntry],
        df_pd,
        product: str,
        top_k: int = 5,
        samples_per_strategy: int = 200,
    ) -> str:
        """Generate a concise one-row-per-strategy summary table with next-draw Top-K numbers."""
        if not strategies or df_pd.empty or "date" not in df_pd.columns:
            return "## 📋 Compact Strategy Table\n\n> Not enough data to generate compact table.\n"

        product_cfg = get_config(product)
        last_date = df_pd["date"].max()
        if not hasattr(last_date, "to_pydatetime"):
            import pandas as pd

            last_date = pd.to_datetime(last_date)
        next_draw_date = last_date + product_cfg.interval
        display_next_draw_date = next_draw_date.date() if hasattr(next_draw_date, "date") else next_draw_date

        rows: List[tuple] = []
        for name, tpd, model in strategies:
            df_eval = model.df_backtest_evaluate
            if df_eval is None or df_eval.empty:
                continue

            cost, gain, profit = model.revenue()
            roi = (profit / cost * 100) if cost > 0 else 0.0

            s_correct = df_eval["correct_num"].apply(self._to_int).astype(int)
            c5 = int((s_correct >= 5).sum())
            c4 = int((s_correct == 4).sum())
            c3 = int((s_correct == 3).sum())

            strategy_counter: Counter[int] = Counter()
            for _ in range(samples_per_strategy):
                strategy_counter.update(model.predict(next_draw_date))
            top_numbers = ", ".join(str(n) for n, _ in strategy_counter.most_common(top_k))

            config_text = f"dải {model.min_val}-{model.max_val}, chọn {model.number_predict}, vé/ngày {tpd}"
            period_text = f"{df_eval['date'].min()} → {df_eval['date'].max()} ({len(model.df_backtest):,} lần quay/{len(df_eval):,} dự đoán)"
            financial_text = f"chi {self._fmt_money_tr(cost)}, lợi {self._fmt_money_tr(gain)}, roi {roi:.2f}%"
            match_text = f"5+: {c5}, 4: {c4}, 3: {c3}"
            best_text = f"{c5} hàng với >=5 số trùng"

            row_text = (
                "| "
                + " | ".join([name, config_text, period_text, financial_text, match_text, best_text, top_numbers])
                + " |"
            )
            rows.append((roi, row_text))

        # Sort by ROI in descending order (highest profit first)
        rows.sort(key=lambda x: x[0], reverse=True)
        rows_sorted = [row_text for _, row_text in rows]

        if not rows_sorted:
            return "## 📋 Bảng Chiến lược Tóm tắt\n\n> Không có dữ liệu chiến lược.\n"

        return f"""## 📋 Bảng Chiến lược Tóm tắt

> Ngày dự đoán: **{display_next_draw_date}**.
> Dạng tóm tắt: Cấu hình, Kỳ Kiểm thử, Tóm tắt Tài chính, Phân bố Trùng khớp, KQ nổi bật (>=5 số trùng), {top_k} Hàng đầu.

| Chiến lược | Cấu hình | Kỳ Kiểm thử | Tóm tắt Tài chính | Phân bố Trùng khớp | KQ nổi bật (>=5) | {top_k} Hàng đầu |
|----------|---------------|-----------------|-------------------|--------------------|--------------|--------|
{chr(10).join(rows_sorted)}
"""

    def _generate_oos_section(
        self,
        strategies: List[_StrategyEntry],
        df_pd,
        oos_days: int,
        oos_draws: Optional[int] = None,
    ) -> str:
        """Generate rolling out-of-sample summary by recent days or recent draw count."""
        if not strategies or df_pd.empty or "date" not in df_pd.columns:
            return ""

        import pandas as pd

        last_date = pd.to_datetime(df_pd["date"]).max()
        date_series = pd.to_datetime(df_pd["date"])

        if oos_draws is not None and oos_draws > 0:
            unique_dates_desc = sorted(date_series.dropna().unique(), reverse=True)
            if not unique_dates_desc:
                return ""
            if oos_draws > len(unique_dates_desc):
                cutoff = min(unique_dates_desc)
            else:
                cutoff = unique_dates_desc[oos_draws - 1]
            oos_mode_text = f"**{oos_draws} kỳ quay gần nhất**"
        else:
            if oos_days < 1:
                return ""
            cutoff = last_date - pd.Timedelta(days=oos_days)
            oos_mode_text = f"**{oos_days} ngày gần nhất**"

        rows = []
        for name, _, model in strategies:
            df_eval = model.df_backtest_evaluate
            if df_eval is None or df_eval.empty:
                continue

            eval_dates = pd.to_datetime(df_eval["date"])
            oos_eval = df_eval.loc[eval_dates >= cutoff].copy()
            if oos_eval.empty:
                continue

            correct_num = oos_eval["correct_num"].apply(self._to_int).astype(int)
            cost = len(oos_eval) * model.ticket_price
            gain = correct_num.map(model.prices).fillna(0).astype(int).sum()
            profit = gain - cost
            roi = (profit / cost * 100) if cost > 0 else 0.0

            c6 = int((correct_num >= 6).sum())
            c5 = int((correct_num == 5).sum())
            c4 = int((correct_num == 4).sum())
            c3 = int((correct_num == 3).sum())

            period_text = f"{oos_eval['date'].min()} → {oos_eval['date'].max()} ({len(oos_eval):,} dự đoán)"
            financial_text = f"chi {self._fmt_money_tr(cost)}, lợi {self._fmt_money_tr(gain)}, roi {roi:.2f}%"
            match_text = f"6+: {c6}, 5: {c5}, 4: {c4}, 3: {c3}"

            row_text = "| " + " | ".join([name, period_text, financial_text, match_text]) + " |"
            rows.append((roi, row_text))

        if not rows:
            return ""

        rows.sort(key=lambda x: x[0], reverse=True)
        rows_sorted = [row_text for _, row_text in rows]

        lines = [
            "## 🧪 Đánh giá Rolling Out-of-Sample",
            "",
            f"> Cửa sổ kiểm thử ngoài mẫu: {oos_mode_text} (đến {last_date.date()}).",
            "> Mục tiêu: đánh giá chiến lược trên giai đoạn gần đây, giảm thiên lệch do fit vào toàn bộ lịch sử.",
            "",
            "| Chiến lược | Giai đoạn OOS | Tài chính OOS | Phân bố trùng khớp OOS |",
            "|------------|----------------|---------------|--------------------------|",
            *rows_sorted,
            "",
        ]
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Strategy documentation
    # ------------------------------------------------------------------

    _STRATEGY_DOCS = {
        "Chiến lược Ngẫu nhiên": (
            "**Cách hoạt động**: Tạo vé bằng cách xáo trộn tất cả các số trong dải hợp lệ "
            "và chọn `number_predict` mục đầu tiên. Mỗi số có cơ hội được chọn bằng nhau; "
            "không sử dụng dữ liệu lịch sử.\n\n"
            "**Trường hợp sử dụng**: Phục vụ như một đường cơ sở hiệu suất không thiên vị. "
            "Bất kỳ chiến lược nào không thể vượt qua lựa chọn ngẫu nhiên trong kiểm thử lớn đều không có giá trị dự đoán."
        ),
        "Chiến lược Vắng mặt Lâu dài": (
            "**Cách hoạt động**: Đối với mỗi lần quay, nhìn lại tất cả các lần quay trước đó và ghi lại "
            "lần cuối cùng mỗi số xuất hiện. Các số được xếp hạng theo bao nhiêu ngày đã trôi qua "
            "kể từ khi chúng cuối cùng xuất hiện (các số chưa bao giờ xuất hiện được xếp hạng cao nhất). "
            "Một nhóm các `top_n` số vắng mặt lâu nhất có thể cấu hình được tập hợp, và "
            "`number_predict` số được lấy mẫu ngẫu nhiên từ nhóm đó.\n\n"
            "**Tham số chính**: `top_n` (mặc định 10) – nhóm lớn hơn → tính ngẫu nhiên nhiều hơn; "
            "nhóm nhỏ hơn → thiên vị mạnh hơn về các số vắng mặt lâu nhất.\n\n"
            "**Trường hợp sử dụng**: Nắm bắt trực giác rằng các số bị *trễ hạn* "
            "trong một thời gian dài có nhiều khả năng xuất hiện hơn. (Lưu ý: đối với xổ số công bằng, trực giác này là sai về mặt toán học, "
            "nhưng chiến lược được đưa vào để so sánh thực nghiệm.)"
        ),
        "Chiến lược Mẫu": (
            "**Cách hoạt động**: Phân tích hai thuộc tính cấu trúc của các lần quay lịch sử "
            "trong cửa sổ `lookback_days` lăn:\n\n"
            "1. **Mẫu khoảng cách** – khoảng cách giữa các số được sắp xếp liên tiếp trong vé. "
            "Các khoảng cách phổ biến nhất được sử dụng để tạo số tiếp theo bằng cách áp dụng "
            "một khoảng cách được lấy mẫu cho số đã chọn trước đó.\n"
            "2. **Phân bố dải** – dải số 1–55 được chia thành năm dải con bằng nhau. "
            "Phần lịch sử của các lần quay rơi vào mỗi dải con được sử dụng "
            "như một trọng số xác suất để chọn số đầu tiên.\n\n"
            "Một phần `pattern_weight` của vé được điền bằng các số xuất phát từ mẫu; "
            "phần còn lại được điền ngẫu nhiên.\n\n"
            "**Tham số chính**: `lookback_days` (mặc định 180), `pattern_weight` (mặc định 0.6)."
        ),
        "Chiến lược Số Nóng": (
            "**Cách hoạt động**: Đếm số lần mỗi số xuất hiện trong `lookback_days` ngày qua. "
            "Các số được sắp xếp từ thường xuyên nhất đến ít thường xuyên nhất. "
            "Một nhóm được trọng số hóa được xây dựng với mỗi số được lặp lại tỷ lệ với "
            "tần số của nó, sau đó các số được rút ra mà không thay thế từ nhóm đó.\n\n"
            "Một phần `selection_weight` của vé được điền từ "
            "nhóm được trọng số hóa theo tần số; phần còn lại được điền bằng cách ngẫu nhiên.\n\n"
            "**Tham số chính**: `lookback_days` (mặc định 365), `selection_weight` (mặc định 0.7).\n\n"
            "**Trường hợp sử dụng**: Kiểm tra xem các số nóng gần đây có tiếp tục xuất hiện ở tỷ lệ trên mức trung bình hay không."
        ),
        "Chiến lược Số Lạnh": (
            "**Cách hoạt động**: Giống với Chiến lược Số Nóng nhưng xếp hạng các số theo "
            "thứ tự *ngược lại* (ít thường xuyên nhất trước). Nhóm được trọng số hóa cho trọng số cao hơn "
            "cho các số xuất hiện ít hơn trong cửa sổ nhìn lại.\n\n"
            "**Tham số chính**: `lookback_days` (mặc định 365), `selection_weight` (mặc định 0.7).\n\n"
            "**Trường hợp sử dụng**: Kiểm tra giả thuyết bổ sung rằng các số rất ít được rút "
            "có nhiều khả năng xuất hiện hơn (đảo chiều trung bình / ngộ nhận của người cờ bạc)."
        ),
        "Not Repeat Strategy": (
            "**How it works**: Collects all numbers that appeared in *any* draw within the "
            "last `lookback_days` days.  Whenever enough *non-recent* numbers exist to fill "
            "a full ticket they are sampled uniformly.  When the pool of non-recent numbers "
            "is too small, remaining slots are filled using an `avoid_weight` probability to "
            "decide whether to pick from recent numbers or from the full range.\n\n"
            "**Key parameters**: `lookback_days` (default 30), `avoid_weight` (default 0.8).\n\n"
            "**Use case**: Models the idea that numbers drawn recently are *less* likely to "
            "repeat in the very next draw."
        ),
        "Exponential Decay Strategy": (
            "**How it works**: Every historical draw contributes a score to each number it "
            "contained, but the contribution decays exponentially with age: "
            "``weight = exp(-ln(2) × days_ago / half_life_days)``.  Draws from yesterday "
            "contribute much more than draws from a year ago.  Numbers are then selected "
            "from a pool weighted by their accumulated scores.\n\n"
            "Unlike Hot/Cold Numbers Strategy there is **no hard window cutoff** — all "
            "history is used, with very old draws contributing negligibly.  The smooth "
            "decay avoids abrupt weight changes when a draw ages past a window boundary.\n\n"
            "**Key parameters**: `half_life_days` (default 90), `hot` (default True), "
            "`selection_weight` (default 0.8)."
        ),
        "Chiến lược Tần suất Cặp": (
            "**Cách hoạt động**: Xây dựng ma trận đồng xuất hiện từ các lần quay lịch sử: "
            "``cooccurrence[a][b]`` đếm các lần quay trong đó các số ``a`` và ``b`` cả hai "
            "xuất hiện. Các vé được lắp ráp lặp đi lặp lại:\n\n"
            "1. Số đầu tiên được lấy mẫu tỷ lệ với tần suất rút riêng lẻ.\n"
            "2. Mỗi số tiếp theo được lấy mẫu theo tỷ lệ với **điểm đồng xuất hiện trung bình** "
            "của nó với các số đã được chọn.\n\n"
            "Điều này tạo ra các cụm các số xuất hiện cùng nhau trong lịch sử, "
            "khai thác các tương quan bậc hai mà tất cả các chiến lược một chữ số bỏ qua.\n\n"
            "**Tham số chính**: `lookback_days` (mặc định 365)."
        ),
    }

    def _strategy_docs_section(self) -> str:
        """Return a markdown section documenting every strategy."""
        lines = ["## 📚 Mô tả Chiến lược\n"]
        for name, description in self._STRATEGY_DOCS.items():
            lines.append(f"### {name}\n\n{description}\n")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Summary assembly
    # ------------------------------------------------------------------

    def generate_prediction_summary(
        self,
        product: str = "power_655",
        seed: Optional[int] = None,
        seed_runs: int = 1,
        history_window: int = 30,
        oos_days: int = 365,
        oos_draws: Optional[int] = None,
    ) -> Tuple[str, List[List[Dict[str, float]]]]:
        """Generate the complete prediction summary content."""
        logger.info("Starting prediction summary generation...")

        product_cfg = get_config(product)
        df_product = self._load_lottery_data(product)
        if df_product.is_empty():
            return "# Lỗi\n\nKhông có dữ liệu.\n"

        df_pd = df_product.to_pandas()
        number_predict = product_cfg.size_output

        if seed_runs < 1:
            raise ValueError("seed_runs phải >= 1")

        run_metrics: List[List[Dict[str, float]]] = []
        strategies: Optional[List[_StrategyEntry]] = None

        for i in range(seed_runs):
            run_seed = (seed + i) if seed is not None else None
            self._set_seed(run_seed)
            run_strategies = self._build_and_run_strategies(
                df_pd,
                min_val=product_cfg.min_value,
                max_val=product_cfg.max_value,
                number_predict=number_predict,
            )
            run_metrics.append(self._collect_strategy_metrics(run_strategies))
            if strategies is None:
                strategies = run_strategies

        assert strategies is not None

        roi_table = self._roi_comparison_table(strategies)
        roi_dual_tables = self._generate_roi_dual_tables(
            strategies,
            df_pd,
            oos_days=oos_days,
            oos_draws=oos_draws,
        )
        roi_chart = self._generate_roi_bar_chart(strategies)
        compact_table = self._generate_compact_strategy_table(strategies, df_pd, product=product, top_k=number_predict)
        future_forecast = self._generate_future_number_forecast(
            strategies,
            df_pd,
            product=product,
            top_k=number_predict,
        )
        oos_section = self._generate_oos_section(
            strategies,
            df_pd,
            oos_days=oos_days,
            oos_draws=oos_draws,
        )
        stability_table = self._stability_section(run_metrics)
        history_leaderboard = self._history_leaderboard_section(product=product, history_window=history_window)
        seed_note = (
            f"> **Seed**: {seed} (deterministic), **Seed runs**: {seed_runs}\n"
            if seed is not None
            else f"> **Seed**: ngẫu nhiên, **Seed runs**: {seed_runs}\n"
        )

        summary = f"""# 🔮 Tóm tắt Dự đoán Vietlott {product.replace('_', ' ').title()}

> **Được tạo**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
{seed_note}>
>
> Tài liệu này chứa các dự đoán học máy cho dữ liệu xổ số Việt Nam.
> Đây là một mô-đun thử nghiệm chỉ dành cho mục đích giáo dục.

{roi_table}

{roi_dual_tables}

{roi_chart}

{compact_table}

{future_forecast}

{oos_section}

{stability_table}

{history_leaderboard}

---

## ⚠️ Tuyên bố Miễn trách nhiệm

Tóm tắt dự đoán này chỉ dành cho mục đích giáo dục và nghiên cứu. Kết quả xổ số ngẫu nhiên và không thể dự đoán một cách đáng tin cậy. Không bao giờ cờ bạc nhiều hơn những gì bạn có thể mất được.
"""

        return summary, run_metrics

    def save_prediction_summary(
        self,
        product: str = "power_655",
        output_path: Optional[Path] = None,
        seed: Optional[int] = None,
        seed_runs: int = 1,
        history_window: int = 30,
        oos_days: int = 365,
        oos_draws: Optional[int] = None,
    ) -> None:
        """Generate and save prediction summary to file."""
        if output_path is None:
            output_name = "readme.md" if product == "power_655" else f"readme_{product}.md"
            output_path = Path(__file__).parent / output_name

        try:
            summary_content, run_metrics = self.generate_prediction_summary(
                product=product,
                seed=seed,
                seed_runs=seed_runs,
                history_window=history_window,
                oos_days=oos_days,
                oos_draws=oos_draws,
            )

            with output_path.open("w", encoding="utf-8") as ofile:
                ofile.write(summary_content)

            self._append_history(
                product=product,
                seed=seed,
                seed_runs=seed_runs,
                output_path=output_path,
                run_metrics=run_metrics,
            )

            logger.info(f"Tóm tắt dự đoán đã được lưu thành công vào {output_path.absolute()}")
        except Exception as e:
            logger.error(f"Lỗi khi lưu tóm tắt dự đoán: {e}")
            raise


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for prediction summary generation."""
    parser = argparse.ArgumentParser(description="Generate prediction summary for a Vietlott product")
    parser.add_argument("--product", default="power_655", help="Product name, e.g. power_655 or power_645")
    parser.add_argument("--output", default=None, help="Optional output markdown path")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for deterministic runs")
    parser.add_argument("--seed-runs", type=int, default=1, help="Number of runs with sequential seeds")
    parser.add_argument("--history-window", type=int, default=30, help="Number of recent history records for leaderboard")
    parser.add_argument("--oos-days", type=int, default=365, help="Out-of-sample window size in days")
    parser.add_argument("--oos-draws", type=int, default=None, help="Out-of-sample window by recent draw count")
    return parser.parse_args()


def main():
    """Main entry point for prediction summary generation."""
    try:
        args = parse_args()
        generator = PredictionSummaryGenerator()
        output_path = Path(args.output) if args.output else None
        generator.save_prediction_summary(
            product=args.product,
            output_path=output_path,
            seed=args.seed,
            seed_runs=args.seed_runs,
            history_window=args.history_window,
            oos_days=args.oos_days,
            oos_draws=args.oos_draws,
        )
        logger.info("Prediction summary generation completed successfully!")
    except Exception as e:
        logger.error(f"Failed to generate prediction summary: {e}")
        raise


if __name__ == "__main__":
    main()
