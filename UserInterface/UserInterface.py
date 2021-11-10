from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window():
   def setupUI(self):
       app = QApplication(sys.argv)
       win = QMainWindow()
       win.setGeometry(0, 0, 800, 600)
       win.setWindowTitle('Teste')

       win.show()
       sys.exit(app.exec_())

window = Window()
window.setupUI()

