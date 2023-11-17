from threading import Thread
from urllib.request import urlopen
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea, \
    QGridLayout, QLabel

import requests
import time


class TestWindow(QMainWindow):

    bigger_list = [
        ["https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Java_programming_language_logo.svg/121px-Java_programming_language_logo.svg.png"],
        ["https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Java_programming_language_logo.svg/121px-Java_programming_language_logo.svg.png"]
    ]

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.setFixedWidth(1230)
        self.setFixedHeight(740)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)
        central_widget.setLayout(layout)

        output_scroll = QScrollArea(self)
        output_scroll.setWidgetResizable(True)
        output_container = QWidget()
        self.output_layout = QVBoxLayout()
        output_container.setLayout(self.output_layout)
        output_scroll.setWidget(output_container)
        output_scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        output_scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        output_scroll.setWidgetResizable(True)

        self.button = QPushButton("Run", self)
        self.button.clicked.connect(self.on_click)
        self.setLayout(layout)

        layout.addWidget(output_scroll)
        layout.addWidget(self.button)

    def on_click(self):
        default_pixmap = self.__create_default_pixmap()

        # Create a list which contains labels and its request url.
        widget_and_url_list: list[tuple[QLabel, str]] = []

        for smaller_list in self.bigger_list:
            grid = QGridLayout()

            for i, url in enumerate(smaller_list):
                # Loop over to create widgets.
                # Keep in mind that we should create widgets in main thread. Otherwise, some errors might occur
                image_label = QLabel()
                image_label.setPixmap(default_pixmap)
                grid.addWidget(image_label, int(i / 5), i % 5)

                widget_and_url_list.append((image_label, url))
            self.output_layout.addLayout(grid)
            self.output_layout.addStretch()

        # This is how you can call a thread in python. There is a class name QThread but it is quite overkill in this case.
        # You just have to pass the function into lambda
        thread = Thread(
            target=lambda: self.__lazy_load_pixmaps(widget_and_url_list))
        thread.start()

    def __create_default_pixmap(self) -> QPixmap:
        url = 'https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Java_programming_language_logo.svg/121px-Java_programming_language_logo.svg.png'
        data = urlopen(url).read()
        default_pixmap: QPixmap = QPixmap()
        default_pixmap.loadFromData(data)
        return default_pixmap.scaledToHeight(100)

    def __lazy_load_pixmaps(self, widget_and_url_list: list[tuple[QLabel, str]]) -> None:
        for widget_and_url in widget_and_url_list:
            widget, url = widget_and_url
            response = requests.get(url)

            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            pixmap = pixmap.scaledToHeight(100)
            widget.setPixmap(pixmap)
            # This make the loading pixmaps feel more smoothly
            time.sleep(0.02)


def main():
    app = QApplication([])
    window = TestWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
