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
'''This function connects to our engine on aws using the details stored in our db_creds file then returns a list of tables 
we then clean the table data removing null values and upload this into our local engine as dim users'''


    cred = db.read_db_creds('db_creds.yaml')
    #read credentials file
    engine = db.init_db_engine(cred)
    engine.connect()
    #connects to engine
    table_list = db.list_db_tables(engine)
    #lists tables
    df_name = table_list[1]
    df = dc.clean_user_data(de.read_rds_table(engine, df_name))
    #cleans table
    cred_local   = db.read_db_creds("local_details.yaml") 
    print(cred_local)
    sql_engine = db.init_db_engine(cred_local)
    sql_engine.connect()
    #connects to local engine
    db.upload_to_db(df,'dim_users',sql_engine)
    #uploads to local engine
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
    #calls function where we retrieve the store data
    df = dc.clean_store_data(df)
    df = df.reset_index(drop=True)
    print(df)
    cred = db.read_db_creds('local_details.yaml')
    engine = db.init_db_engine(cred)
    engine.connect()
    db.upload_to_db(df,'dim_store_details', engine)
    print(engine)
dim_store = upload_dim_store_details()




def upload_dim_products():
    df = de.extract_from_s3()
    #gets data from s3
    df = dc.convert_product_weights(df,'weight')
    df = dc.clean_products_data(df)
    cred = db.read_db_creds('local_details.yaml')
    engine = db.init_db_engine(cred)
    engine.connect()
    db.upload_to_db(df,'dim_products', engine)
    print(engine)
#upload_dim_products()







def upload_orders():
    cred   = db.read_db_creds("db_creds.yaml") 
    engine = db.init_db_engine(cred)
    engine.connect()
    tables_list = db.list_db_tables(engine)
    df_name = tables_list[2]
    df = de.read_rds_table(engine, df_name)
    df.to_csv('orders_table.csv')    
    # converts to csv
    df = dc.clean_orders_data(df)
    print(df['product_quantity'].sum())
    # upload to our postgres server 
    cred   = db.read_db_creds("local_details.yaml") 
    engine = db.init_db_engine(cred)
    engine.connect()
    db.upload_to_db(df,'orders_table',engine)
    print(engine)
upload_orders()





def dim_date_times():
    df = de.extract_json_from_s3()
    df.to_csv('dim_date_times.csv')
    df = dc.clean_date_time(df)
    cred   = db.read_db_creds("local_details.yaml") 
    engine = db.init_db_engine(cred)
    engine.connect()
    db.upload_to_db(df,'dim_date_times',engine)
    print(engine)
dates = dim_date_times()