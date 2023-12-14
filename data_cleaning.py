import pandas as pd
import numpy as np
import re
from pandasgui  import show

pd.set_option('display.max_columns', None)
# df.info()

class DataCleaning:
    def clean_invalid_date(self,df: pd.DataFrame,column_name):
        df[column_name] = pd.to_datetime(df[column_name], format='%Y-%m-%d', errors='ignore')
        df.dropna(subset = column_name,how='any',inplace= True)
        print(type(df))
        print(df.columns)
        return df
    
    def clean_user_data(self,df):
        df = self.clean_invalid_date(df,'date_of_birth')
        df = self.clean_invalid_date(df,'join_date')        
        df.dropna(how='any',inplace=True)
        df.drop(columns='index',inplace=True)
        df = df.loc[~(df['first_name'] == 'NULL')]
        df = df.loc[~(df['first_name'].str.contains('\d', regex=True, case=True))]
        return df
    
    
    def clean_card_data(self,df):
        df['card_number'] = df['card_number'].apply(str)
        df['card_number'] = df['card_number'].str.replace('?','')
        df = self.clean_invalid_date(df,'date_payment_confirmed')  
        df.drop(columns='Unnamed: 0',inplace=True)
        df.dropna(how='any',inplace= True)
        return df

    def clean_date_time(self,df):
        df['month']         =  pd.to_numeric( df['month'],errors='coerce', downcast="integer")
        df['year']          =  pd.to_numeric( df['year'], errors='coerce', downcast="integer")
        df['day']           =  pd.to_numeric( df['day'], errors='coerce', downcast="integer")
        df['timestamp']     =  pd.to_datetime(df['timestamp'], format='%H:%M:%S', errors='coerce')
        df.dropna(how='any',inplace= True)
        df.reset_index(inplace=True)       
        return df

    def clean_products_weights(self,df):
        df = self.clean_invalid_date(df,'date_added')
        df.dropna(how='any',inplace= True)
        return df 
    
    def convert_product_weights(self,df,column_name):
        df[column_name] = df[column_name].apply[self.get_grams]
        return df
    
    def clean_products_data(self,df):
        df = self.clean_invalid_date(df,'date_added')
        df.dropna(how='any',inplace=True)
        return df


    def clean_orders_data(self,df):
        df.drop(columns='1',inplace=True)
        df.drop(columns='first_name',inplace=True)
        df.drop(columns='last_name',inplace=True)
        df.drop(columns='level_0',inplace=True)
        df['card_number'] = df['card_number'].apply(self.isDigits)
        df.dropna(how='any',inplace= True)
        return df
    
    def isDigits(self,num):
        return str(num) if str(num).isdigit() else np.nan


    def clean_store_data(self,df):
        df.drop(columns='lat',inplace=True)
        df =  self.clean_invalid_date(df,'opening_date')                     
        df['staff_numbers'] =  pd.to_numeric( df['staff_numbers'].apply(self.remove_char_from_string),errors='coerce', downcast="integer") 
        df.dropna(subset = ['staff_numbers'],how='any',inplace= True)
        return df

    def get_grams(self,value):
        value = str(value)
        value = value.replace('.',)

    def remove_char_from_string(self,value):
        return re.sub(r'\D', '',value)
