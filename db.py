import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = snowflake.connector.connect(
        user = os.getenv("SNOW_USERNAME"),
        password = os.getenv("PASSWORD"),
        account = os.getenv("ACCOUNT"),
        warehouse = os.getenv("WAREHOUSE"),
        database = os.getenv("DATABASE"),
        schema = os.getenv("SCHEMA")
    )
    return conn



