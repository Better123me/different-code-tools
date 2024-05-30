from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication

class projManager(QMainWindow):
    def __init__(self):
        super(projManager, self).__init__()
        # 导入界面文件
        uic.loadUi("python\pyqt5-utils\ExampleProjs\mainwindow.ui", self)
