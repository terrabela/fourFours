import sys

# from PySide2.QtWidgets import QApplication

from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog

# 2023-Fev-14
# A organização dos tutoriais é algo confusa.
# O mais direto para uso com Qt Designer é
# https://www.pythonguis.com/tutorials/pyside-first-steps-qt-designer/
# Em seguida, para adicionar diálogos ao app:
# https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/

# Para chamar a ui simplezinha, ui_new_main_ui
# from ui_new_main_ui import Ui_MainWindow

# Para chamar a antiga e complexa interface, ui_main
from ui_maininterface_with_toolbar import Ui_MainInterfaceClass

from ui_languages import Ui_LanguageDlg


class MainWindow(QMainWindow, Ui_MainInterfaceClass):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # lang_dlg = Ui_LanguageDlg("Interface languages")
        # lang_dlg.okButton.clicked()
        # 2023-Fev-16 Defining custom signal/slots
        # self.actionLanguage.triggered.connect(self.button_clicked)
        self.actionLanguage.triggered.connect(self.actionLanguage_triggered)

    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        button = dlg.exec_()

        if button == QMessageBox.Ok:
            print("OK!")

    def actionLanguage_triggered(self, s):
        # lang_dlg = Ui_LanguageDlg("Interface languages")
        lang_dlg = Ui_LanguageDlg()
        # lang_dlg. okButton.clicked()
        lang_dlg.setupUi(QDialog)
        # se_ok = lang_dlg.okButton.clicked()
        # if se_ok == Ui_LanguageDlg

        # dlg = QMessageBox(self)
        # dlg.setWindowTitle("I have a question!")
        # dlg.setText("This is a simple dialog")
        # button = dlg.exec_()

        # if button == QMessageBox.Ok:
        #     print("OK!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
