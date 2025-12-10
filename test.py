import  sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton,QMessageBox, QRadioButton, QGroupBox,QVBoxLayout
from Pregunta import Pregunta

class Principal(QMainWindow):
    #constructor de la clase principal
    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")

        #declara variables globales 
        self.crearCuestionario()
        self.index=0
        self.maximo =len(self.cuestionario)
        print(self.maximo)
        self.resp = 0

        #Crea los diferentes widgets
        self.lb_num=QLabel(str(self.cuestionario[self.index].num_pregunta))
        self.lb_num_pregunta= QLabel(self.cuestionario[self.index].pregunta)
        self.btn_siguiente=QPushButton("Siguiente")

        self.grupo= QGroupBox ("Seleccione una opcion")
        vbox= QVBoxLayout()

        self.nunca= QRadioButton("Nunca")
        self.aveces= QRadioButton("A veces")
        self.frec= QRadioButton("Frecuentemente")
        self.siempre= QRadioButton("Siempre")

        vbox.addWidget(self.nunca)
        vbox.addWidget(self.aveces)
        vbox.addWidget(self.frec)
        vbox.addWidget(self.siempre)
        self.grupo.setLayout(vbox)

        #crea el layout y los agrega en la coordenada deseada
        layout = QGridLayout()
        layout.addWidget(self.lb_num,0,0)
        layout.addWidget(self.lb_pregunta,1,0)
        layout.addWidget(self.grupo,2,0)
        layout.addWidget(self.btn_siguiente,3,0)

        #crea los eventos
        self.btn_siguiente.clicked.connect(self.siguiente)

        #agrega el layout a la ventana
        widget = widget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def crearCuestionario(self):
        #creacion de objeto
         pregunta1 = Pregunta(1,"¿Juegas videojuegos mas de 4 horas al dia?",0)
         pregunta2 = Pregunta(2,"¿Te has sentido ansioso o irritado cuando no puedes jugar?",0)
         pregunta3 = Pregunta(3,"¿Has experimentado ansiedad por los videojuegos?",0)
         pregunta4 = Pregunta(4,"¿Cuando juegas por mucho tiempo tienes una gran dificultad para detenerte?",0)
         pregunta5 = Pregunta(5,"¿Has descuidado tus intereces por jugar videojuegos?",0)
         pregunta6 = Pregunta(6,"¿Juegas mas tiempo del que planeas cada que empiezas a jugar?",0)
         pregunta7 = Pregunta(7,"¿Usas los videojuegos para sentirte mejor cuando estas triste o estresado?",0)
         pregunta8 = Pregunta(8,"¿has perdido el interes en otras actividades que antes disfrutabas porque ahora prefieres jugar?",0)
         pregunta9 = Pregunta(9,"¿Te encuentas preocupado por tu conducta hacia las personas?",0)
         pregunta10 = Pregunta(10,"¿Tus problemas con los videojuegos han causado conflictos serios con tu familia o amigos?",0)

         #agrega los elementos a una lista llamada cuestionario
         self.cuestionario = [pregunta1,pregunta2,pregunta3,pregunta4,pregunta5,pregunta6,pregunta7,pregunta8,pregunta9,pregunta10] 
    
    def siguiente(self):
         self.validar_respuesta()
         if self.resp >=0:
             #Guardar la respuesta
             self.cuestionario[self.index].respuesta=self.resp
             print(self.cuestionario[self.index].respuesta)

             if self.index < self.maximo -1:
                 self.index = self.index +1
                 num=str(self.cuestionario[self.index].num_pregunta)
                 preg=self.cuestionario[self.index].Pregunta
                 self.lb_num.setText(num)
                 self.lb_pregunta.setText(preg)

    def validar_respuesta(self):
        if self.nunca.isChecked():
            self.resp = 0
        elif self.aveces.isChecked():
            self.resp = 1
        elif self.frec.isChecked():
            self.resp = 2
        elif self.siempre.isChecked():
            self.resp = 3
        else:QMessageBox.warning(self,"Error","Seleccione una opcion")
        self.resp = -1
        
app= QApplication(sys.argv)
window=Principal()
window.show() 
app.exec()