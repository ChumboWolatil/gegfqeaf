from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QListWidget, QDialog, QLineEdit
import sys


class Add(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.setWindowTitle("Adicionar Morador")
        self.setGeometry(50,50, 500, 400)
        self.inputText()

    def inputText(self):
        nome = QLineEdit(self)
        nome.setText("Nome")
        nome.setGeometry(20,20,400,40)
        cpf = QLineEdit(self)
        cpf.setText("CPF")
        cpf.setGeometry(20, 80, 400, 40)
        email = QLineEdit(self)
        email.setText("E-Mail")
        email.setGeometry(20, 140, 400, 40)
        senha = QLineEdit(self)
        senha.setText("senha")
        senha.setGeometry(20, 200, 400, 40)

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Sol Nascente")
        self.setGeometry(0, 0, 800, 600)
        self.initUI()

    def initUI(self):
        self.labels()
        self.buttons()
        self.listMoradores()

    def labels(self):
        self.moradorLabel = QLabel(self)
        self.moradorLabel.setText('Moradores')
        self.moradorLabel.setGeometry(260, 0, 91, 16)


    def buttons(self):
        self.adicionar = QPushButton(self)
        self.adicionar.setText('Adicionar')
        self.adicionar.setGeometry(500, 150, 75, 24)
        self.adicionar.clicked.connect(self.adicionarF)
        self.excluir = QPushButton(self)
        self.excluir.setGeometry(500, 190, 75, 24)
        self.excluir.setText('Excluir')
        self.editar = QPushButton(self)
        self.editar.setGeometry(500, 110, 75, 24)
        self.editar.setText('Editar')

    def listMoradores(self):
        self.moradorList = QListWidget(self)
        self.moradorList.setGeometry(0, 30, 500, 260)

    def adicionarF(self):
        window = Add()
        window.show()
        x = window.exec_()




def inicio():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


inicio()
