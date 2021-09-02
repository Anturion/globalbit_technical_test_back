import os
import pyodbc
import urllib
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

driver=os.getenv('DRIVER')
server=os.getenv('SERVER')
database=os.getenv('DATABASE')
user=os.getenv('USER')
pwd=os.getenv('PWD')
#pwd="Hopeusers!"
# urllib.parse.quote_plus for python 3

conn_str = f'Driver={driver};Server={server};Database={database};Uid={user};Pwd={pwd};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": conn_str})
engine_azure = create_engine(connection_url)

print(engine_azure.table_names())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_azure)

Base = declarative_base()