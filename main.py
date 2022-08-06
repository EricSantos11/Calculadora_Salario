from PyQt6.QtWidgets import QApplication
import sys
from main_window import MainWindow

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()