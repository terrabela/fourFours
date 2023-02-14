# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogpyqtexemplexuTWZn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogPyqtExemple(object):
    def setupUi(self, DialogPyqtExemple):
        if not DialogPyqtExemple.objectName():
            DialogPyqtExemple.setObjectName(u"DialogPyqtExemple")
        DialogPyqtExemple.resize(217, 158)
        self.verticalLayout_2 = QVBoxLayout(DialogPyqtExemple)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(DialogPyqtExemple)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(DialogPyqtExemple)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lneDecMark = QLineEdit(DialogPyqtExemple)
        self.lneDecMark.setObjectName(u"lneDecMark")

        self.gridLayout.addWidget(self.lneDecMark, 2, 1, 1, 1)

        self.label_3 = QLabel(DialogPyqtExemple)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.lneThousSep = QLineEdit(DialogPyqtExemple)
        self.lneThousSep.setObjectName(u"lneThousSep")

        self.gridLayout.addWidget(self.lneThousSep, 0, 1, 1, 1)

        self.spbDecPlaces = QSpinBox(DialogPyqtExemple)
        self.spbDecPlaces.setObjectName(u"spbDecPlaces")

        self.gridLayout.addWidget(self.spbDecPlaces, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.ckbRedNegat = QCheckBox(DialogPyqtExemple)
        self.ckbRedNegat.setObjectName(u"ckbRedNegat")

        self.verticalLayout.addWidget(self.ckbRedNegat)

        self.btbCloseApply = QDialogButtonBox(DialogPyqtExemple)
        self.btbCloseApply.setObjectName(u"btbCloseApply")
        self.btbCloseApply.setOrientation(Qt.Horizontal)
        self.btbCloseApply.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.btbCloseApply)


        self.verticalLayout_2.addLayout(self.verticalLayout)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.lneThousSep)
        self.label_2.setBuddy(self.lneDecMark)
        self.label_3.setBuddy(self.spbDecPlaces)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(DialogPyqtExemple)
        self.btbCloseApply.accepted.connect(DialogPyqtExemple.accept)
        self.btbCloseApply.rejected.connect(DialogPyqtExemple.reject)

        QMetaObject.connectSlotsByName(DialogPyqtExemple)
    # setupUi

    def retranslateUi(self, DialogPyqtExemple):
        DialogPyqtExemple.setWindowTitle(QCoreApplication.translate("DialogPyqtExemple", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogPyqtExemple", u"&Thousands separator", None))
        self.label_2.setText(QCoreApplication.translate("DialogPyqtExemple", u"Decimal &marker", None))
        self.label_3.setText(QCoreApplication.translate("DialogPyqtExemple", u"&Decimal places", None))
        self.ckbRedNegat.setText(QCoreApplication.translate("DialogPyqtExemple", u"&Red negative numbers", None))
    # retranslateUi

