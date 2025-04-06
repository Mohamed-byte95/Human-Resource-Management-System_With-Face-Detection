#Entry Point that starts the application
import sys
import os 
from models.database import session, engine, Base
from models.employee_model import Employee

#Create All the Tables in the Database
Base.metadata.create_all(engine)




