from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///db/source.db')
meta = MetaData()

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String),
)

orders = Table(
    'orders', meta,
    Column('order_id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('amount', Integer),
)

meta.create_all(engine)

with engine.begin() as conn:
    conn.execute(users.insert(), [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'},
    ])
    conn.execute(orders.insert(), [
        {'user_id': 1, 'amount': 200},
        {'user_id': 2, 'amount': 300},
    ])

print("Dummy database created.")
