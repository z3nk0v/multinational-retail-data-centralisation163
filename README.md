# multinational-retail-data-centralisation163

Table of Contents


        Explanation of the project


        The Milestones of the project
            Milestone 1
            Milestone 2
            Milestone 3
            Milestone 4
        Installation instructions
        Usage instructions
        File structure of the project
        Project Utils
        License Information




Explanation of the project

        You work for a multinational company that sells various goods across the globe. Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team. In an effort to become more data-driven, your organisation would like to make its sales data accessible from one centralised location. Your first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data. You will then query the database to get up-to-date metrics for the business.

The project is broken down into 4 milestones each with its own tasks to complete.

        Milestone 1: Set up the environment
                Here we set up a Github repository in order to track changes to our code.
        
        Milestone 2: Extract and Clean the data from the data sources.
                Here we are extracting data from multiple sources, cleaning it then storing it onto our postgresql server.
        
        Milestone 3: Create the Database Schema
                I developed the star-based schema of the database ensuring the data columns were of the correct type
                The changes made to each tables can be seen within the Database_Schema sql file
                
        Milestone 4: Querying the Data
                Here I used SQL queries in order to find out specific business information such as how many stores were in each location, which months were most successful etc 
                These queries were the following queries answered and can be found under 'business Queries'
                
                        How many stores does the business have and in which countries?
                
                        Which locations currently have the most stores?
                        
                        Which months produce the most sales typically?
                        
                        How many sales are coming from online?
                        
                        What percentage of sales come through each type of store?
                        
                        Which month in each year produced the most sales?
                        
                        What is our staff headcount?
                        
                        Which German store type is selling the most?
                        
                        How quickly is the company making sales?

Installation instructions
        In order for this project to run the following modules require to be installed:
        pandas
        sqlalchemy
        requests
        tabula-py
        python-dotenv
        PyYAML
        boto3
        re
        pandas

Usage instructions
        Data extraction. In "data_extraction.py" we store methods responsible for the upload of data into pandas data frame from different sources.
        
        Data cleaning. In "data_cleaning.py" we develop the class DataCleaning that clean different tables, which we uploaded in "data_extraction.py".
        
        Data Utils. In "database_utils.py" We write DatabaseConnector class "database_utils.py", which initiates the database engine based on credentials provided in ".yaml" file.
        
        "main.py" contains methods, which allow uploading data directly into the local database.

File structure of the project

DATA Sources 

        AWS RDS Database
        Source Data: Historical sales and user data stored in an AWS RDS database.
        Extraction Methods: Used methods in data_extraction and database_utils classes.
        Tables: orders_table, dim_users

        AWS S3 Bucket
        Source Data: Products data saved as a CSV file in an AWS S3 bucket.
        Extraction Method: Leveraged boto3 for downloading and extraction. This is then turned into a Pandas DataFrame.
        Tables: dim_products, dim_date_times

        AWS Link (PDF)
        Source Data: PDF file stored in an AWS S3 bucket.
        Extraction Method: Utilized tabula to read tables from the PDF and convert them into a pandas DataFrame.
        Tables: dim_card_details

        RESTful API
        Source Data: Store data retrieved from an API endpoint.
        Extraction Method: HTTP GET requests to the API, then converting to JSON
        Tables: dim_store_details

License information
