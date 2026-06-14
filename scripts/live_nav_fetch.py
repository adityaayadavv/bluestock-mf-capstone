"""
Live NAV Fetch Module

Author: Aditya Yadav
Project: Bluestock Mutual Fund Analytics Platform

Description:
Retrieves the latest Net Asset Value (NAV) data
for mutual fund schemes and stores the results
for analysis and reporting purposes.
"""

from pathlib import Path
import pandas as pd
import requests

# ----------------------------------
# Paths
# ----------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW = PROJECT_ROOT / "data" / "raw"

RAW.mkdir(parents=True, exist_ok=True)

# ----------------------------------
# API Configuration
# ----------------------------------
BASE_URL = "https://api.mfapi.in/mf"

# ----------------------------------
# Fund Codes
# ----------------------------------
FUNDS = {
    "hdfc_top_100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841,
}

print("=" * 80)
print("BLUESTOCK LIVE NAV FETCH")
print("=" * 80)

# ----------------------------------
# Fetch NAV Data
# ----------------------------------
for fund_name, amfi_code in FUNDS.items():

    print(f"\nFetching {fund_name} ({amfi_code})...")

    url = f"{BASE_URL}/{amfi_code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        output_file = RAW / f"{fund_name}_nav.csv"

        nav_df.to_csv(output_file, index=False)

        print(
            f"✓ Saved {len(nav_df)} rows -> {output_file.name}"
        )

    except requests.exceptions.RequestException as e:
        print(
            f"✗ Failed to fetch {fund_name}: {e}"
        )

print("\nNAV download completed.")