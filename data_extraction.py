from sqlalchemy import inspect
import boto3
import pandas as pd
import tabula
import requests
import numpy as np
import io


link = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'



def retrieve_pdf_data(self,link):
   #retrieves pdf data from a link and turns it into a pandas dataframe
    return pd.concat(tabula.read_pdf(link, pages='all'))

# run = tabula.read_pdf('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf',pages=all)
# print(run)

class DataExtractor:
   
   def __init__(self):
      pass

   def read_rds_table(self,engine,table_name):
      #reads our table and turns it into an sql table
      with engine.connect() as conn:
         return pd.read_sql_table(table_name, con=conn)
      
   def retrieve_pdf_data(self,link):
      #takes pdf data in and returns a pandas dataframe
    return pd.concat(tabula.read_pdf(link, pages='all',stream=False))
      
   
   def list_number_of_stores(self):
      api_key = {'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
      #api key used to access the info on aws
      store_number = requests.get('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores',headers= api_key).json()
      return store_number['number_stores']

   

   def retrieve_stores_data(self):
      api_key = {'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
      number_of_stores = self.list_number_of_stores()
      stores_list = []
      for store_number in range(0,number_of_stores):
            store = (requests.get('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/'+str(store_number), headers= api_key).json())
            store_df = pd.DataFrame(store, index=[np.NaN])
            stores_list.append(store_df)
      df = pd.concat(stores_list)
      df.to_csv('store_list.csv')
      print(df.head())
      return df  
   


   def extract_from_s3(self):
      s3 = boto3.client('s3')
      bucket = 'data-handling-public'
      file_name = 'products.csv'
      obj = s3.get_object(bucket = bucket, key= file_name)
      table = pd.read_csv((io.BytesIO(obj['Body'].read())))
      return table

   
      
   
 

   # def extract_json_from_s3(s3_address):
   #    s3_address = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'
   #    response = requests.get(s3_address)
   #    data = response.json()
   #    dates_and_times = pd.DataFrame(data)
   #    return dates_and_times
   



 






   def extract_from_s3(self):
        s3 = boto3.client('s3')
        bucket = 'data-handling-public'
        object = 'products.csv'
        file = 'products.csv'
        s3.download_file(bucket,object,file)
        table = pd.read_csv('./products.csv')
        return table

   
   # def extract_from_s3(self):
   #    s3_client = boto3.client(3)
   #    response = s3_client.get_object(Bucket='data-handling-public',key = 'products.csv')
   #    status  = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
   #    if status == 200:
   #       print(f'success!{status}')
   #       return pd.read_csv(response.get('body'))
   #    else:
   #       print(f'Unsuccesful{status}')

    
   # def extract_from_s3_link(self):
   #    url = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'
   #    response = requests.get(url)
   #    dic = response.json
   #    df = pd.DataFrame([])
   #    for column_name in dic.keys():
   #       value_list = []
   #       for i in dic[column_name].keys():
   #          value_list.append(dic[column_name][_])
   #          df[column_name] = value_list
   #    return df
      
      





      
