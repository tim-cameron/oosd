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
        self.btnSwitch.clicked.connect(self.clicked)

    def clicked(self):
        palette = self.palette()
        QtGui.QSound("switch.wav").play()
        if self.rdoOn.isChecked():
            self.rdoOff.setChecked(True)
            palette.setColor(self.backgroundRole(),QtGui.QColor(0,0,0) )
        else:
            self.rdoOn.setChecked(True)
            palette.setColor(self.backgroundRole(),QtGui.QColor(255,255,255) )
        self.setPalette(palette)


#THING IN THE MIDDLE


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = DashApplication()
    window.show()
    sys.exit(app.exec_())

