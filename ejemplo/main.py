import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QListWidget, QListWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.search)

        self.results_list = QListWidget()
        self.results_list.itemClicked.connect(self.show_details)

        self.setCentralWidget(self.search_bar)
        self.setCentralWidget(self.results_list)

    def search(self):
        search_term = self.search_bar.text()
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{search_term}")
        pokemon_info = response.json()

        list_item = QListWidgetItem(pokemon_info["name"])
        list_item.setData(0, pokemon_info)
        self.results_list.addItem(list_item)

    def show_details(self, item):
        pokemon_info = item.data(0)
        # create a new window with the detailed information
        pass


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()