# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(282, 185)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_19 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy)
        self.widget_19.setObjectName("widget_19")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_19)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.widget_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(74, 74, 74);\n"
"color: rgb(228, 228, 228);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.display = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display.sizePolicy().hasHeightForWidth())
        self.display.setSizePolicy(sizePolicy)
        self.display.setMinimumSize(QtCore.QSize(0, 48))
        self.display.setMaximumSize(QtCore.QSize(16777215, 48))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono PS")
        font.setPointSize(20)
        self.display.setFont(font)
        self.display.setAutoFillBackground(False)
        self.display.setFrame(False)
        self.display.setObjectName("display")
        self.verticalLayout_4.addWidget(self.display)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.widget_19)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.basic = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basic.sizePolicy().hasHeightForWidth())
        self.basic.setSizePolicy(sizePolicy)
        self.basic.setObjectName("basic")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.basic)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.basic_buttons_layout = QtWidgets.QGridLayout()
        self.basic_buttons_layout.setContentsMargins(3, 0, 3, 3)
        self.basic_buttons_layout.setSpacing(0)
        self.basic_buttons_layout.setObjectName("basic_buttons_layout")
        self.verticalLayout.addLayout(self.basic_buttons_layout)
        self.stackedWidget.addWidget(self.basic)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 282, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuConvert = QtWidgets.QMenu(self.menubar)
        self.menuConvert.setObjectName("menuConvert")
        MainWindow.setMenuBar(self.menubar)
        self.actionClose_Calculator_Window = QtWidgets.QAction(MainWindow)
        self.actionClose_Calculator_Window.setObjectName("actionClose_Calculator_Window")
        self.actionSave_Tape_As = QtWidgets.QAction(MainWindow)
        self.actionSave_Tape_As.setObjectName("actionSave_Tape_As")
        self.actionPage_Setup = QtWidgets.QAction(MainWindow)
        self.actionPage_Setup.setObjectName("actionPage_Setup")
        self.actionPrint_Tape = QtWidgets.QAction(MainWindow)
        self.actionPrint_Tape.setObjectName("actionPrint_Tape")
        self.actionView_Basic = QtWidgets.QAction(MainWindow)
        self.actionView_Basic.setObjectName("actionView_Basic")
        self.actionView_Scientific = QtWidgets.QAction(MainWindow)
        self.actionView_Scientific.setObjectName("actionView_Scientific")
        self.actionView_Programation = QtWidgets.QAction(MainWindow)
        self.actionView_Programation.setObjectName("actionView_Programation")
        self.actionView_Tape = QtWidgets.QAction(MainWindow)
        self.actionView_Tape.setObjectName("actionView_Tape")
        self.actionView_RPN = QtWidgets.QAction(MainWindow)
        self.actionView_RPN.setObjectName("actionView_RPN")
        self.actionView_Precision = QtWidgets.QAction(MainWindow)
        self.actionView_Precision.setObjectName("actionView_Precision")
        self.actionConvert_Recent_Convertions = QtWidgets.QAction(MainWindow)
        self.actionConvert_Recent_Convertions.setEnabled(False)
        self.actionConvert_Recent_Convertions.setObjectName("actionConvert_Recent_Convertions")
        self.actionConvert_Area = QtWidgets.QAction(MainWindow)
        self.actionConvert_Area.setEnabled(False)
        self.actionConvert_Area.setObjectName("actionConvert_Area")
        self.actionConvert_Currency = QtWidgets.QAction(MainWindow)
        self.actionConvert_Currency.setEnabled(False)
        self.actionConvert_Currency.setObjectName("actionConvert_Currency")
        self.actionConvert_Energy_or_Work = QtWidgets.QAction(MainWindow)
        self.actionConvert_Energy_or_Work.setEnabled(False)
        self.actionConvert_Energy_or_Work.setObjectName("actionConvert_Energy_or_Work")
        self.actionConvert_Temperature = QtWidgets.QAction(MainWindow)
        self.actionConvert_Temperature.setEnabled(False)
        self.actionConvert_Temperature.setObjectName("actionConvert_Temperature")
        self.actionConvert_Length = QtWidgets.QAction(MainWindow)
        self.actionConvert_Length.setEnabled(False)
        self.actionConvert_Length.setObjectName("actionConvert_Length")
        self.actionConvert_Weigths_and_Masses = QtWidgets.QAction(MainWindow)
        self.actionConvert_Weigths_and_Masses.setEnabled(False)
        self.actionConvert_Weigths_and_Masses.setObjectName("actionConvert_Weigths_and_Masses")
        self.actionConvert_Speed = QtWidgets.QAction(MainWindow)
        self.actionConvert_Speed.setEnabled(False)
        self.actionConvert_Speed.setObjectName("actionConvert_Speed")
        self.actionConvert_Pressure = QtWidgets.QAction(MainWindow)
        self.actionConvert_Pressure.setEnabled(False)
        self.actionConvert_Pressure.setObjectName("actionConvert_Pressure")
        self.actionConvert_Power = QtWidgets.QAction(MainWindow)
        self.actionConvert_Power.setEnabled(False)
        self.actionConvert_Power.setObjectName("actionConvert_Power")
        self.actionConvert_Volume = QtWidgets.QAction(MainWindow)
        self.actionConvert_Volume.setEnabled(False)
        self.actionConvert_Volume.setObjectName("actionConvert_Volume")
        self.actionConvert_Update_currencies_rate = QtWidgets.QAction(MainWindow)
        self.actionConvert_Update_currencies_rate.setEnabled(False)
        self.actionConvert_Update_currencies_rate.setObjectName("actionConvert_Update_currencies_rate")
        self.actionConvert_Last_Update = QtWidgets.QAction(MainWindow)
        self.actionConvert_Last_Update.setEnabled(False)
        self.actionConvert_Last_Update.setObjectName("actionConvert_Last_Update")
        self.ActionMenuHelpAbout = QtWidgets.QAction(MainWindow)
        self.ActionMenuHelpAbout.setObjectName("ActionMenuHelpAbout")
        self.menuFile.addAction(self.actionClose_Calculator_Window)
        self.menuFile.addAction(self.actionSave_Tape_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPage_Setup)
        self.menuFile.addAction(self.actionPrint_Tape)
        self.menuView.addAction(self.actionView_Basic)
        self.menuView.addAction(self.actionView_Scientific)
        self.menuView.addAction(self.actionView_Programation)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionView_Tape)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionView_RPN)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionView_Precision)
        self.menuHelp.addAction(self.ActionMenuHelpAbout)
        self.menuConvert.addAction(self.actionConvert_Recent_Convertions)
        self.menuConvert.addSeparator()
        self.menuConvert.addAction(self.actionConvert_Area)
        self.menuConvert.addAction(self.actionConvert_Currency)
        self.menuConvert.addAction(self.actionConvert_Energy_or_Work)
        self.menuConvert.addAction(self.actionConvert_Temperature)
        self.menuConvert.addAction(self.actionConvert_Length)
        self.menuConvert.addAction(self.actionConvert_Weigths_and_Masses)
        self.menuConvert.addAction(self.actionConvert_Speed)
        self.menuConvert.addAction(self.actionConvert_Pressure)
        self.menuConvert.addAction(self.actionConvert_Power)
        self.menuConvert.addAction(self.actionConvert_Volume)
        self.menuConvert.addSeparator()
        self.menuConvert.addAction(self.actionConvert_Update_currencies_rate)
        self.menuConvert.addAction(self.actionConvert_Last_Update)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuConvert.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuConvert.setTitle(_translate("MainWindow", "Convert"))
        self.actionClose_Calculator_Window.setText(_translate("MainWindow", "Close calculator Window"))
        self.actionClose_Calculator_Window.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionSave_Tape_As.setText(_translate("MainWindow", "Save Tape As..."))
        self.actionSave_Tape_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionPage_Setup.setText(_translate("MainWindow", "Page Setup..."))
        self.actionPage_Setup.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.actionPrint_Tape.setText(_translate("MainWindow", "Print Tape..."))
        self.actionPrint_Tape.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionView_Basic.setText(_translate("MainWindow", "Basic"))
        self.actionView_Basic.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionView_Scientific.setText(_translate("MainWindow", "Scientific"))
        self.actionView_Scientific.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionView_Programation.setText(_translate("MainWindow", "Programmer"))
        self.actionView_Programation.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionView_Tape.setText(_translate("MainWindow", "Show Paper Tape"))
        self.actionView_RPN.setText(_translate("MainWindow", "RPN"))
        self.actionView_Precision.setText(_translate("MainWindow", "Precision"))
        self.actionConvert_Recent_Convertions.setText(_translate("MainWindow", "Recent Conversions"))
        self.actionConvert_Area.setText(_translate("MainWindow", "Area..."))
        self.actionConvert_Currency.setText(_translate("MainWindow", "Currency..."))
        self.actionConvert_Energy_or_Work.setText(_translate("MainWindow", "Energy or Work..."))
        self.actionConvert_Temperature.setText(_translate("MainWindow", "Temperature..."))
        self.actionConvert_Temperature.setToolTip(_translate("MainWindow", "Temperature"))
        self.actionConvert_Length.setText(_translate("MainWindow", "Length..."))
        self.actionConvert_Weigths_and_Masses.setText(_translate("MainWindow", "Weigths and Masses..."))
        self.actionConvert_Speed.setText(_translate("MainWindow", "Speed..."))
        self.actionConvert_Pressure.setText(_translate("MainWindow", "Pressure..."))
        self.actionConvert_Power.setText(_translate("MainWindow", "Power..."))
        self.actionConvert_Volume.setText(_translate("MainWindow", "Volume..."))
        self.actionConvert_Update_currencies_rate.setText(_translate("MainWindow", "Update Currency Exchanges Rates..."))
        self.actionConvert_Last_Update.setText(_translate("MainWindow", "Last Update:"))
        self.ActionMenuHelpAbout.setText(_translate("MainWindow", "About"))
