from PyQt6.QtWidgets import QApplication , QWidget , QLineEdit , QPushButton , QTextEdit , QVBoxLayout
from PyQt6.QtGui import QIcon
import sys


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('HR.png'))
        self.setWindowTitle("Human Resource Application")
    
    
app = QApplication(sys.argv)

# An instance of the Application 
window = MyApp()

#To show the Application 

window.show()
#To Run The Application
app.exec()

 
 
#Implement a Registertaion Page

#Text Fields For Enter The Data For The Employees

#Button For Confriming The Registeration 

#Implement a Main Page With Login Credentials For the Manager And the Admin

#Two Text Fileds For the User_Name and Passwords 

#Button "Login" To Enter The Application 

# Home Page For the Emplpoyees

#Implement Two Buttons For the Check-In and Check Out 

# a Sapce to Welcome the user and show the User if the Late or Not 

# widnows where the Video of the Camera will appear in  