# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanaPrincipal(object):
    def setupUi(self, ventanaPrincipal):
        ventanaPrincipal.setObjectName("ventanaPrincipal")
        ventanaPrincipal.resize(637, 242)
        ventanaPrincipal.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(ventanaPrincipal)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background-color: rgb(114, 159, 207);\n"
"}\n"
"QLineEdit{\n"
"border-radius:20px;\n"
"background-color:white;\n"
"padding-left:20px;\n"
"\n"
"}\n"
"QPushButton{\n"
"border-radius:20px;\n"
"borber-bottom:2px solid;\n"
"background-color:black;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:orange;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(160, 110, 291, 41))
        self.btnAceptar.setObjectName("btnAceptar")
        self.lineEditClave = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditClave.setGeometry(QtCore.QRect(60, 30, 501, 41))
        self.lineEditClave.setClearButtonEnabled(True)
        self.lineEditClave.setObjectName("lineEditClave")
        self.estado = QtWidgets.QLabel(self.centralwidget)
        self.estado.setGeometry(QtCore.QRect(30, 180, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.estado.setFont(font)
        self.estado.setText("")
        self.estado.setObjectName("estado")
        self.lineEditClave.raise_()
        self.btnAceptar.raise_()
        self.estado.raise_()
        ventanaPrincipal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ventanaPrincipal)
        self.statusbar.setObjectName("statusbar")
        ventanaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(ventanaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(ventanaPrincipal)

    def retranslateUi(self, ventanaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        ventanaPrincipal.setWindowTitle(_translate("ventanaPrincipal", "Validador"))
        self.btnAceptar.setText(_translate("ventanaPrincipal", "Aceptar"))
        self.lineEditClave.setPlaceholderText(_translate("ventanaPrincipal", "Digite su clave"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_ventanaPrincipal()
    ui.setupUi(ventanaPrincipal)
    ventanaPrincipal.show()
    sys.exit(app.exec_())
