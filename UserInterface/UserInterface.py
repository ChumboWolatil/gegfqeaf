from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QCheckBox, QPushButton, QListWidget
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Sol Nascente")
        self.setGeometry(0, 0, 800, 600)
        self.initUI()

    def initUI(self):
        self.labels()
        self.checkButtons()
        self.buttons()
        self.listMoradores()

    def labels(self):
        self.condominioLabel = QLabel(self)
        self.condominioLabel.setText('Condominios')
        self.condominioLabel.setGeometry(0, 0, 91, 16)
        self.moradorLabel = QLabel(self)
        self.moradorLabel.setText('Moradores')
        self.moradorLabel.setGeometry(260, 0, 91, 16)

    def checkButtons(self):
        self.rosaCheck = QCheckBox(self)
        self.rosaCheck.setText("Condominio Rosa Flores")
        self.rosaCheck.setGeometry(0, 30, 200, 20)
        self.homeCheck = QCheckBox(self)
        self.homeCheck.setText('Condominio Home Beach')
        self.homeCheck.setGeometry(0, 60, 200, 20)

    def buttons(self):
        self.adicionar = QPushButton(self)
        self.adicionar.setText('Adicionar')
        self.adicionar.setGeometry(500, 150, 75, 24)
        self.excluir = QPushButton(self)
        self.excluir.setGeometry(500, 190, 75, 24)
        self.excluir.setText('Excluir')
        self.editar = QPushButton(self)
        self.editar.setGeometry(500, 110, 75, 24)
        self.editar.setText('Editar')

    def listMoradores(self):
        self.moradorList = QListWidget(self)
        self.moradorList.setGeometry(260, 30, 240, 190)

def inicio():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


inicio()
