import sys,os
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLineEdit,QFormLayout,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import pyqtSignal

class Countrypage(QWidget):
    def __init__(self):
        super().__init__()
        self.btn_close = QPushButton("Close")
        self.btn_new = QPushButton("New")
        self.tb_country = QLineEdit()
        self.tb_continent = QLineEdit()
        self.form_layout = QFormLayout()
        self.form_layout.addRow("Country", self.tb_country)
        self.form_layout.addRow("Continent", self.tb_continent)
        self.form_layout.addRow("", self.btn_close)
        self.form_layout.addRow("", self.btn_new)
        self.setLayout(self.form_layout)

    def update_fields(self, other):
        if isinstance(other, Countrypage):
            self.tb_country.setText(other.tb_country.text())
            self.tb_continent.setText(other.tb_continent.text())
        else:
            raise TypeError('invalid page type')