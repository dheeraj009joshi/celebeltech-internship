import pandas as pd
from sqlalchemy import create_engine, MetaData

source_engine = create_engine('sqlite:///db/source.db')
dest_engine = create_engine('sqlite:///db/destination.db')

meta = MetaData(bind=source_engine)
meta.reflect()

for table in meta.tables:
    df = pd.read_sql_table(table, source_engine)
    df.to_sql(table, dest_engine, if_exists='replace', index=False)

print("All tables copied from source to destination.")
