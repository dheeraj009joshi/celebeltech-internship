from sqlalchemy import create_engine

def get_engine(path):
    return create_engine(f'sqlite:///{path}')
