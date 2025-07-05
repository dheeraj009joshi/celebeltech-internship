import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from fastavro import writer, parse_schema
from sqlalchemy import create_engine
import os

engine = create_engine('sqlite:///db/source.db')
os.makedirs("exports", exist_ok=True)

def export_table(table_name):
    df = pd.read_sql_table(table_name, engine)

    df.to_csv(f"exports/{table_name}.csv", index=False)

    table = pa.Table.from_pandas(df)
    pq.write_table(table, f"exports/{table_name}.parquet")

    records = df.to_dict(orient='records')
    schema = {
        'doc': f'{table_name} schema',
        'name': table_name,
        'namespace': 'example.avro',
        'type': 'record',
        'fields': [{'name': col, 'type': 'string'} for col in df.columns]
    }

    with open(f"exports/{table_name}.avro", 'wb') as out:
        writer(out, parse_schema(schema), records)

for table in ['users', 'orders']:
    export_table(table)

print("Data exported to CSV, Parquet, and Avro.")
