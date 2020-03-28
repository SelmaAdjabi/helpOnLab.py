from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('/Users/hightech/Documents/M2 MGB/Stage M2/Aide-moi-au-labo/helpMeOnLab/helponlab.ui', self)
        self.vi = self.findChild(QtWidgets.QLineEdit, 'viInput')
        self.vf = self.findChild(QtWidgets.QLineEdit, 'vfInput')
        self.resultLabel = self.findChild(QtWidgets.QLabel, 'resultLabel')
        self.result2Label = self.findChild(QtWidgets.QLabel, 'result2Label')
        self.calculataButton = self.findChild(QtWidgets.QPushButton, 'calculateButton')
        self.calculataButton.clicked.connect(self.calculateFd)


        self.show()

    def calculateFd(self):
        vi = float(self.vi.text())
        vf = float(self.vf.text())

        fd=  1 / (vi / vf)
        vd = vf - vi



        self.resultLabel.setText(str(fd))
        self.result2Label.setText(str(vd))


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()