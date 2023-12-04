import yaml
from yaml.loader import SafeLoader
from sqlalchemy import create_engine
import pandas as pd
import psycopg2
from sqlalchemy import inspect


class DatabaseConnector:

    #def __init__(self) -> None:
        #pass

    def read_db_creds(self,cred_path):
        with open(cred_path,'r') as stream:
            cred = yaml.safe_load(stream)
            print(cred)
            return cred


    def init_db_engine(self,cred):
        engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{cred['USER']}:{cred['PASSWORD']}@{cred['HOST']}:{cred['PORT']}/{cred['DATABASE']}")
        engine.connect()
        return engine

    def list_db_tables(self,engine):
        inspector = inspect(engine)
        return inspector.get_table_names()    
    
    def upload_to_db(self,df,table,sql_engine):
        df.to_sql(table,sql_engine ,if_exists='replace')


if __name__ == '__main__':
    instance = DatabaseConnector()
    creds = instance.read_db_creds('db_creds.yaml')
    engine = instance.init_db_engine(creds)
    engine.connect()
    table_list = instance.list_db_tables(engine)
    print(table_list)
    # with engine.connect() as conn:
    #     table=pd.read_sql_table(table_list[1],con=conn)
    #     print(table)

