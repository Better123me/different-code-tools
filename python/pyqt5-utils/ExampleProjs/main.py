from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5 import uic, QtCore

# 导入登录界面类的声明
from UI_login import *

# 程序运行主循环事件
def main():
    app = QApplication([])

    # 新建一个页面的实例
    firstWindow = loginWindow()

    # 展示
    firstWindow.show()
    app.exec_()



if "__main__" == __name__:
    main()