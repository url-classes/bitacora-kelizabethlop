import requests
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QImage, QPixmap

url_image = ''

app = QApplication([])
web_image = QImage()
web_image.loadFromData(requests.get(url_image).content)

image_label = QLabel()
image_label.setPixmap(QPixmap(web_image))
image_label.show()

app.exec()
