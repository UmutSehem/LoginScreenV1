import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

class ForgotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.connect_db()
        self.init_ui()

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
        self.password.setPlaceholderText("  Old Password:")
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

        self.newpassword = QtWidgets.QLineEdit(self)
        self.newpassword.setGeometry(QtCore.QRect(120,250,195,40))
        self.newpassword.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.newpassword.setPlaceholderText("   New Password:")
        self.newpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpassword.setMaxLength(5)
        self.newpassword.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(254,254,254,254);\n"
"    border-radius:15px;\n"
"    color: #FFF;\n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"}\n")

        



        




        self.paswbuton = QtWidgets.QPushButton(self)
        self.paswbuton.setGeometry(QtCore.QRect(145,300,150,40))
        self.paswbuton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.paswbuton.setStyleSheet("QPushButton{\n"
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
        
        self.paswbuton.setText("Reset Pass!")





        

        
                       
        










        
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("552721.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setMinimumSize(450,450)
        self.setMaximumSize(450,450)
        self.setStyleSheet("background-color: #B0E0E6 ")
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.setWindowTitle("(_SHM_)ForgotPassScreen")

        self.paswbuton.clicked.connect(self.forgotpass)
        self.show()
    def forgotpass(self):
        username = self.login.text()
        old_password = self.password.text()
        new_password = self.newpassword.text()
        if not username or not old_password or not new_password:
            print("Please fill in all fields.")
            return
        else:
            self.cursor.execute("SELECT * FROM DATABASE WHERE ID = ? AND PASSWORD = ?", (username,old_password))
            existing_user = self.cursor.fetchone()
            if existing_user:
                if existing_user[0] == username or old_password:  
                    self.cursor.execute("UPDATE DATABASE SET PASSWORD = ? WHERE ID = ?", (new_password, username))
                    self.database_connect.commit()
                    print("Password Reset Successful!")
                    self.close()
                else:
                    print("Old Password Incorrect!")
                    self.password.clear()
                    self.newpassword.clear()
            else:
                print("User not found!")
                self.login.clear()
                self.password.clear()
                self.newpassword.clear()

                