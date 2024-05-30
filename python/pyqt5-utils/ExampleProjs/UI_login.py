from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from UI_mainWindow import *

class loginWindow(QMainWindow):
    def __init__(self):
        super(loginWindow, self).__init__()
        # 导入界面文件
        uic.loadUi(r"python\pyqt5-utils\ExampleProjs\form.ui", self)


    @pyqtSlot()
    def on_loginPushBtm_clicked(self):
        usrName = self.usrName.text()
        usrPassword = self.usrPassword.text()
        QMessageBox.information(None, "trying", f"输入的用户名为:{usrName}; 密码为：{usrPassword}")

        # 需要把主界面作为登录界面的一个成员变量，或者是在main文件当中进行调整窗口事件的操作，此处选择了第一种实现
        self.mainWindow = projManager()
        self.mainWindow.show()

        # 关闭登陆界面
        self.close()