"""
Master Pipeline Runner

Author: Aditya Yadav
Project: Bluestock Mutual Fund Analytics Platform

Description:
Executes the complete ETL workflow including
database connection testing, data ingestion,
data profiling, NAV fetching, and PostgreSQL loading.
"""

import subprocess
import sys

SCRIPTS = [
    "test_connection.py",
    "data_ingestion.py",
    "data_profiling.py",
    "live_nav_fetch.py"
]

print("=" * 80)
print("BLUESTOCK MUTUAL FUND PIPELINE")
print("=" * 80)

for script in SCRIPTS:

    print(f"\nRunning {script}...")

    try:
        subprocess.run(
            [sys.executable, script],
            check=True
        )

        print(f"✓ {script} completed.")

    except subprocess.CalledProcessError:

        print(f"✗ {script} failed.")
        break

print("\nPipeline execution finished.")