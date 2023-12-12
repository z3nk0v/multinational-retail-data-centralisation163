from sqlalchemy import inspect
import boto3
import pandas as pd
import tabula
import requests
link = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'



def retrieve_pdf_data(self,link):
    return pd.concat(tabula.read_pdf(link, pages='all'))

# run = tabula.read_pdf('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf',pages=all)
# print(run)

class DataExtractor:
   
   def __init__(self):
      pass

   def read_rds_table(self,engine,table_name):
      with engine.connect() as conn:
         return pd.read_sql_table(table_name, con=conn)
      
   def retrieve_pdf_data(self,link):
    return pd.concat(tabula.read_pdf(link, pages='all',stream=False))
      
   
   def API_key(self):
      return {'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX' }
   
   def list_number_of_stores(self):
      api_url_base = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
      response = requests.get(api_url_base,headers=self.API_key())
      return response.json()['number_stores']
   

   def retrieve_stores_data(self):
      list_of_frames = []
      store_number   = self.list_number_of_stores()
      for i in range(store_number):
            api_url_base = f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{_}'
            response = requests.get(api_url_base,headers=self.API_key())
            list_of_frames.append( pd.json_normalize(response.json()))
      return pd.concat(list_of_frames)
   
   def extract_from_s3(self):
      s3_client = boto3.client(3)
      response = s3_client.get_object(Bucket='data-handling-public',key = 'products.csv')
      status  = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
      if status == 200:
         print(f'success!{status}')
         return pd.read_csv(response.get('body'))
      else:
         print(f'Unsuccesful{status}')

    
   def extract_from_s3_link(self):
      url = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'
      response = requests.get(url)
      dic = response.json
      df = pd.DataFrame([])
      for column_name in dic.keys():
         value_list = []
         for i in dic[column_name].keys():
            value_list.append(dic[column_name][_])
            df[column_name] = value_list
      return df
      
      





      
