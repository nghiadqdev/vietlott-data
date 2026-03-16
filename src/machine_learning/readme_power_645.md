# 🔮 Vietlott Power 645 Prediction Summary

> **Generated**: 2026-03-16 15:25:38
>
> This document contains machine learning predictions for Vietnamese lottery data.
> This is an experimental module for educational purposes only.

## 📊 Strategy Performance Comparison

> Sorted by ROI (best → worst).  All strategies backtested with **20 tickets/draw**.
> Note: All ROIs are deeply negative — lottery odds make profit impossible at scale.
> The comparison shows *which strategy loses the least*, not which one is profitable.

| Rank | Strategy | Total Cost (VND) | Total Gain (VND) | Net Profit (VND) | ROI |
|------|----------|-----------------|-----------------|-----------------|-----|
| 🥇 1 | Long Absence Strategy | 296,800,000 | 10,047,850,000 | 9,751,050,000 | 3285.39% |
| 🥈 2 | Random Strategy | 296,800,000 | 10,047,750,000 | 9,750,950,000 | 3285.36% |
| 🥉 3 | Hot Numbers Strategy | 296,800,000 | 5,056,750,000 | 4,759,950,000 | 1603.76% |
|    4 | Not Repeat Strategy | 296,800,000 | 60,150,000 | -236,650,000 | -79.73% |
|    5 | Pattern Strategy | 296,800,000 | 58,100,000 | -238,700,000 | -80.42% |
|    6 | Pair Frequency Strategy | 296,800,000 | 57,700,000 | -239,100,000 | -80.56% |
|    7 | Cold Numbers Strategy | 296,800,000 | 56,400,000 | -240,400,000 | -81.00% |
|    8 | Exponential Decay Strategy | 296,800,000 | 49,900,000 | -246,900,000 | -83.19% |


## 📚 Strategy Descriptions

### Random Strategy

**How it works**: Generates tickets by shuffling all numbers in the valid range and picking the first `number_predict` entries.  Every number has an equal chance of being selected; no historical data is used.

**Use case**: Serves as an unbiased performance baseline.  Any strategy that cannot beat random selection over a large backtest offers no predictive value.

### Long Absence Strategy

**How it works**: For each draw date, looks back at all past draws and records the last date each number appeared.  Numbers are ranked by how many days have elapsed since they last appeared (numbers that have *never* appeared rank highest). A configurable pool of the `top_n` most-absent numbers is assembled, and `number_predict` numbers are randomly sampled from that pool.

**Key parameter**: `top_n` (default 10) – larger pool → more randomness; smaller pool → stronger bias toward the longest-absent numbers.

**Use case**: Captures the intuition that numbers that have been *overdue* for a long time are somehow more likely to appear.  (Note: for a fair lottery this intuition is mathematically incorrect, but the strategy is included for empirical comparison.)

### Pattern Strategy

**How it works**: Analyses two structural properties of historical draws in a rolling `lookback_days` window:

1. **Spacing patterns** – gaps between consecutive sorted numbers in a ticket.  The most common gaps are used to generate the next number by applying a sampled gap to the previously chosen number.
2. **Range distribution** – the number range 1–55 is split into five equal sub-ranges.  The historical fraction of draws falling in each sub-range is used as a probability weight for choosing the first number.

A `pattern_weight` fraction of the ticket is filled with pattern-derived numbers; the remainder is filled randomly.

**Key parameters**: `lookback_days` (default 180), `pattern_weight` (default 0.6).

### Hot Numbers Strategy

**How it works**: Counts how many times each number appeared over the last `lookback_days` days.  Numbers are sorted from most-frequent to least-frequent.  A weighted pool is built where each number is repeated proportionally to its frequency, then numbers are drawn without replacement from that pool.

A `selection_weight` fraction of the ticket is filled from the frequency-weighted pool; the rest is filled uniformly at random.

**Key parameters**: `lookback_days` (default 365), `selection_weight` (default 0.7).

**Use case**: Tests whether recently hot numbers continue to appear at above-average rates.

### Cold Numbers Strategy

**How it works**: Identical to Hot Numbers Strategy but ranks numbers in the *reverse* order (least frequent first).  The weighted pool gives higher weight to numbers that have appeared fewer times in the lookback window.

