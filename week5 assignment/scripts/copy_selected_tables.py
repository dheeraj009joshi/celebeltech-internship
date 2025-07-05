import pandas as pd
from sqlalchemy import create_engine
import json

source_engine = create_engine('sqlite:///db/source.db')
dest_engine = create_engine('sqlite:///db/destination.db')

with open('config/tables_config.json') as f:
    config = json.load(f)

for table, columns in config.items():
    df = pd.read_sql_query(f"SELECT {', '.join(columns)} FROM {table}", source_engine)
    df.to_sql(table, dest_engine, if_exists='replace', index=False)

print("Selected tables/columns copied based on config.")
