# Data Dictionary

## dim_fund

| Column | Description |
|----------|-------------|
| amfi_code | Unique AMFI scheme identifier |
| fund_house | Mutual fund company |
| scheme_name | Scheme name |
| category | Fund category |
| sub_category | Fund sub-category |
| launch_date | Scheme launch date |
| risk_category | Risk classification |

---

## fact_nav

| Column | Description |
|----------|-------------|
| amfi_code | Fund identifier |
| nav_date | NAV date |
| nav | Net Asset Value |

---

## fact_performance

| Column | Description |
|----------|-------------|
| return_1yr_pct | 1 year return |
| return_3yr_pct | 3 year return |
| return_5yr_pct | 5 year return |
| sharpe_ratio | Risk-adjusted return metric |
| sortino_ratio | Downside risk metric |
| alpha | Excess return |
| beta | Market sensitivity |

---

## fact_transactions

| Column | Description |
|----------|-------------|
| investor_id | Investor identifier |
| transaction_date | Transaction date |
| transaction_type | SIP/Lumpsum/Redemption |
| amount_inr | Transaction amount |
| state | Investor state |
| city | Investor city |
| kyc_status | KYC verification status |

---

## fact_portfolio

| Column | Description |
|----------|-------------|
| stock_symbol | Stock ticker |
| stock_name | Stock name |
| sector | Industry sector |
| weight_pct | Portfolio allocation |
| market_value_cr | Market value |