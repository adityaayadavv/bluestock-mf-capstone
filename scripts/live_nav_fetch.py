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
# Fund Codes
# ----------------------------------
FUNDS = {
    "hdfc_top_100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}


# ----------------------------------
# Fetch NAV Data
# ----------------------------------
for fund_name, amfi_code in FUNDS.items():

    print(f"\nFetching {fund_name} ({amfi_code})...")

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed: {fund_name}")
        continue

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    output_file = RAW / f"{fund_name}_nav.csv"

    nav_df.to_csv(output_file, index=False)

    print(
        f"Saved {len(nav_df)} rows -> {output_file.name}"
    )

print("\nSUCCESS: NAV files downloaded.")