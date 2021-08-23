import _gui



from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
import sys


class ExampleApp(QtWidgets.QMainWindow, _gui.Ui_Dialog):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
