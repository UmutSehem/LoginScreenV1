import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window import MainWindow  
from register import RegisterApp
from forgotpasword import ForgotApp

        

class LoginWindow(QtWidgets.QWidget):
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
        self.paswbuton = QtWidgets.QPushButton(self)
        self.paswbuton.setGeometry(QtCore.QRect(280,400,150,40))
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
        self.paswbuton.setText("Forgot Pass?")



        self.registerbuton = QtWidgets.QPushButton(self)
        self.registerbuton.setGeometry(QtCore.QRect(20,400,150,40))
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
        self.registerbuton.setText("Register?")
        
        self.loginbuton = QtWidgets.QPushButton(self)
        self.loginbuton.setGeometry(QtCore.QRect(145,253,150,40))
        self.loginbuton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.loginbuton.setStyleSheet("QPushButton{\n"
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
        self.loginbuton.setText("Login")


        self.login = QtWidgets.QLineEdit(self)
        self.login.setGeometry(QtCore.QRect(120,150,195,40))        
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.login.setPlaceholderText("  ID:")
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
        





        

        
                       
        










        
        
        
        
        
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("552721.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("(_SHM_)LoginScreenV1")
        self.setMinimumSize(450,450)
        self.setMaximumSize(450,450)
        self.setStyleSheet("background-color: #B0E0E6 ")
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        
        self.loginbuton.clicked.connect(self.loginn)
        self.registerbuton.clicked.connect(self.registerr)
        self.paswbuton.clicked.connect(self.forgotpassword)
        
        self.show()




    def loginn(self):
        ka = self.login.text()
        par = self.password.text()

        self.cursor.execute("SELECT * FROM DATABASE WHERE ID = ? AND PASSWORD = ?", (ka, par))
        data = self.cursor.fetchall()

        if len(data) == 0:
            print("Not Found User!")
            self.login.clear()
            self.password.clear()
        else:
                self.close()
                self.new_window = MainWindow()
                self.new_window.show()


    def registerr(self):
        self.new_window2 = RegisterApp()
        self.new_window2.show()
    
    def forgotpassword(self):
        self.new_window3 = ForgotApp()
        self.new_window3.show()







if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    login_window = LoginWindow()
    sys.exit(app.exec())