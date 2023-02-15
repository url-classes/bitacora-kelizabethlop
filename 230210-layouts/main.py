import sys
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow, MainWindow2, MainWindow3, MainWindow4, MainWindow5


app = QApplication(sys.argv)

v_window = MainWindow()
v_window.show()

h_window = MainWindow2()
h_window.show()

vh_window = MainWindow3()
vh_window.show()

g_window = MainWindow4()
g_window.show()

s_window = MainWindow5()
s_window.show()

app.exec()
