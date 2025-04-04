from sqlalchemy import create_engine , MetaData ,Table 
from sqlalchemy.orm import declarative_base , sessionmaker
import sqlalchemy as sq
#from datetime import time
from dotenv import load_dotenv
import os


#Load the environment variables from the .env file
load_dotenv()




#The URL For The DataBase 
db_url = os.getenv("Database_Path")

#Connecting to a sqlite database
engine = create_engine(db_url , echo=True)

#Consrtruct an Empty Container to load all the table data inside 
metadata = MetaData()


#load all the Tables Data 
metadata.reflect(bind=engine)

#List all of my Tables 
Employee =  Table("Employee" ,metadata , autoload_with=engine)

Salaries =  Table("Salaries" ,metadata , autoload_with=engine)

Shifts =  Table("Shifts" ,metadata , autoload_with=engine)




#Create a Session 
Session = sessionmaker(bind=engine)

#Create and Object of the Created Session to use 
session = Session()



#Creating a session and Adding New Data To the Data base 
def insert_employee_data(name,phone,Job_title):
    #Create a session 
    with engine.connect() as conn:
        #add Records in the data base 
        add_statement = sq.insert(Employee).values(Name=name, Phone_Number=phone , Job_Title=Job_title)
        conn.execute(add_statement)
        conn.commit()
    

 
