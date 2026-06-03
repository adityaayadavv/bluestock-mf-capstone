from sqlalchemy import create_engine

USERNAME = "postgres"
PASSWORD = "aditya2003"
HOST = "localhost"
PORT = "5432"
DATABASE = "bluestock_mf"

DATABASE_URL = (
    f"postgresql+psycopg2://{USERNAME}:{PASSWORD}"
    f"@{HOST}:{PORT}/{DATABASE}"
)

try:
    engine = create_engine(DATABASE_URL)

    with engine.connect() as conn:
        print("SUCCESS: Connected to PostgreSQL!")

except Exception as e:
    print("Connection Failed")
    print(e)