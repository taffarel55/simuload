# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaocaires/Documentos/Projetos/Pessoal/Python/simuload/simuload/user_interface/original_design/transformadorMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuTransformador(object):
    def setupUi(self, MenuTransformador):
        MenuTransformador.setObjectName("MenuTransformador")
        MenuTransformador.resize(600, 500)
        self.verticalLayoutWidget = QtWidgets.QWidget(MenuTransformador)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.procuraTransf = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.procuraTransf.setFont(font)
        self.procuraTransf.setObjectName("procuraTransf")
        self.horizontalLayout_2.addWidget(self.procuraTransf)
        self.procurarBotao = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(12)
        self.procurarBotao.setFont(font)
        self.procurarBotao.setObjectName("procurarBotao")
        self.horizontalLayout_2.addWidget(self.procurarBotao)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.transformadorLista = QtWidgets.QListWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(10)
        self.transformadorLista.setFont(font)
        self.transformadorLista.setObjectName("transformadorLista")
        self.verticalLayout.addWidget(self.transformadorLista)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ExcluirTransformador = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(12)
        self.ExcluirTransformador.setFont(font)
        self.ExcluirTransformador.setObjectName("ExcluirTransformador")
        self.horizontalLayout.addWidget(self.ExcluirTransformador)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.NovoTransformador = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(12)
        self.NovoTransformador.setFont(font)
        self.NovoTransformador.setObjectName("NovoTransformador")
        self.horizontalLayout.addWidget(self.NovoTransformador)
        self.EditarTransformador = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(12)
        self.EditarTransformador.setFont(font)
        self.EditarTransformador.setObjectName("EditarTransformador")
        self.horizontalLayout.addWidget(self.EditarTransformador)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MenuTransformador)
        QtCore.QMetaObject.connectSlotsByName(MenuTransformador)

    def retranslateUi(self, MenuTransformador):
        _translate = QtCore.QCoreApplication.translate
        MenuTransformador.setWindowTitle(_translate("MenuTransformador", "Transformadores"))
        self.procurarBotao.setText(_translate("MenuTransformador", "Procurar"))
        self.ExcluirTransformador.setText(_translate("MenuTransformador", "Excluir"))
        self.NovoTransformador.setText(_translate("MenuTransformador", "Criar Novo"))
        self.EditarTransformador.setText(_translate("MenuTransformador", "Editar"))
