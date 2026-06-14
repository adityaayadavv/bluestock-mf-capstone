"""
Data Profiling Module

Author: Aditya Yadav
Project: Bluestock Mutual Fund Analytics Platform

Description:
Performs exploratory profiling of datasets by
analyzing data types, missing values, duplicates,
summary statistics, and overall data quality.
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

FILES = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv",
]

print("=" * 80)
print("BLUESTOCK MUTUAL FUND DATA PROFILING")
print("=" * 80)

for file in FILES:

    df = pd.read_csv(RAW_DATA_PATH / file)

    print("\n" + "=" * 80)
    print(f"DATASET: {file}")
    print("=" * 80)

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

print("\nData profiling completed.")