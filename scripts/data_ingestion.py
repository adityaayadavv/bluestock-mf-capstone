from pathlib import Path
import pandas as pd

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("=" * 80)
print("BLUESTOCK MUTUAL FUND DATA INGESTION")
print("=" * 80)

for file in files:
    file_path = RAW_DATA_PATH / file

    try:
        df = pd.read_csv(file_path)

        print("\n" + "=" * 80)
        print(f"FILE: {file}")
        print("=" * 80)

        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 3 Rows:")
        print(df.head(3))

    except Exception as e:
        print(f"\nError reading {file}")
        print(e)