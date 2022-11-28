import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)

        self.pushButton.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        print("Clicked")
        self.lineEdit.setText("Clicked")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()