**Key parameters**: `lookback_days` (default 365), `selection_weight` (default 0.7).

**Use case**: Tests the complementary hypothesis that rarely-drawn numbers are more likely to appear (mean-reversion / gambler's fallacy).

### Not Repeat Strategy

**How it works**: Collects all numbers that appeared in *any* draw within the last `lookback_days` days.  Whenever enough *non-recent* numbers exist to fill a full ticket they are sampled uniformly.  When the pool of non-recent numbers is too small, remaining slots are filled using an `avoid_weight` probability to decide whether to pick from recent numbers or from the full range.

**Key parameters**: `lookback_days` (default 30), `avoid_weight` (default 0.8).

**Use case**: Models the idea that numbers drawn recently are *less* likely to repeat in the very next draw.

### Exponential Decay Strategy

**How it works**: Every historical draw contributes a score to each number it contained, but the contribution decays exponentially with age: ``weight = exp(-ln(2) × days_ago / half_life_days)``.  Draws from yesterday contribute much more than draws from a year ago.  Numbers are then selected from a pool weighted by their accumulated scores.

Unlike Hot/Cold Numbers Strategy there is **no hard window cutoff** — all history is used, with very old draws contributing negligibly.  The smooth decay avoids abrupt weight changes when a draw ages past a window boundary.

**Key parameters**: `half_life_days` (default 90), `hot` (default True), `selection_weight` (default 0.8).

### Pair Frequency Strategy

**How it works**: Builds a co-occurrence matrix from historical draws: ``cooccurrence[a][b]`` counts draws where numbers ``a`` and ``b`` both appeared.  Tickets are assembled iteratively:

1. The first number is sampled proportional to individual draw frequency.
2. Each subsequent number is sampled proportional to its **average co-occurrence score** with the numbers already selected.

This produces clusters of numbers that historically appear together, exploiting second-order correlations that all single-number strategies ignore.

**Key parameter**: `lookback_days` (default 365).


## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Random Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 45 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2016-07-20 00:00:00 |
| End date | 2026-03-15 00:00:00 |
| Total draws | 1,484 |
| Total predictions | 29,680 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 296,800,000 VND |
| Total gain | 10,047,750,000 VND |
| Net profit/loss | 9,750,950,000 VND |
| ROI | 3285.36% |

#### Match Distribution
  - **5 matches**: 2 times
  - **4 matches**: 35 times
  - **3 matches**: 605 times
  - **2 matches**: 4,507 times
  - **1 matches**: 12,572 times
  - **0 matches**: 11,959 times

#### Best Results (5+ matches)
| date                | result                  | predicted               |   correct_num |
|:--------------------|:------------------------|:------------------------|--------------:|
| 2024-05-29 00:00:00 | [4, 21, 25, 27, 35, 39] | [14, 4, 27, 21, 25, 35] |             5 |
| 2017-02-03 00:00:00 | [8, 17, 31, 32, 33, 39] | [39, 8, 31, 33, 26, 32] |             5 |

### 🎲 Long Absence Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Long Absence Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 45 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2016-07-20 00:00:00 |
| End date | 2026-03-15 00:00:00 |
| Total draws | 1,484 |
| Total predictions | 29,680 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 296,800,000 VND |
| Total gain | 10,047,850,000 VND |
| Net profit/loss | 9,751,050,000 VND |
| ROI | 3285.39% |

#### Match Distribution
  - **5 matches**: 2 times
  - **4 matches**: 33 times
  - **3 matches**: 627 times
  - **2 matches**: 4,301 times
  - **1 matches**: 12,677 times
  - **0 matches**: 12,040 times

#### Best Results (5+ matches)
| date                | result                   | predicted                |   correct_num |
|:--------------------|:-------------------------|:-------------------------|--------------:|
| 2025-03-26 00:00:00 | [17, 24, 25, 30, 35, 39] | [17, 22, 24, 25, 35, 39] |             5 |
| 2024-04-28 00:00:00 | [1, 13, 14, 22, 23, 37]  | [1, 8, 14, 22, 23, 37]   |             5 |

### 🎲 Pattern Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Pattern Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 45 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2016-07-20 00:00:00 |
| End date | 2026-03-15 00:00:00 |
| Total draws | 1,484 |
| Total predictions | 29,680 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 296,800,000 VND |
| Total gain | 58,100,000 VND |
| Net profit/loss | -238,700,000 VND |
| ROI | -80.42% |

#### Match Distribution
  - **4 matches**: 53 times
  - **3 matches**: 632 times
  - **2 matches**: 4,470 times
  - **1 matches**: 12,662 times
  - **0 matches**: 11,863 times

#### Best Results (5+ matches)
No results with 5+ matches found.

### 🎲 Hot Numbers Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Hot Numbers Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 45 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2016-07-20 00:00:00 |
| End date | 2026-03-15 00:00:00 |
| Total draws | 1,484 |
| Total predictions | 29,680 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 296,800,000 VND |
| Total gain | 5,056,750,000 VND |
| Net profit/loss | 4,759,950,000 VND |
| ROI | 1603.76% |

#### Match Distribution
  - **5 matches**: 1 times
  - **4 matches**: 50 times
  - **3 matches**: 635 times
  - **2 matches**: 4,510 times
  - **1 matches**: 12,725 times
  - **0 matches**: 11,759 times

#### Best Results (5+ matches)
| date                | result                  | predicted               |   correct_num |
|:--------------------|:------------------------|:------------------------|--------------:|
| 2019-12-15 00:00:00 | [3, 13, 15, 16, 22, 36] | [3, 15, 16, 22, 25, 36] |             5 |

### 🎲 Cold Numbers Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Cold Numbers Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 45 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2016-07-20 00:00:00 |
| End date | 2026-03-15 00:00:00 |
| Total draws | 1,484 |
| Total predictions | 29,680 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 296,800,000 VND |
| Total gain | 56,400,000 VND |
| Net profit/loss | -240,400,000 VND |
| ROI | -81.00% |

#### Match Distribution
  - **4 matches**: 45 times
  - **3 matches**: 678 times
  - **2 matches**: 4,529 times
  - **1 matches**: 12,608 times
  - **0 matches**: 11,820 times

#### Best Results (5+ matches)
No results with 5+ matches found.

### 🎲 Not Repeat Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Not Repeat Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 45 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2016-07-20 00:00:00 |
| End date | 2026-03-15 00:00:00 |
| Total draws | 1,484 |
| Total predictions | 29,680 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 296,800,000 VND |
| Total gain | 60,150,000 VND |
| Net profit/loss | -236,650,000 VND |
| ROI | -79.73% |

#### Match Distribution
  - **4 matches**: 68 times
  - **3 matches**: 523 times
  - **2 matches**: 4,595 times
  - **1 matches**: 12,495 times
  - **0 matches**: 11,999 times

#### Best Results (5+ matches)
No results with 5+ matches found.

### 🎲 Exponential Decay Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Exponential Decay Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 45 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2016-07-20 00:00:00 |
| End date | 2026-03-15 00:00:00 |
| Total draws | 1,484 |
| Total predictions | 29,680 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 296,800,000 VND |
| Total gain | 49,900,000 VND |
| Net profit/loss | -246,900,000 VND |
| ROI | -83.19% |

#### Match Distribution
  - **4 matches**: 34 times
  - **3 matches**: 658 times
  - **2 matches**: 4,478 times
  - **1 matches**: 12,549 times
  - **0 matches**: 11,961 times

#### Best Results (5+ matches)
No results with 5+ matches found.

### 🎲 Pair Frequency Strategy

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | Pair Frequency Strategy |
| Tickets per day | 20 |
| Ticket price | 10,000 VND |
| Number range | 1 - 45 |
| Numbers to pick | 6 |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | 2016-07-20 00:00:00 |
| End date | 2026-03-15 00:00:00 |
| Total draws | 1,484 |
| Total predictions | 29,680 |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | 296,800,000 VND |
| Total gain | 57,700,000 VND |
| Net profit/loss | -239,100,000 VND |
| ROI | -80.56% |

#### Match Distribution
  - **4 matches**: 52 times
  - **3 matches**: 634 times
  - **2 matches**: 4,559 times
  - **1 matches**: 12,446 times
  - **0 matches**: 11,989 times

#### Best Results (5+ matches)
No results with 5+ matches found.




---

## ⚠️ Disclaimer

This prediction summary is for educational and research purposes only. Lottery outcomes are random and cannot be reliably predicted. Never gamble more than you can afford to lose.
