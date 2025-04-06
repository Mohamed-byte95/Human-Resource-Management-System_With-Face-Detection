#Create the Database Connection 
import sqlalchemy as sa
import sqlalchemy.orm as orm
import os
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("db_url")
#print("Database URL:", db_url)

#create engine
engine = sa.create_engine(db_url,echo=True)

session = orm.sessionmaker(bind=engine)

Base = orm.declarative_base()


 
