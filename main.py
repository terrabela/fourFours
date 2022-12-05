import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()

        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.addAction("Se&ttings...")
        file.triggered[QAction].connect(self.windowaction)
        self.setWindowTitle("MDI demo")
        print('Construiu janela principal.')

    def windowaction(self, q):
        print("triggered")

        if q.text() == "New":
            MainWindow.count = MainWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("subwindow" + str(MainWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()

        if q.text() == "cascade":
            self.mdi.cascadeSubWindows()

        if q.text() == "Tiled":
            self.mdi.tileSubWindows()


def main():
    # Estah funcionando; ativar depois.
    # app = QApplication(sys.argv)
    # ex = MainWindow()
    # ex.show()
    # sys.exit(app.exec_())

    # 1st sympy ex
    import sympy
    print(sympy.sqrt(5040))
    #
    # 2nd sympy ex
    from sympy import symbols
    x, y = symbols('x y')
    expr = x + 2 * y
    print(expr)
    print(expr-x)
    #
    # 3rd sympy ex
    from sympy import expand, factor
    print(expand(x*expr))
    print(factor(expand(x*expr)))
    #
    # Dealing with prime numbers
    from sympy import prime, factorint, pprint
    print(prime(1000))
    print(prime(1000000))
    print(prime(1300000))
    print(factorint(5040))
    print(factorint(152235446985089743026345634545344))
    print(943856703456356*23452345246)
    print(factorint(22135653272209902405083576))
    pprint(factorint(5040, visual=True))


if __name__ == '__main__':
    main()
