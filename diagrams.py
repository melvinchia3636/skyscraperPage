from PyQt6 import QtCore, QtGui, QtWidgets
from threading import Thread
import requests
from urllib.request import urlopen


class Component_Item(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.initializeComponents()
        self.setupComponents()
        self.placeComponents()

    def initializeComponents(self):
        self.MainContainer = QtWidgets.QVBoxLayout(self)
        self.SubtitleLabel = QtWidgets.QLabel(self)
        self.DiagramLabel = QtWidgets.QLabel(self)
        self.ViewButton = QtWidgets.QPushButton(self, text="View")

    def setupComponents(self):
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(16)
        font.setBold(True)
        self.SubtitleLabel.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(13)
        self.ViewButton.setFont(font)
        self.ViewButton.setMinimumSize(QtCore.QSize(0, 40))

    def placeComponents(self):
        self.MainContainer.addWidget(self.SubtitleLabel)
        self.MainContainer.addWidget(self.DiagramLabel)
        self.MainContainer.addWidget(self.ViewButton)

        self.setLayout(self.MainContainer)

    def setSubtitle(self, text):
        self.SubtitleLabel.setText(text)

    def setDiagram(self, path):
        self.DiagramLabel.setPixmap(QtGui.QPixmap(path))
        self.DiagramLabel.setScaledContents(True)

    def addSpacer(self):
        self.MainContainer.addSpacerItem(
            QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding))


class Ui_Diagrams(object):
    def setupUi(self, MainWindow):
        self.data = []
        self.MainWindow = MainWindow
        QtCore.QDir.addSearchPath('diagrams', 'assets/diagrams/')

        MainWindow.resize(960, 500)

        self.Title1Label = QtWidgets.QLabel(parent=MainWindow)
        self.Title2Label = QtWidgets.QLabel(parent=MainWindow)

        self.MainContainer = QtWidgets.QVBoxLayout(MainWindow)
        self.ContentWrapper = QtWidgets.QScrollArea(MainWindow)
        self.ContentWrapper.setWidgetResizable(True)
        self.ContentContainer = QtWidgets.QWidget()
        self.ContentContainerLayout = QtWidgets.QGridLayout(
            self.ContentContainer)

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(20)
        font.setBold(True)
        self.Title1Label.setFont(font)
        self.Title1Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setBold(True)
        self.Title2Label.setFont(font)
        self.Title2Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.MainContainer.addWidget(self.Title1Label)
        self.MainContainer.addWidget(self.Title2Label)

        self.ContentWrapper.setWidget(self.ContentContainer)
        self.MainContainer.addWidget(self.ContentWrapper)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def updateContent(self):
        for i in reversed(range(self.ContentContainerLayout.count())):
            self.ContentContainerLayout.itemAt(i).widget().setParent(None)

        default_pixmap = self.__create_default_pixmap()

        for i, item in enumerate(self.data[0:3]):
            component = Component_Item()
            component.setSubtitle(item[1])
            component.setDiagram(default_pixmap)
            component.ViewButton.clicked.connect(
                lambda _, i=i: self.openDiagram(i))

            self.ContentContainerLayout.addWidget(component, 0, i, 1, 1)

        for i, item in enumerate(self.data[3:6]):
            component = Component_Item()
            component.setSubtitle(item[1])
            component.setDiagram(default_pixmap)
            component.ViewButton.clicked.connect(
                lambda _, i=i: self.openDiagram(i+3))

            self.ContentContainerLayout.addWidget(
                component, 1, i, 1 if i < 2 else 2, 1)

            if i == 2:
                component.addSpacer()

        for i, item in enumerate(self.data[6:8]):
            component = Component_Item()
            component.setSubtitle(item[1])
            component.setDiagram(default_pixmap)
            component.ViewButton.clicked.connect(
                lambda _, i=i: self.openDiagram(i+6))

            self.ContentContainerLayout.addWidget(
                component, 2, i, 1, 1)

        for i, item in enumerate(self.data[8:]):
            component = Component_Item()
            component.setSubtitle(item[1])
            component.setDiagram(default_pixmap)
            component.ViewButton.clicked.connect(
                lambda _, i=i: self.openDiagram(i+8))

            self.ContentContainerLayout.addWidget(
                component, int(3 + (i) / 3), (i - 1) % 3, 1, 1)

        thread = Thread(
            target=lambda: self.__lazy_load_pixmaps())
        thread.start()

    def __create_default_pixmap(self):
        url = 'https://placehold.co/100x60/png?text=Image+Loading...'
        data = urlopen(url).read()
        default_pixmap = QtGui.QPixmap()
        default_pixmap.loadFromData(data)
        return default_pixmap.scaledToHeight(100)

    def __lazy_load_pixmaps(self) -> None:
        for i, item in enumerate(self.data):
            response = requests.get("https://skyscraperpage.com/" + item[2])

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(response.content)
            self.ContentContainerLayout.itemAt(
                i).widget().DiagramLabel.setPixmap(pixmap)

    def retranslateUi(self, Form):
        Form.setWindowTitle("Skyscraper Diagrams")
        self.Title1Label.setText("Skyscraper Diagrams")
        self.Title2Label.setText(
            "710+ cities, 60,000+ structures, 77,000+ drawings")
