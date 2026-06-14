"""
Data Ingestion Module

Author: Aditya Yadav
Project: Bluestock Mutual Fund Analytics Platform

Description:
Loads raw mutual fund datasets from CSV files,
performs initial validation checks, and verifies
file availability before downstream processing.
"""

from pathlib import Path
import pandas as pd

# Project root
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
print("BLUESTOCK MUTUAL FUND DATA INGESTION")
print("=" * 80)

for file in FILES:
    file_path = RAW_DATA_PATH / file

    try:
        df = pd.read_csv(file_path)

        print(
            f"✓ {file} loaded successfully "
            f"({df.shape[0]} rows, {df.shape[1]} columns)"
        )

    except Exception as e:
        print(f"✗ Failed to load {file}")
        print(f"Error: {e}")

print("\nData ingestion completed.")