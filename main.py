import pandas as pd
from database_utils  import DatabaseConnector 
from data_extraction import DataExtractor 
from data_cleaning   import DataCleaning
from pandasgui import show


def upload_dim_users():
    de = DataExtractor()
    db = DatabaseConnector()
    dc = DataCleaning()    

    cred = db.read_db_creds('db_creds.yaml')
    engine = db.init_db_engine(cred)
    engine.connect()
    table_list = db.list_db_tables(engine)
    df_name = table_list[1]
    df = dc.clean_user_data(de.read_rds_table(engine, df_name))
    show(df)
    print(df.head())
    
    cred_local   = db.read_db_creds("local_details.yaml") 
    print(cred_local)
    sql_engine = db.init_db_engine(cred_local)
    sql_engine.connect()
    db.upload_to_db(df,'dim_users',sql_engine)
    print(sql_engine)
upload_dim_users()

def upload_card_details():
    de = DataExtractor()
    db = DatabaseConnector()
    dc = DataCleaning()    
    file_path = 'dmitry@pc-11-251/Downloads/cards.csv' 
    df = pd.read_csv(file_path)
    #df = de.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')
    print(df.head())
    print(df.info())
    df = dc.clean_card_data(de.read_rds_table(engine,df))

    cred = db.read_db_creds('local_details.yaml')
    engine = db.init_db_engine(cred)
    engine.connect()
    db.upload_to_db(df,'dim_card_details', engine)
    print(engine)
upload_card_details()





# def upload_dim_store_details():
#     de = DataExtractor()
#     db = DatabaseConnector()
#     dc = DataCleaning()  
#     # get data
#     df = de.retrieve_stores_data()
#     print(df[df['store_code']=='WEB-1388012W'])
#     df.to_csv('dim_store_details.csv')
#     # clean data 
#     df = dc.called_clean_store_data(df)
#     # upload to db 
#     cred   = db.read_db_creds("local_details.yaml") 
#     engine = db.init_db_engine(cred)
#     engine.connect()
#     db.upload_to_db(df,'dim_store_details',engine)
#     print(engine)


# def upload_dim_products(self,df):
#     de = DataExtractor()
#     db = DatabaseConnector()
#     dc = DataCleaning()  

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

