# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
        MainWindow.resize(978, 598)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionPuntos = QAction(MainWindow)
        self.actionPuntos.setObjectName(u"actionPuntos")
        self.actionPuntos_Cercanos = QAction(MainWindow)
        self.actionPuntos_Cercanos.setObjectName(u"actionPuntos_Cercanos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.graphicsView = QGraphicsView(self.tab)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 5)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 3, 2, 1)

        self.id = QSpinBox(self.tab)
        self.id.setObjectName(u"id")
        self.id.setMaximum(500)

        self.gridLayout_2.addWidget(self.id, 2, 0, 2, 1)

        self.origen_x = QSpinBox(self.tab)
        self.origen_x.setObjectName(u"origen_x")
        self.origen_x.setMaximum(500)

        self.gridLayout_2.addWidget(self.origen_x, 3, 1, 1, 1)

        self.destino_x = QSpinBox(self.tab)
        self.destino_x.setObjectName(u"destino_x")
        self.destino_x.setMaximum(500)

        self.gridLayout_2.addWidget(self.destino_x, 3, 3, 1, 1)

        self.rojo = QSpinBox(self.tab)
        self.rojo.setObjectName(u"rojo")
        self.rojo.setMaximum(255)

        self.gridLayout_2.addWidget(self.rojo, 3, 6, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 8, 2, 1)

        self.azul = QSpinBox(self.tab)
        self.azul.setObjectName(u"azul")
        self.azul.setMaximum(255)

        self.gridLayout_2.addWidget(self.azul, 3, 8, 1, 1)

        self.destino_y = QSpinBox(self.tab)
        self.destino_y.setObjectName(u"destino_y")
        self.destino_y.setMaximum(500)

        self.gridLayout_2.addWidget(self.destino_y, 3, 4, 1, 1)

        self.velocidad = QSpinBox(self.tab)
        self.velocidad.setObjectName(u"velocidad")
        self.velocidad.setMaximum(500)

        self.gridLayout_2.addWidget(self.velocidad, 3, 5, 1, 1)

        self.origen_y = QSpinBox(self.tab)
        self.origen_y.setObjectName(u"origen_y")
        self.origen_y.setMaximum(500)

        self.gridLayout_2.addWidget(self.origen_y, 3, 2, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 4, 2, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 2, 2, 1)

        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 5, 1, 4)

        self.verde = QSpinBox(self.tab)
        self.verde.setObjectName(u"verde")
        self.verde.setMaximum(255)

        self.gridLayout_2.addWidget(self.verde, 3, 7, 1, 1)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 1, 2, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 5, 2, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 7, 2, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 6, 2, 1)

        self.agregar_inicio = QPushButton(self.tab)
        self.agregar_inicio.setObjectName(u"agregar_inicio")

        self.gridLayout_2.addWidget(self.agregar_inicio, 7, 2, 1, 2)

        self.agregar_final = QPushButton(self.tab)
        self.agregar_final.setObjectName(u"agregar_final")

        self.gridLayout_2.addWidget(self.agregar_final, 7, 0, 1, 2)

        self.mostrar_adyacencias = QPushButton(self.tab)
        self.mostrar_adyacencias.setObjectName(u"mostrar_adyacencias")

        self.gridLayout_2.addWidget(self.mostrar_adyacencias, 7, 7, 1, 2)

        self.mostrar = QPushButton(self.tab)
        self.mostrar.setObjectName(u"mostrar")

        self.gridLayout_2.addWidget(self.mostrar, 7, 4, 1, 3)

        self.limpiar = QPushButton(self.tab)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_2.addWidget(self.limpiar, 4, 5, 1, 4)

        self.dibujar = QPushButton(self.tab)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_2.addWidget(self.dibujar, 4, 0, 1, 5)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_3.addWidget(self.tabla, 0, 0, 1, 5)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_3.addWidget(self.buscar_lineEdit, 1, 0, 1, 2)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_3.addWidget(self.buscar_pushButton, 1, 2, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_3.addWidget(self.mostrar_tabla_pushButton, 1, 3, 1, 1)

        self.ordenar_id = QPushButton(self.tab_2)
        self.ordenar_id.setObjectName(u"ordenar_id")

        self.gridLayout_3.addWidget(self.ordenar_id, 1, 4, 1, 1)

        self.ordenar_distancia = QPushButton(self.tab_2)
        self.ordenar_distancia.setObjectName(u"ordenar_distancia")

        self.gridLayout_3.addWidget(self.ordenar_distancia, 2, 0, 1, 1)

        self.ordenar_velocidad = QPushButton(self.tab_2)
        self.ordenar_velocidad.setObjectName(u"ordenar_velocidad")

        self.gridLayout_3.addWidget(self.ordenar_velocidad, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 978, 21))
        self.menuAbrir = QMenu(self.menubar)
        self.menuAbrir.setObjectName(u"menuAbrir")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbrir.menuAction())
        self.menuAbrir.addAction(self.actionAbrir)
        self.menuAbrir.addSeparator()
        self.menuAbrir.addAction(self.actionGuardar)
        self.menuAbrir.addAction(self.actionPuntos)
        self.menuAbrir.addSeparator()
        self.menuAbrir.addAction(self.actionPuntos_Cercanos)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.actionPuntos.setText(QCoreApplication.translate("MainWindow", u"Puntos", None))
        self.actionPuntos_Cercanos.setText(QCoreApplication.translate("MainWindow", u"Puntos Cercanos", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Destino x", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Azul", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Destino y", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen y", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Origen x", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Verde", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Rojo", None))
        self.agregar_inicio.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.agregar_final.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.mostrar_adyacencias.setText(QCoreApplication.translate("MainWindow", u"Mostrar adyacencias", None))
        self.mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identificador de particula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.ordenar_id.setText(QCoreApplication.translate("MainWindow", u"Ordenar ID ASC", None))
        self.ordenar_distancia.setText(QCoreApplication.translate("MainWindow", u"Ordenar distancia DESC", None))
        self.ordenar_velocidad.setText(QCoreApplication.translate("MainWindow", u"Ordenar velocidad ASC", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuAbrir.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

