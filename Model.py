from sqlalchemy import create_engine , MetaData ,Table

#The URL For The DataBase 
db_url = "sqlite:///HR_System.db"

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

