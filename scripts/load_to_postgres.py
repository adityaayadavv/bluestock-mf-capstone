from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

from config import DB_CONFIG

# -----------------------------
# Database Connection
# -----------------------------
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_CONFIG['username']}:"
    f"{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:"
    f"{DB_CONFIG['port']}/"
    f"{DB_CONFIG['database']}"
)

engine = create_engine(DATABASE_URL)

# -----------------------------
# Paths
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW = PROJECT_ROOT / "data" / "raw"

# -----------------------------
# Load dim_fund
# -----------------------------
print("\nLoading dim_fund...")

fund_df = pd.read_csv(RAW / "01_fund_master.csv")

fund_df["launch_date"] = pd.to_datetime(
    fund_df["launch_date"],
    errors="coerce"
)

fund_df = fund_df[
    [
        "amfi_code",
        "fund_house",
        "scheme_name",
        "category",
        "sub_category",
        "plan",
        "launch_date",
        "benchmark",
        "expense_ratio_pct",
        "exit_load_pct",
        "min_sip_amount",
        "min_lumpsum_amount",
        "fund_manager",
        "risk_category",
        "sebi_category_code"
    ]
]

fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="append",
    index=False
)

print(f"Loaded {len(fund_df)} rows")

# -----------------------------
# Load fact_nav
# -----------------------------
print("\nLoading fact_nav...")

nav_df = pd.read_csv(
    RAW / "02_nav_history.csv"
)

nav_df.rename(
    columns={"date": "nav_date"},
    inplace=True
)

nav_df["nav_date"] = pd.to_datetime(
    nav_df["nav_date"],
    errors="coerce"
)

nav_df = nav_df[
    [
        "amfi_code",
        "nav_date",
        "nav"
    ]
]

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="append",
    index=False
)

print(f"Loaded {len(nav_df)} rows")

# -----------------------------
# Load fact_aum
# -----------------------------
print("\nLoading fact_aum...")

aum_df = pd.read_csv(
    RAW / "03_aum_by_fund_house.csv"
)

aum_df.rename(
    columns={"date": "report_date"},
    inplace=True
)

aum_df["report_date"] = pd.to_datetime(
    aum_df["report_date"],
    errors="coerce"
)

aum_df = aum_df[
    [
        "report_date",
        "fund_house",
        "aum_lakh_crore",
        "aum_crore",
        "num_schemes"
    ]
]

aum_df.to_sql(
    "fact_aum",
    engine,
    if_exists="append",
    index=False
)

print(f"Loaded {len(aum_df)} rows")

# -----------------------------
# Load fact_sip_industry
# -----------------------------
print("\nLoading fact_sip_industry...")

sip_df = pd.read_csv(
    RAW / "04_monthly_sip_inflows.csv"
)

sip_df = sip_df[
    [
        "month",
        "sip_inflow_crore",
        "active_sip_accounts_crore",
        "new_sip_accounts_lakh",
        "sip_aum_lakh_crore",
        "yoy_growth_pct"
    ]
]

sip_df.to_sql(
    "fact_sip_industry",
    engine,
    if_exists="append",
    index=False
)

print(f"Loaded {len(sip_df)} rows")

# -----------------------------
# Load fact_performance
# -----------------------------
print("\nLoading fact_performance...")

perf_df = pd.read_csv(
    RAW / "07_scheme_performance.csv"
)

perf_df = perf_df[
    [
        "amfi_code",
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "benchmark_3yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "std_dev_ann_pct",
        "max_drawdown_pct",
        "aum_crore",
        "expense_ratio_pct",
        "morningstar_rating",
        "risk_grade"
    ]
]

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="append",
    index=False
)

print(f"Loaded {len(perf_df)} rows")

# -----------------------------
# Load fact_transactions
# -----------------------------
print("\nLoading fact_transactions...")

tx_df = pd.read_csv(
    RAW / "08_investor_transactions.csv"
)

tx_df["transaction_date"] = pd.to_datetime(
    tx_df["transaction_date"],
    errors="coerce"
)

tx_df = tx_df[
    [
        "investor_id",
        "transaction_date",
        "amfi_code",
        "transaction_type",
        "amount_inr",
        "state",
        "city",
        "city_tier",
        "age_group",
        "gender",
        "annual_income_lakh",
        "payment_mode",
        "kyc_status"
    ]
]

tx_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="append",
    index=False
)

print(f"Loaded {len(tx_df)} rows")

# -----------------------------
# Load fact_portfolio
# -----------------------------
print("\nLoading fact_portfolio...")

portfolio_df = pd.read_csv(
    RAW / "09_portfolio_holdings.csv"
)

portfolio_df["portfolio_date"] = pd.to_datetime(
    portfolio_df["portfolio_date"],
    errors="coerce"
)

portfolio_df = portfolio_df[
    [
        "amfi_code",
        "stock_symbol",
        "stock_name",
        "sector",
        "weight_pct",
        "market_value_cr",
        "current_price_inr",
        "portfolio_date"
    ]
]

portfolio_df.to_sql(
    "fact_portfolio",
    engine,
    if_exists="append",
    index=False
)

print(f"Loaded {len(portfolio_df)} rows")

print("\nSUCCESS: All data loaded!")