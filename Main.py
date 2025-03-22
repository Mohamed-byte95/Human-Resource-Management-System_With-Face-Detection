from Model import engine ,Employee , Salaries ,Shifts
from sqlalchemy.orm import declarative_base , sessionmaker
import sqlalchemy as sq
from datetime import time


#Create Start Time 
#start = time(7,00)
#end = time(21,00)



#Create a Session 
Session = sessionmaker(bind=engine)
#Create and Object of the Created Session to use 
session = Session()



#Creating a session and Adding New Data To the Data base 
def insert_data(name,phone,Job_title):
    #Create a session 
    with engine.connect() as conn:
        #add Records in the data base 
        add_statement = sq.insert(Employee).values(Name=name, Phone_Number=phone , Job_Title=Job_title)
        conn.execute(add_statement)
        conn.commit()
    

 
# Fetch The Data From Users 



#Insert the New Data into the Data base on Click of the Button 