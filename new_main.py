import sys

# from PySide2.QtWidgets import QApplication

from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog

# 2023-Fev-14
# A organização dos tutoriais é algo confusa.
# Introdućão:
# https://www.pythonguis.com/pyside2/
# O mais direto para uso com Qt Designer é
# https://www.pythonguis.com/tutorials/pyside-first-steps-qt-designer/
# Diálogos:
# https://www.pythonguis.com/tutorials/pyside-dialogs/
# Em seguida, para adicionar diálogos ao app:
# https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/
# Com numpy e Pandas:
# https://www.pythonguis.com/tutorials/pyside-qtableview-modelviews-numpy-pandas/

# Para chamar a ui simplezinha, ui_new_main_ui
# from ui_new_main_ui import Ui_MainWindow

# Para chamar a antiga e complexa interface, ui_main
from ui_maininterface_with_toolbar import Ui_MainInterfaceClass

from ui_languages import Ui_LanguageDlg


class LngDlg(QDialog, Ui_LanguageDlg):
    def __init__(self):
        super(LngDlg, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Vamos customizar!!!")
        # self.okButton.clicked.connect(self.printa())
        self.okButton.clicked.connect(self.printa())
        # serah aqui?
        # Como fazer o connect?
        # https://www.pythonguis.com/tutorials/pyside-dialogs/
        # self.Rejected.connect(self.escolhe()) ERRADO
        # self.cancelButton.connect(self.cancelButton.clicked(), self.escolhe()) ERRADO

    def printa(self):
        print("Chamou")

    def escolhe(self):
        print("Escolhe")


class MainWindow(QMainWindow, Ui_MainInterfaceClass):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # lang_dlg = Ui_LanguageDlg("Interface languages")
        # lang_dlg.okButton.clicked()
        # 2023-Fev-16 Defining custom signal/slots
        # self.actionLanguage.triggered.connect(self.button_clicked)
        self.actionLanguage.triggered.connect(self.actionLanguage_triggered)

    def actionLanguage_triggered(self, s):
        langdlg = LngDlg()
        if langdlg.exec_():
            print("Success!")
        else:
            print("Cancel!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
