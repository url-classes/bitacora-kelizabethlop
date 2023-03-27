from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt6 import QtCore
from circular_list import CircularList
from process import Process


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.circular_list = CircularList()

        self.setWindowTitle('Proceso')

        main_layout = QVBoxLayout()
        layout = QHBoxLayout()
        self.label = QLabel('PROCESOS NUEVOS: procesos en la CPU para completar todas las operaciones')
        layout.addWidget(self.label)
        main_layout.addLayout(layout)

        layout1 = QHBoxLayout()
        self.time_label = QLabel('ID (4 dígitos):')
        layout1.addWidget(self.time_label)

        self.id_textbox = QLineEdit()
        layout1.addWidget(self.id_textbox)

        self.time_label = QLabel('Tiempo:')
        layout1.addWidget(self.time_label)

        self.time_textbox = QLineEdit()
        layout1.addWidget(self.time_textbox)

        add_button = QPushButton('Añadir proceso')
        add_button.clicked.connect(self.add_process)
        layout1.addWidget(add_button)
        main_layout.addLayout(layout1)

        attend_button = QPushButton('Atender proceso')
        attend_button.clicked.connect(self.attend_process)
        main_layout.addWidget(attend_button)

        self.process = QLabel()
        self.process.setWordWrap(True)
        main_layout.addWidget(self.process)

        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)

    def add_process(self):
        try:
            remaining_time = 0
            process_id = int(self.id_textbox.text())
            process_time = int(self.time_textbox.text())
            if len(str(process_id)) == 4:
                process = Process(process_id, process_time)

                self.circular_list.append(process)

                for i in range(0, self.circular_list.size):
                    current_process = self.circular_list.find_at(i)
                    remaining_time += current_process.data.time

                self.process.setText(f'{self.circular_list.transversal()} \nProcesos Activos: {self.circular_list.size}'
                                     f'\nTiempo restante: {remaining_time}')
            else:
                print('El ID debe ser 4 dígitos')

        except Exception as error:
            print('Los procesos deben de ser registrados como enteros')

    def attend_process(self):
        remaining_time = 0
        current_process = self.circular_list.head.data
        current_process.time -= 2

        if current_process.time <= 0:
            self.circular_list.pop()
        else:
            self.circular_list.prepend(self.circular_list.pop().data)

        for i in range(0, self.circular_list.size):
            current_process = self.circular_list.find_at(i)
            remaining_time += current_process.data.time

        self.process.setText(f'{self.circular_list.transversal()} \nActive process: {self.circular_list.size}'
                             f'\nRemaining time: {remaining_time}')
