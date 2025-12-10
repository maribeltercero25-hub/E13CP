import sys
from PyQt5.QtWidgets import QMainWindow, QWidget,QApplication, QLabel,QLineEdit, QPushButton,QDialogButtonBox, QGridLayout
class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro")

        #Crea los diferentes widget
        self.lb_nombre= nombre =QLabel("Nombre")
        self.lb_edad= edad =QLabel("Edad")
        self.lb_telefono= telefono =QLabel("Telefono")
        self.lb_correo= correo =QLabel("Correo")
        self.txt_nombre= QLineEdit()
        self.txt_edad= QLineEdit()
        self.txt_telefono= QLineEdit()
        self.txt_correo= QLineEdit()
        self.btn_= QPushButton()
        self.btn_box =QDialogButtonBox()

#Crear el layout y los agrega en la coordenada deseada
        layout = QGridLayout()
        layout.addWidget(self.lb_nombre,0,0)
        layout.addWidget(self.txt_nombre,0,1)
        layout.addWidget(self.lb_edad,1,0)
        layout.addWidget(self.txt_edad,1,1)
        layout.addWidget(self.lb_telefono,2,0)
        layout.addWidget(self.txt_telefono,2,1)
        layout.addWidget(self.lb_correo,3,0)
        layout.addWidget(self.txt_correo,3,1)
        layout.addWidget(self.btn_box)



app=QApplication(sys.argv)
window=Principal()
window.show()
app.exec()