import pandas as pd
from database_utils  import DatabaseConnector 
from data_extraction import DataExtractor 
from data_cleaning   import DataCleaning
from pandasgui import show
import requests

de = DataExtractor()
db = DatabaseConnector()
dc = DataCleaning() 

def upload_dim_users():
    cred = db.read_db_creds('db_creds.yaml')
    engine = db.init_db_engine(cred)
    engine.connect()
    table_list = db.list_db_tables(engine)
    df_name = table_list[1]
    df = dc.clean_user_data(de.read_rds_table(engine, df_name))
    #show(df)
    #print(df.head())
    
    cred_local   = db.read_db_creds("local_details.yaml") 
    print(cred_local)
    sql_engine = db.init_db_engine(cred_local)
    sql_engine.connect()
    db.upload_to_db(df,'dim_users',sql_engine)
    print(sql_engine)
upload_dim_users()

def upload_dim_card_details():
    df = pd.read_csv('cards.csv')
    #df = de.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')
    print(df.head())
    print(df.info())
    df = dc.clean_card_data(df)
    #show(df)
    cred = db.read_db_creds('local_details.yaml')
    engine = db.init_db_engine(cred)
    engine.connect()
    db.upload_to_db(df,'dim_card_details', engine)
    print(engine)
upload_dim_card_details()


def upload_dim_store_details():
    df = de.retrieve_stores_data()
    df = dc.clean_store_data(df)
    df = df.reset_index(drop=True)
    print(df)
    cred = db.read_db_creds('local_details.yaml')
    engine = db.init_db_engine(cred)
    engine.connect()
    db.upload_to_db(df,'dim_store_details', engine)
    print(engine)
dim_store = upload_dim_store_details()















# def upload_dim_products():
#     cred = db.read_db_creds('local_details.yaml')
#     engine = db.init_db_engine(cred)
#     engine.connect()
#     db.upload_to_db(df,'dim_products', engine)
#     print(engine)





# def upload_dim_products(self,df):

#     df = de.extract_from_s3()

#     cred   = db.read_db_creds("local_details.yaml") 
#     engine = db.init_db_engine(cred)
#     engine.connect()
#     db.upload_to_db(df,'dim_products',engine)
#     print(engine)



# def upload_orders():
#     de = DataExtractor()
#     db = DatabaseConnector()
#     dc = DataCleaning()
#     # connect to db
#     cred   = db.read_db_creds("db_creds_remote.yaml") 
#     engine = db.init_db_engine(cred)
#     engine.connect()
#     tables_list = db.list_db_tables(engine)
#     # get frame name and download
#     df_name = tables_list[2]
#     df = de.read_rds_table( engine, df_name)
#     df.to_csv('orders_table.csv')    
#     # clean data 
#     df = dc.clean_order_data(df)
#     print(df.info())
#     print(df['product_quantity'].sum())
#     # upload to db 
#     cred   = db.read_db_creds("local_details.yaml") 
#     engine = db.init_db_engine(cred)
#     engine.connect()
#     db.upload_to_db(df,'dim_upload_orders',engine)
#     print(engine)

# def dim_date_times():
#     de = DataExtractor()
#     db = DatabaseConnector()
#     dc = DataCleaning()

#     df = de.extract_from_s3_by_link()
#     df.to_csv('dim_date_times.csv')
    
#     df = dc.clean_date_time(df)
#     cred   = db.read_db_creds("local_details.yaml") 
#     engine = db.init_db_engine(cred)
#     engine.connect()
#     db.upload_to_db(df,'dim_date_times',engine)
#     print(engine)

