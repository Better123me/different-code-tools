# -- main.py
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5 import uic, QtCore
# from UI_mainWindow import *


def main():
    app = QApplication([])
    firstWindow = mainWindow()

    # dataAnalysisWindow = picShowWindow()
    # dataAnalysisWindow.switch_window.connect(firstWindow.show)

    firstWindow.show()
    app.exec_()


if __name__ == "__main__":
    main()

#################################################################################
# --ui_main_window.py
from PyQt5.QtCore import pyqtSlot
class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        uic.loadUi("mainwindow.ui", self)


    @pyqtSlot()
    def on_makeSure_clicked(self):
        # 关闭当前界面
        self.second_window = chooseWindow()
        self.second_window.show()
        self.close()