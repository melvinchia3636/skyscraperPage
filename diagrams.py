from PyQt6 import QtCore, QtGui, QtWidgets
import sys


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
        self.ViewButton = QtWidgets.QPushButton(self)

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

    def setButtonText(self, text):
        self.ViewButton.setText(text)


class Ui_Diagrams(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        QtCore.QDir.addSearchPath('diagrams', 'assets/diagrams/')

        MainWindow.resize(926, 878)

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

        for i in range(3):
            for j in range(3):
                item = Component_Item(self.ContentContainer)
                item.setSubtitle("City, Country")
                item.setDiagram(
                    "diagrams:world_skyscraper_construction_2330944475.png")
                item.setButtonText("View Diagram")
                self.ContentContainerLayout.addWidget(item, i, j, 1, 1)

        self.ContentWrapper.setWidget(self.ContentContainer)
        self.MainContainer.addWidget(self.ContentWrapper)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Form):
        Form.setWindowTitle("Skyscraper Diagrams")
        self.Title1Label.setText("Skyscraper Diagrams")
        self.Title2Label.setText(
            "710+ cities, 60,000+ structures, 77,000+ drawings")
