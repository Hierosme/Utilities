# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './dialog_paper_tape.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PaperTape(object):
    def setupUi(self, PaperTape):
        PaperTape.setObjectName("PaperTape")
        PaperTape.resize(244, 251)
        self.gridLayout = QtWidgets.QGridLayout(PaperTape)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_clear = QtWidgets.QPushButton(PaperTape)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 1, 1, 1, 1)
        self.pushButton_recalculate_totals = QtWidgets.QPushButton(PaperTape)
        self.pushButton_recalculate_totals.setObjectName("pushButton_recalculate_totals")
        self.gridLayout.addWidget(self.pushButton_recalculate_totals, 1, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(PaperTape)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 2)

        self.retranslateUi(PaperTape)
        self.pushButton_clear.clicked.connect(self.plainTextEdit.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PaperTape)

    def retranslateUi(self, PaperTape):
        _translate = QtCore.QCoreApplication.translate
        PaperTape.setWindowTitle(_translate("PaperTape", "Form"))
        self.pushButton_clear.setText(_translate("PaperTape", "Clear"))
        self.pushButton_recalculate_totals.setText(_translate("PaperTape", "Recalculate Totals"))