# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HumanResource(object):
    def setupUi(self, HumanResource):
        HumanResource.setObjectName("HumanResource")
        HumanResource.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        HumanResource.resize(848, 689)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        font.setPointSize(9)
        HumanResource.setFont(font)
        self.pushButton = QtWidgets.QPushButton(parent=HumanResource)
        self.pushButton.setGeometry(QtCore.QRect(522, 397, 211, 61))
        self.pushButton.setObjectName("Check-In")
        self.pushButton_2 = QtWidgets.QPushButton(parent=HumanResource)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 397, 211, 61))
        self.pushButton_2.setObjectName("Check_Out")

        self.retranslateUi(HumanResource)
        QtCore.QMetaObject.connectSlotsByName(HumanResource)

    def retranslateUi(self, HumanResource):
        _translate = QtCore.QCoreApplication.translate
        HumanResource.setWindowTitle(_translate("HumanResource", "Human Resource Application"))
        self.pushButton.setText(_translate("HumanResource", "Check-In"))
        self.pushButton_2.setText(_translate("HumanResource", "Check-Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HumanResource = QtWidgets.QWidget()
    ui = Ui_HumanResource()
    ui.setupUi(HumanResource)
    HumanResource.show()
    sys.exit(app.exec())
