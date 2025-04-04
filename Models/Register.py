from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtWidgets import QWidget
from Data_Base  import insert_employee_data
import sys


class Ui_Emp_reg(object):
    def setupUi(self, Emp_reg):
        Emp_reg.setObjectName("Emp_reg")
        Emp_reg.resize(480, 317)
        self.verticalLayout = QtWidgets.QVBoxLayout(Emp_reg)
        self.verticalLayout.setObjectName("verticalLayout")
        
        #The Registeration Label Design
        self.Registertation = QtWidgets.QLabel(parent=Emp_reg)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        self.Registertation.setFont(font)
        self.Registertation.setObjectName("Registertation")
        self.verticalLayout.addWidget(self.Registertation)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        
        #For The Name Section 
        self.Name_l = QtWidgets.QLabel(parent=Emp_reg)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.Name_l.setFont(font)
        self.Name_l.setObjectName("Name_l")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Name_l)
        self.Name_t = QtWidgets.QLineEdit(parent=Emp_reg)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Name_t.setFont(font)
        self.Name_t.setObjectName("Name_t")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Name_t)
        
        #Phone Design UI
        self.Phone_l = QtWidgets.QLabel(parent=Emp_reg)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.Phone_l.setFont(font)
        self.Phone_l.setObjectName("Phone_l")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Phone_l)
        self.Phone_t = QtWidgets.QLineEdit(parent=Emp_reg)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Phone_t.setFont(font)
        self.Phone_t.setObjectName("Phone_t")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Phone_t)
        self.Job_l = QtWidgets.QLabel(parent=Emp_reg)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        
        #Job UI
        self.Job_l.setFont(font)
        self.Job_l.setObjectName("Job_l")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Job_l)
        self.Title_t = QtWidgets.QLineEdit(parent=Emp_reg)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Title_t.setFont(font)
        self.Title_t.setObjectName("Title_t")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Title_t)
        self.Face_l = QtWidgets.QLabel(parent=Emp_reg)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.Face_l.setFont(font)
        self.Face_l.setObjectName("Face_l")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Face_l)
        self.Face_t = QtWidgets.QLineEdit(parent=Emp_reg)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Face_t.setFont(font)
        self.Face_t.setReadOnly(True)
        self.Face_t.setObjectName("Face_t")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Face_t)
        self.Face_rec = QtWidgets.QPushButton(parent=Emp_reg)
        self.Face_rec.setObjectName("Face_rec")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Face_rec)
        self.verticalLayout.addLayout(self.formLayout)
        self.Sec_layout = QtWidgets.QHBoxLayout()
        self.Sec_layout.setObjectName("Sec_layout")
        self.Register = QtWidgets.QPushButton(parent=Emp_reg)
        self.Register.setObjectName("Register")
        self.Sec_layout.addWidget(self.Register)
        self.Cancel = QtWidgets.QPushButton(parent=Emp_reg)
        self.Cancel.setObjectName("Cancel")
        self.Sec_layout.addWidget(self.Cancel)
        self.verticalLayout.addLayout(self.Sec_layout)

        self.retranslateUi(Emp_reg)
        QtCore.QMetaObject.connectSlotsByName(Emp_reg)

    def retranslateUi(self, Emp_reg):
        _translate = QtCore.QCoreApplication.translate
        Emp_reg.setWindowTitle(_translate("Emp_reg", "Register Form"))
        self.Registertation.setText(_translate("Emp_reg", "Registeration"))
        self.Name_l.setText(_translate("Emp_reg", "Name"))
        self.Phone_l.setText(_translate("Emp_reg", "Phone Number"))
        self.Job_l.setText(_translate("Emp_reg", "Job Title"))
        self.Face_l.setText(_translate("Emp_reg", "Face ID"))
        self.Face_rec.setText(_translate("Emp_reg", "Start Facial Recognition"))
        self.Register.setText(_translate("Emp_reg", "Register"))
        self.Cancel.setText(_translate("Emp_reg", "Cancel"))



class Emp_Reg(QWidget,Ui_Emp_reg):
    def __init__(self):
        super().__init__()
        #Setup the user interface 
        self.setupUi(self)
        self.Register.clicked.connect(self.insert_user)
        
       
        
        
    #Insert_Data_Into_DataBase
    def insert_user(self):
            #Retrieve_Data_From_the_Registeration_Form
            name = self.Name_t.text()
            phone = self.Phone_t.text()
            job_title = self.Title_t.text()
            
            #Add new Record to the data base 
            insert_employee_data(name,phone,job_title)
            
            #Clear the data After Registeration
            self.clear()
            print("User Is Registered Successfully!")
            self.Registertation.setText("Regsiteration Success!")
            
    #Clear the data fields after insertion 
    def clear(slef):
        slef.Name_t.clear()
        slef.Phone_t.clear()
        slef.Title_t.clear()
                
            
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Emp_Reg()
    window.show()
    sys.exit(app.exec())
