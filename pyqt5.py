import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
os.system("cls")
class Checkbox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(30,50,1600,1400)
        self.setWindowTitle("Qcheckboxni organamiz ")
        self.setWindowIcon(QIcon("C:\\Users\\Asus Vivobook\\Pictures\\Screenshots\\paynet_1 jpg"))

        self.ln1=QLineEdit(self)
        self.ln1.setGeometry(100,340,200,50)
        self.ln1.setFont(QFont("Consolas",22))
        self.ln1.setStyleSheet("color: red; background-color: black;")


        self.qb=QCheckBox(self)
        self.qb.setGeometry(100,500,120,40)
        self.qb.setFont(QFont("Calibri",22))
        self.qb.setText("😎")
        self.qb.clicked.connect(self.password)
    def password(self):
        if self.qb.text()=="😎":
            self.qb.setText("😐")
            self.ln1.setEchoMode(QLineEdit.Password)
        elif self.qb.text()=="😐":
            self.qb.setText("😎")
            self.ln1.setEchoMode(QLineEdit.Normal)
        
app=QApplication(sys.argv)
mn=Checkbox()
mn.show()
sys.exit(app.exec_())