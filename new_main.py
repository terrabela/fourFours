
import sys
from PySide2 import QtWidgets

# 2023-Fev-14
# A organização dos tutoriais é algo confusa.
# O mais direto para uso com Qt Designer é
# https://www.pythonguis.com/tutorials/pyside-first-steps-qt-designer/
# Em seguida, para adicionar diálogos ao app:
# https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/

# 2023-Fev-14 Parei aqui...
# RESOLVER: usar resource compiler para compilar mdi.qrc em Qt5 (mdi_rc.py antigo
# está em Qt4

# Para chamar a ui simplezinha, ui_new_main_ui
# from ui_new_main_ui import Ui_MainWindow

# Para chamar a antiga e complexa interface, ui_main
from ui_maininterface_with_toolbar import Ui_MainInterfaceClass

# class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
class MainWindow(QtWidgets.QMainWindow, Ui_MainInterfaceClass):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()