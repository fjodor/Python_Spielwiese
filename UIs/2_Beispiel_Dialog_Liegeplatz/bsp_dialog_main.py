from bsp_dialog import Ui_frmLiegeplatzerfasssung
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
import sys

class MainForm(QtWidgets.QWidget,Ui_frmLiegeplatzerfasssung):
    def __init__(self):
        super(MainForm,self).__init__()
        self.setupUi(self)
    def btnSave_click(self):
        pass
    def btnNew_click(self):
        pass
    def btnClose_click(self):
        pass
    def cbVermietet_click(self):
        pass
    def cbBelegt_click(self):
        pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec())