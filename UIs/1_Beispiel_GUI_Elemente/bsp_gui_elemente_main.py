from bsp_gui_elemente_frmMain import Ui_frmMain
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox
import sys

class Bsp_Form(QtWidgets.QWidget,Ui_frmMain):
    def __init__(self):
        super(Bsp_Form,self).__init__()
        self.setupUi(self)

    def btnClose_click(self):
        app.quit()

    def btnShow_click(self):
        text = self.lineEdit.text()
        QMessageBox.information(self, 'Information', text)

    def rbGreen_click(self):
        self.lblColor.setStyleSheet("background-color: rgb(0, 170, 0);")

    def rbRed_click(self):
        self.lblColor.setStyleSheet("background-color: rgb(255, 0, 0);")

    def rbBlue_click(self):
        self.lblColor.setStyleSheet("background-color: rgb(0, 0, 255);")

    def cbText1_click(self):
        if (self.cbText1.isChecked()):
            self.lblText1.setVisible(True)
        else:
            self.lblText1.setVisible(False)

    def cbText2_click(self):
        if (self.cbText2.isChecked()):
            self.lblText2.setVisible(True)
        else:
            self.lblText2.setVisible(False)

    def hSlider_moved(self):
        self.lblSliderValue.setText(str(self.hSlider.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Bsp_Form()
    form.show()
    sys.exit(app.exec())