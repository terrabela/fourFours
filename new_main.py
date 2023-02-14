
import sys
from PySide2 import QtWidgets

# 2023-Fev-14
# A organização dos tutoriais é algo confusa.
# O mais direto para uso com Qt Designer é
# https://www.pythonguis.com/tutorials/pyside-first-steps-qt-designer/
# Em seguida, para adicionar diálogos ao app:
# https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/

# 2023-Fev-14 Parei aqui...

# from MainWindow import Ui_MainWindow
from ui_new_main_ui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()