# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaocaires/Documentos/Projetos/Pessoal/Python/simuload/simuload/user_interface/nova_carga.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NovaCarga(object):
    def setupUi(self, NovaCarga):
        NovaCarga.setObjectName("NovaCarga")
        NovaCarga.resize(396, 300)
        self.groupBox = QtWidgets.QGroupBox(NovaCarga)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 41))
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 361, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox_2 = QtWidgets.QGroupBox(NovaCarga)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 60, 381, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 19, 361, 181))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.equipList = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.equipList.setObjectName("equipList")
        self.horizontalLayout_2.addWidget(self.equipList)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addOne = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.addOne.setObjectName("addOne")
        self.verticalLayout_2.addWidget(self.addOne)
        self.addMany = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.addMany.setObjectName("addMany")
        self.verticalLayout_2.addWidget(self.addMany)
        self.equipNum = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.equipNum.setMinimum(0)
        self.equipNum.setMaximum(100)
        self.equipNum.setProperty("value", 10)
        self.equipNum.setObjectName("equipNum")
        self.verticalLayout_2.addWidget(self.equipNum)
        self.removeEquip = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.removeEquip.setObjectName("removeEquip")
        self.verticalLayout_2.addWidget(self.removeEquip)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.addedEquipList = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.addedEquipList.setObjectName("addedEquipList")
        self.horizontalLayout_2.addWidget(self.addedEquipList)
        self.line = QtWidgets.QFrame(NovaCarga)
        self.line.setGeometry(QtCore.QRect(10, 260, 381, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(NovaCarga)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 270, 261, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.criarCarga = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.criarCarga.setObjectName("criarCarga")
        self.horizontalLayout.addWidget(self.criarCarga)
        self.cancelarCarga = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancelarCarga.setObjectName("cancelarCarga")
        self.horizontalLayout.addWidget(self.cancelarCarga)

        self.retranslateUi(NovaCarga)
        QtCore.QMetaObject.connectSlotsByName(NovaCarga)

    def retranslateUi(self, NovaCarga):
        _translate = QtCore.QCoreApplication.translate
        NovaCarga.setWindowTitle(_translate("NovaCarga", "Carga"))
        self.groupBox.setTitle(_translate("NovaCarga", "Carga"))
        self.label_5.setText(_translate("NovaCarga", "Conjunto de equipamentos que constituem um consumidor"))
        self.groupBox_2.setTitle(_translate("NovaCarga", "Adicionar Equipamentos"))
        self.addOne.setText(_translate("NovaCarga", ">"))
        self.addMany.setText(_translate("NovaCarga", ">>"))
        self.removeEquip.setText(_translate("NovaCarga", "Remover"))
        self.criarCarga.setText(_translate("NovaCarga", "OK"))
        self.cancelarCarga.setText(_translate("NovaCarga", "Cancelar"))
