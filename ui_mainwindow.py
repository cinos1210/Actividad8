# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1359, 630)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(30, 0, 1251, 561))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")
        self.salida.setGeometry(QRect(230, 10, 321, 231))
        self.Mostrar_pushButton = QPushButton(self.tab)
        self.Mostrar_pushButton.setObjectName(u"Mostrar_pushButton")
        self.Mostrar_pushButton.setGeometry(QRect(10, 210, 201, 23))
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 211, 201))
        self.splitter_2 = QSplitter(self.groupBox)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(20, 40, 49, 111))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.label = QLabel(self.splitter_2)
        self.label.setObjectName(u"label")
        self.splitter_2.addWidget(self.label)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.splitter_2.addWidget(self.label_2)
        self.label_3 = QLabel(self.splitter_2)
        self.label_3.setObjectName(u"label_3")
        self.splitter_2.addWidget(self.label_3)
        self.label_4 = QLabel(self.splitter_2)
        self.label_4.setObjectName(u"label_4")
        self.splitter_2.addWidget(self.label_4)
        self.label_5 = QLabel(self.splitter_2)
        self.label_5.setObjectName(u"label_5")
        self.splitter_2.addWidget(self.label_5)
        self.label_6 = QLabel(self.splitter_2)
        self.label_6.setObjectName(u"label_6")
        self.splitter_2.addWidget(self.label_6)
        self.AgragrInicio_pushButton = QPushButton(self.groupBox)
        self.AgragrInicio_pushButton.setObjectName(u"AgragrInicio_pushButton")
        self.AgragrInicio_pushButton.setGeometry(QRect(10, 168, 86, 23))
        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(90, 40, 45, 120))
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(True)
        self.DesX_pinBox = QSpinBox(self.splitter)
        self.DesX_pinBox.setObjectName(u"DesX_pinBox")
        self.DesX_pinBox.setMaximum(500)
        self.splitter.addWidget(self.DesX_pinBox)
        self.DesY_spinBox_2 = QSpinBox(self.splitter)
        self.DesY_spinBox_2.setObjectName(u"DesY_spinBox_2")
        self.DesY_spinBox_2.setMaximum(500)
        self.splitter.addWidget(self.DesY_spinBox_2)
        self.Velocidad_spinBox_3 = QSpinBox(self.splitter)
        self.Velocidad_spinBox_3.setObjectName(u"Velocidad_spinBox_3")
        self.Velocidad_spinBox_3.setMaximum(1000)
        self.splitter.addWidget(self.Velocidad_spinBox_3)
        self.Red_spinBox_4 = QSpinBox(self.splitter)
        self.Red_spinBox_4.setObjectName(u"Red_spinBox_4")
        self.Red_spinBox_4.setMaximum(255)
        self.splitter.addWidget(self.Red_spinBox_4)
        self.Green_spinBox_5 = QSpinBox(self.splitter)
        self.Green_spinBox_5.setObjectName(u"Green_spinBox_5")
        self.Green_spinBox_5.setMaximum(255)
        self.splitter.addWidget(self.Green_spinBox_5)
        self.Blue_spinBox_6 = QSpinBox(self.splitter)
        self.Blue_spinBox_6.setObjectName(u"Blue_spinBox_6")
        self.Blue_spinBox_6.setMaximum(255)
        self.splitter.addWidget(self.Blue_spinBox_6)
        self.agregarFinal_pushButton = QPushButton(self.groupBox)
        self.agregarFinal_pushButton.setObjectName(u"agregarFinal_pushButton")
        self.agregarFinal_pushButton.setGeometry(QRect(109, 168, 81, 23))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 20, 49, 11))
        self.ID_pinBox = QSpinBox(self.groupBox)
        self.ID_pinBox.setObjectName(u"ID_pinBox")
        self.ID_pinBox.setGeometry(QRect(90, 20, 45, 16))
        self.ID_pinBox.setMaximum(500000)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Tabla = QTableWidget(self.tab_2)
        self.Tabla.setObjectName(u"Tabla")

        self.gridLayout.addWidget(self.Tabla, 0, 0, 1, 3)

        self.Buscar_lineEdit = QLineEdit(self.tab_2)
        self.Buscar_lineEdit.setObjectName(u"Buscar_lineEdit")

        self.gridLayout.addWidget(self.Buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.Mostrar_Tabla_pushButton_2 = QPushButton(self.tab_2)
        self.Mostrar_Tabla_pushButton_2.setObjectName(u"Mostrar_Tabla_pushButton_2")

        self.gridLayout.addWidget(self.Mostrar_Tabla_pushButton_2, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1359, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionAbrir)
        self.menuFile.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.Mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.AgragrInicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al Inicio", None))
        self.agregarFinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Mostrar_Tabla_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mostra", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

