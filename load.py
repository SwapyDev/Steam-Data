from db import get_connection
import pandas as pd
def load_to_snowflake(df: pd.DataFrame):
    conn = get_connection()
    cursor = conn.cursor()

    for index, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO game_sales(title, original_price, current_price, discount)
            VALUES (%s, %s, %s, %s)
            """,
            (row['Game Title'], row['Original Price'], row['Current Price'], row['Discount'])
        )
    conn.commit()
        