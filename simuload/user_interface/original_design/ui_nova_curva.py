# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joaocaires/Documentos/Projetos/Pessoal/Python/simuload/simuload/user_interface/original_design/nova_curva.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_curveEdit(object):
    def setupUi(self, curveEdit):
        curveEdit.setObjectName("curveEdit")
        curveEdit.resize(400, 300)
        self.groupBox = QtWidgets.QGroupBox(curveEdit)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 381, 41))
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 291, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox_2 = QtWidgets.QGroupBox(curveEdit)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 381, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 19, 361, 181))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(100)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_2.addWidget(self.spinBox)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_2.addWidget(self.listWidget_2)
        self.line = QtWidgets.QFrame(curveEdit)
        self.line.setGeometry(QtCore.QRect(10, 250, 381, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(curveEdit)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 260, 261, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.criarEquipamento = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.criarEquipamento.setObjectName("criarEquipamento")
        self.horizontalLayout.addWidget(self.criarEquipamento)
        self.cancelarEquipamento = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancelarEquipamento.setObjectName("cancelarEquipamento")
        self.horizontalLayout.addWidget(self.cancelarEquipamento)

        self.retranslateUi(curveEdit)
        QtCore.QMetaObject.connectSlotsByName(curveEdit)

    def retranslateUi(self, curveEdit):
        _translate = QtCore.QCoreApplication.translate
        curveEdit.setWindowTitle(_translate("curveEdit", "Editar Curva"))
        self.groupBox.setTitle(_translate("curveEdit", "Curva"))
        self.label_5.setText(_translate("curveEdit", "Conjunto de cargas para simulação da curva"))
        self.groupBox_2.setTitle(_translate("curveEdit", "Adicionar Cargas"))
        self.pushButton.setText(_translate("curveEdit", ">"))
        self.pushButton_2.setText(_translate("curveEdit", ">>"))
        self.pushButton_3.setText(_translate("curveEdit", "Remover"))
        self.criarEquipamento.setText(_translate("curveEdit", "OK"))
        self.cancelarEquipamento.setText(_translate("curveEdit", "Cancelar"))
