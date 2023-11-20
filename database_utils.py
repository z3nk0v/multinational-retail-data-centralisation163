import yaml
from yaml.loader import SafeLoader
from sqlalchemy import create_engine
import pandas as pd
import psycopg2
from sqlalchemy import inspect


class DatabaseConnector:

    #def __init__(self) -> None:
        #pass

    def read_db_creds(self):
        with open('db_creds.yaml','r') as stream:
            cred = yaml.safe_load(stream)
            print(cred)
            return cred


    def init_db_engine(self,cred):
        engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{cred['RDS_USER']}:{cred['RDS_PASSWORD']}@{cred['RDS_HOST']}:{cred['RDS_PORT']}/{cred['RDS_DATABASE']}")
        engine.connect()
        return engine

    def list_db_tables(self,engine):
        inspector = inspect(engine)
        return inspector.get_table_names()    



instance = DatabaseConnector()
creds = instance.read_db_creds()
engine = instance.init_db_engine(creds)
engine.connect()
table_list = instance.list_db_tables(engine)
print(table_list)
with engine.connect() as conn:
    table=pd.read_sql_table(table_list[1],con=conn)
    print(table)

#variable = DatabaseConnector()
#variable.read_db_creds()



    #def list_db_tables():    
    #SELECT * FROM 
        
    #def read_rds_table():

    #upload_to_db
    #dim users