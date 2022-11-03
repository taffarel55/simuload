# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaocaires/Documentos/Projetos/Pessoal/Python/simuload/simuload/user_interface/original_design/janela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 397)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 160, 211, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.carga_menu = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.carga_menu.setObjectName("carga_menu")
        self.verticalLayout.addWidget(self.carga_menu)
        self.equipamento_menu = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.equipamento_menu.setObjectName("equipamento_menu")
        self.verticalLayout.addWidget(self.equipamento_menu)
        self.editar_curva = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.editar_curva.setObjectName("editar_curva")
        self.verticalLayout.addWidget(self.editar_curva)
        self.simular_curva = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.simular_curva.setObjectName("simular_curva")
        self.verticalLayout.addWidget(self.simular_curva)
        self.barra_progresso = QtWidgets.QProgressBar(self.centralwidget)
        self.barra_progresso.setGeometry(QtCore.QRect(10, 310, 551, 23))
        self.barra_progresso.setProperty("value", 0)
        self.barra_progresso.setObjectName("barra_progresso")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 10, 20, 291))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(20, 30, 191, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("/home/joaocaires/Documentos/Projetos/Pessoal/Python/simuload/simuload/user_interface/original_design/../img/simuload-logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.lista_curvas = QtWidgets.QListView(self.centralwidget)
        self.lista_curvas.setGeometry(QtCore.QRect(250, 50, 301, 251))
        self.lista_curvas.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.lista_curvas.setObjectName("lista_curvas")
        self.titulo_curvas = QtWidgets.QLabel(self.centralwidget)
        self.titulo_curvas.setGeometry(QtCore.QRect(250, 20, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.titulo_curvas.setFont(font)
        self.titulo_curvas.setObjectName("titulo_curvas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSalvar_como = QtWidgets.QMenu(self.menuFile)
        self.menuSalvar_como.setObjectName("menuSalvar_como")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuCurva = QtWidgets.QMenu(self.menuEditar)
        self.menuCurva.setObjectName("menuCurva")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNova_Curva = QtWidgets.QAction(MainWindow)
        self.actionNova_Curva.setObjectName("actionNova_Curva")
        self.actionAbrir_Curva = QtWidgets.QAction(MainWindow)
        self.actionAbrir_Curva.setObjectName("actionAbrir_Curva")
        self.actionCurvas_Recentes = QtWidgets.QAction(MainWindow)
        self.actionCurvas_Recentes.setObjectName("actionCurvas_Recentes")
        self.actionSalvar_Curva = QtWidgets.QAction(MainWindow)
        self.actionSalvar_Curva.setObjectName("actionSalvar_Curva")
        self.action_csv = QtWidgets.QAction(MainWindow)
        self.action_csv.setObjectName("action_csv")
        self.action_xls = QtWidgets.QAction(MainWindow)
        self.action_xls.setObjectName("action_xls")
        self.actionDura_o = QtWidgets.QAction(MainWindow)
        self.actionDura_o.setObjectName("actionDura_o")
        self.actionIntervalo = QtWidgets.QAction(MainWindow)
        self.actionIntervalo.setObjectName("actionIntervalo")
        self.actionDura_o_2 = QtWidgets.QAction(MainWindow)
        self.actionDura_o_2.setObjectName("actionDura_o_2")
        self.menuSalvar_como.addAction(self.action_csv)
        self.menuSalvar_como.addAction(self.action_xls)
        self.menuFile.addAction(self.actionNova_Curva)
        self.menuFile.addAction(self.actionAbrir_Curva)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSalvar_Curva)
        self.menuFile.addAction(self.menuSalvar_como.menuAction())
        self.menuCurva.addAction(self.actionIntervalo)
        self.menuCurva.addAction(self.actionDura_o_2)
        self.menuEditar.addAction(self.menuCurva.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIMULOAD"))
        self.carga_menu.setText(_translate("MainWindow", "Cargas"))
        self.equipamento_menu.setText(_translate("MainWindow", "Equipamentos"))
        self.editar_curva.setText(_translate("MainWindow", "Editar Curva"))
        self.simular_curva.setText(_translate("MainWindow", "Simular Curva"))
        self.titulo_curvas.setText(_translate("MainWindow", "Selecione uma curva de cargas"))
        self.menuFile.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuSalvar_como.setTitle(_translate("MainWindow", "Salvar como..."))
        self.menuEditar.setTitle(_translate("MainWindow", "Configurações"))
        self.menuCurva.setTitle(_translate("MainWindow", "Curva"))
        self.actionNova_Curva.setText(_translate("MainWindow", "Nova Curva"))
        self.actionAbrir_Curva.setText(_translate("MainWindow", "Abrir Curva"))
        self.actionCurvas_Recentes.setText(_translate("MainWindow", "Curvas Recentes"))
        self.actionSalvar_Curva.setText(_translate("MainWindow", "Salvar Curva"))
        self.action_csv.setText(_translate("MainWindow", ".csv"))
        self.action_xls.setText(_translate("MainWindow", ".xls"))
        self.actionDura_o.setText(_translate("MainWindow", "Duração"))
        self.actionIntervalo.setText(_translate("MainWindow", "Intervalo"))
        self.actionDura_o_2.setText(_translate("MainWindow", "Duração"))
