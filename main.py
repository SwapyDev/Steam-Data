from scraper import extract
from transform import transform
from load import load_to_snowflake

data = extract()
print(data)
df = transform(data)
load_to_snowflake(df)