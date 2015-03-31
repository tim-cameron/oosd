__author__ = 'camertp1'
import sys
from PyQt4 import QtCore, QtGui, uic



qtui = "light.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtui)

class DashApplication(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

#THING IN THE MIDDLE


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = DashApplication()
    window.show()
    sys.exit(app.exec_())

