"""
Database Connection Test Module

Author: Aditya Yadav
Project: Bluestock Mutual Fund Analytics Platform

Description:
Tests connectivity between Python and PostgreSQL
to verify database configuration and ensure
successful data loading operations.
"""

from sqlalchemy import create_engine

from config import DB_CONFIG

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_CONFIG['username']}:"
    f"{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:"
    f"{DB_CONFIG['port']}/"
    f"{DB_CONFIG['database']}"
)

try:
    engine = create_engine(DATABASE_URL)

    with engine.connect():
        print("✓ Connected to PostgreSQL.")

except Exception as e:
    print("✗ PostgreSQL connection failed.")
    print(f"Error: {e}")