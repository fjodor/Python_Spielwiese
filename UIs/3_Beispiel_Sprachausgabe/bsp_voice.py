# playsound funktioniert nicht mit modernen Python-Versionen, nicht installierbar
# Stattdessen playsound3 verwenden

from frm_voice import Ui_Form
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from gtts import gTTS
from playsound3 import playsound
import sys, os

class MainForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MainForm,self).__init__()
        self.setupUi(self)

    def btnRead_click(self):
        output = self.txtText.toPlainText()
        language = 'de'
        if self.rbEnglish.isChecked():
           language = 'en'
        voice_obj = gTTS(text=output, lang=language, slow=False)
        voice_obj.save("output.mp3")
        playsound("output.mp3")
        os.remove("output.mp3")

    def btnClose_click(self):
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec())