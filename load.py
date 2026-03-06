from db import get_connection
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
from dotenv import load_dotenv
import os 

load_dotenv()

def load_to_snowflake(df: pd.DataFrame):
    df.columns = [col.upper() for col in df.columns]

    #snowflake allows to upload pandas dataframes, so cool xd
    success, nchunks, nrows, _ = write_pandas(
    conn=get_connection(),
    df=df,
    table_name='GAME_SALES',
    database=os.getenv("DATABASE"),      
    schema=os.getenv("SCHEMA")     
    )

    #for index, row in df.iterrows():
        #cursor.execute(
    """
            INSERT INTO game_sales(title, original_price, current_price, discount, img_src)
            VALUES (%s, %s, %s, %s, %s)
            """,
            #(row['Game Title'], row['Original Price'], row['Current Price'], row['Discount'], row['Source Image'])
        #)
    #conn.commit()
        