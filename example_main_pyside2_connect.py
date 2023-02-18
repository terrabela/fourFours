import sys

from PySide2.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton
from ui_languages import Ui_LanguageDlg


class LngDlg(QDialog, Ui_LanguageDlg):
    def __init__(self):
        super(LngDlg, self).__init__()
        self.setupUi(self)

        # serah aqui?
        # Como fazer o connect?


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # langdlg = Ui_LanguageDlg()
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        langdlg = LngDlg()
        langdlg.exec_()
        # AQUI? como usar ????
        if langdlg.accept():
            print("Accepted!")
        if langdlg.Rejected:
            print("Rejected!")
        print("OK!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
