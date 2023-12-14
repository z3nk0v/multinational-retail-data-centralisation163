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

Table of Contents, if the README file is long
A description of the project: what it does, the aim of the project, and what you learned



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
These queries can be found within the 

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
The tasks for milestone 


License information