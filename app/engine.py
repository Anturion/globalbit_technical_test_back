from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from database import engine_azure

def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD %s %s' % (table_name, column_name, column_type))

token_session = Column('token_session', String(100))
add_column(engine_azure, 'users', token_session)