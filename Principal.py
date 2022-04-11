import sys
from PyQt5 import QtWidgets, uic
import re
from disenio.interfaz import *


class Principal(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_ventanaPrincipal()
        self.ui.setupUi(self)
        self.ui.btnAceptar.clicked.connect(lambda: self.validar(self.ui.lineEditClave.text()))

    def validar(self, clave):
        if re.findall('^[A-Z][\d]{3}[a-z]{3}[#%$*+-]{3}$', clave):
           self.ui.estado.setStyleSheet("color:green")
           self.ui.estado.setText("Aceptada")
        else:
           self.ui.estado.setStyleSheet("color:red")
           self.ui.estado.setText('Rechazada')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = Principal()
    GUI.show()
    sys.exit(app.exec_())
