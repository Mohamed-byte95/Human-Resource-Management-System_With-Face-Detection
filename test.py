from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QCheckBox,
    QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout
)
from PyQt6.QtGui import QFont, QPalette, QColor
from PyQt6.QtCore import Qt
import sys

class RegisterForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interior Register Form")
        self.setFixedSize(800, 500)
        self.setStyleSheet("background-color: #f5f5f5;")

        # Main Layout
        main_layout = QHBoxLayout(self)

        # Left Section (Welcome)
        left_section = QWidget()
        left_layout = QVBoxLayout(left_section)
        left_section.setStyleSheet("background-color: #222; color: white; padding: 40px;")

        welcome_label = QLabel("Welcome !")
        welcome_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        desc_label = QLabel("Lorem Ipsum Dolor Sit Amet, Nulla Consectetur Adipiscing Elit Sed.")
        desc_label.setFont(QFont("Arial", 12))
        desc_label.setWordWrap(True)

        left_layout.addWidget(welcome_label)
        left_layout.addWidget(desc_label)
        left_layout.addStretch()  # Push content to the top

        # Right Section (Form)
        right_section = QWidget()
        right_layout = QVBoxLayout(right_section)
        right_section.setStyleSheet("background-color: black; padding: 40px; border-radius: 10px;")

        form_layout = QFormLayout()

        first_name = QLineEdit()
        last_name = QLineEdit()
        email = QLineEdit()
        password = QLineEdit()
        confirm_password = QLineEdit()

        password.setEchoMode(QLineEdit.EchoMode.Password)
        confirm_password.setEchoMode(QLineEdit.EchoMode.Password)

        first_name.setPlaceholderText("First Name")
        last_name.setPlaceholderText("Last Name")
        email.setPlaceholderText("Email")
        password.setPlaceholderText("Password")
        confirm_password.setPlaceholderText("Confirm Password")

        form_layout.addRow(" ", first_name)
        form_layout.addRow(" ", last_name)
        form_layout.addRow(" ", email)
        form_layout.addRow(" ", password)
        form_layout.addRow(" ", confirm_password)

        check_updates = QCheckBox("Send Me Latest Updates")
        create_account_btn = QPushButton("CREATE ACCOUNT")
        create_account_btn.setStyleSheet("background-color: #00c853; color: Black; padding: 10px; font-size: 14px;")

        right_layout.addWidget(QLabel("<h2>Create An Account</h2>"), alignment=Qt.AlignmentFlag.AlignCenter)
        right_layout.addLayout(form_layout)
        right_layout.addWidget(check_updates)
        right_layout.addWidget(create_account_btn)

        # Add sections to main layout
        main_layout.addWidget(left_section, 1)
        main_layout.addWidget(right_section, 2)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterForm()
    window.show()
    sys.exit(app.exec())
#========================================================================

from sqlalchemy import create_engine , MetaData ,Table 
from sqlalchemy.orm import declarative_base , sessionmaker
import sqlalchemy as sq
#from datetime import time
from dotenv import load_dotenv
import os


#Load the environment variables from the .env file
load_dotenv()




#The URL For The DataBase 
db_url = os.getenv("db_url")

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
    