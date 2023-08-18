import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

class RegisterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.connect_db()

    def connect_db(self):
        self.database_connect = sqlite3.connect("DATABASE.db")
        self.cursor = self.database_connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS DATABASE (ID TEXT, PASSWORD TEXT)")
        self.database_connect.commit()
    def init_ui(self):

        self.login = QtWidgets.QLineEdit(self)
        self.login.setGeometry(QtCore.QRect(120,150,195,40))
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.login.setPlaceholderText("  ID:")
        self.login.setMaxLength(15)
        self.login.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(254,254,254,254);\n"
"    border-radius:15px;\n"
"    color: #FFF;\n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"    border:2px solid rgb(48,50,62)\n"
"}\n"
"QLineEdit:focus{\n"
"    border:2px solid rgb(0, 0, 0, 0)\n"
"}")

        self.password = QtWidgets.QLineEdit(self)
        self.password.setGeometry(QtCore.QRect(120,200,195,40))
        self.password.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.password.setPlaceholderText("  Password:")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setMaxLength(5)
        self.password.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(254,254,254,254);\n"
"    border-radius:15px;\n"
"    color: #FFF;\n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"    border:2px solid rgb(48,50,62)\n"
"}\n"
"QLineEdit:focus{\n"
"    border:2px solid rgb(0, 0, 0, 0)\n"
"}")

        self.confpassword = QtWidgets.QLineEdit(self)
        self.confpassword.setGeometry(QtCore.QRect(120,250,195,40))
        self.confpassword.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.confpassword.setPlaceholderText("   Confirm Password:")
        self.confpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confpassword.setMaxLength(5)
        self.confpassword.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(254,254,254,254);\n"
"    border-radius:15px;\n"
"    color: #FFF;\n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"}\n")

        



        




        self.registerbuton = QtWidgets.QPushButton(self)
        self.registerbuton.setGeometry(QtCore.QRect(145,300,150,40))
        self.registerbuton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.registerbuton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(251, 255, 254);\n"
"    font: 75 19pt \"Agency FB\";\n"
"   border-radius:15px;\n"
"   background-color: rgb(0, 0, 0);\n"
"   \n"
"    color: rgb(254, 254, 254);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(37, 37, 38);\n"
" \n"
"}")
        
        self.registerbuton.setText("Register")





        

        
                       
        










        
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("552721.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setMinimumSize(450,450)
        self.setMaximumSize(450,450)
        self.setStyleSheet("background-color: #B0E0E6 ")
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.setWindowTitle("(_SHM_)RegisterScreen")

        self.registerbuton.clicked.connect(self.registerr)
        self.show()

    def registerr(self):
        ID = self.login.text()
        PASSWORD = self.password.text()
        conf_password = self.confpassword.text()

        if not ID or not PASSWORD or not conf_password:
            print("Please fill in all fields.")
            return
        else:
            self.cursor.execute("SELECT * FROM DATABASE WHERE ID = ?", (ID,))
            existing_user = self.cursor.fetchone()
            if existing_user:
                self.login.clear()
                print("Such a User Already Exists!\nPlease Try Again!")
            elif PASSWORD == conf_password:
                self.cursor.execute("INSERT INTO DATABASE (ID, PASSWORD) VALUES (?, ?)", (ID, PASSWORD))
                self.database_connect.commit()
                print("Registration Success!")
                self.close()
            else:
                print("Passwords Do Not Match!")
                self.login.clear()
                self.password.clear()
                self.confpassword.clear()

