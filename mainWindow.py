from PyQt6 import QtCore, QtGui, QtWidgets, QtNetwork
import sys
from bs4 import BeautifulSoup as bs
from diagrams import Ui_Diagrams


class ErrorDialog(QtWidgets.QDialog):
    def __init__(self, message_content):
        super().__init__()

        self.setWindowTitle("An error occurred")

        QBtn = QtWidgets.QDialogButtonBox.StandardButton.Close

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel(message_content)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def reject(self):
        sys.exit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        QtCore.QDir.addSearchPath('welcome', 'assets/welcome/')

        self.initializeComponents()
        self.setupMainWindow()
        self.setupComponents()
        self.placeComponents()
        self.setupMenuBar()
        self.addText()
        self.linkSignals()

        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def setupMainWindow(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(450, 600)
        self.MainWindow.setCentralWidget(self.MainWrapper)
        centerPoint = QtGui.QScreen.availableGeometry(
            QtGui.QGuiApplication.primaryScreen()).center()
        frame = self.MainWindow.frameGeometry()
        frame.moveCenter(centerPoint)
        self.MainContainer.setContentsMargins(-1, -1, -1, 20)

    def initializeComponents(self):
        self.Statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.MainWrapper = QtWidgets.QWidget(self.MainWindow)
        self.MainContainer = QtWidgets.QVBoxLayout(self.MainWrapper)
        self.CoverImage = QtWidgets.QLabel(self.MainWrapper)
        self.Title1Label = QtWidgets.QLabel(self.MainWrapper)
        self.Title2Label = QtWidgets.QLabel(self.MainWrapper)
        self.ButtonWrapper = QtWidgets.QHBoxLayout()
        self.ButtonContainer = QtWidgets.QVBoxLayout()
        self.ToDiagramButton = QtWidgets.QPushButton(self.MainWrapper)
        self.ToDatabaseButton = QtWidgets.QPushButton(self.MainWrapper)
        self.ButtonWrapperHorizontalSpacerLeft = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.ButtonWrapperHorizontalSpacerRight = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.SpacerBetweenButtonsAndTitle = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)

    def setupComponents(self):
        self.CoverImage.setText("")
        self.CoverImage.setPixmap(QtGui.QPixmap(
            "welcome:diagram-removebg-preview(1).png"))
        self.CoverImage.setScaledContents(True)
        self.CoverImage.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(16)

        self.Title1Label.setFont(font)
        self.Title1Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Title2Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(24)
        font.setBold(True)

        self.Title2Label.setFont(font)

        self.Title1Label.setMaximumHeight(20)
        self.Title2Label.setMaximumHeight(40)

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(16)

        self.ToDiagramButton.setFont(font)
        self.ToDatabaseButton.setFont(font)

        self.ToDiagramButton.setMinimumHeight(60)
        self.ToDatabaseButton.setMinimumHeight(60)

        self.ToDatabaseButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ToDiagramButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)

    def placeComponents(self):
        self.MainContainer.addWidget(self.CoverImage)
        self.MainContainer.addWidget(self.Title1Label)
        self.MainContainer.addWidget(self.Title2Label)
        self.MainContainer.addItem(self.SpacerBetweenButtonsAndTitle)
        self.MainContainer.addLayout(self.ButtonWrapper)

        self.ButtonWrapper.addItem(self.ButtonWrapperHorizontalSpacerLeft)
        self.ButtonWrapper.addLayout(self.ButtonContainer)
        self.ButtonWrapper.addItem(self.ButtonWrapperHorizontalSpacerRight)

        self.ButtonContainer.addWidget(self.ToDiagramButton)
        self.ButtonContainer.addWidget(self.ToDatabaseButton)

        self.MainWindow.setStatusBar(self.Statusbar)

    def setupMenuBar(self):
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menuDiagrams = QtWidgets.QMenu(self.menubar)
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuBrowse = QtWidgets.QMenu(self.menuDatabase)

        self.actionSkyscraper_Diagrams = QtGui.QAction(self.MainWindow)
        self.actionBrowse_by_Cities = QtGui.QAction(self.MainWindow)
        self.actionDiagram_Search = QtGui.QAction(self.MainWindow)
        self.actionDiagram_Statistics = QtGui.QAction(self.MainWindow)
        self.actionSearch = QtGui.QAction(self.MainWindow)
        self.actionMetropolitan_Areas = QtGui.QAction(self.MainWindow)
        self.actionBy_Metropolitan_Areas = QtGui.QAction(self.MainWindow)
        self.actionNewest_Entries = QtGui.QAction(self.MainWindow)
        self.actionBy_Countries = QtGui.QAction(self.MainWindow)
        self.actionBy_Cities = QtGui.QAction(self.MainWindow)
        self.actionBy_Metropolitan_Areas_2 = QtGui.QAction(self.MainWindow)
        self.actionBy_Cities_2 = QtGui.QAction(self.MainWindow)
        self.actionBy_Countries_2 = QtGui.QAction(self.MainWindow)
        self.actionBy_Continents = QtGui.QAction(self.MainWindow)
        self.actionStatistics = QtGui.QAction(self.MainWindow)
        self.actionInteractive_Maps = QtGui.QAction(self.MainWindow)

        self.menuDiagrams.addAction(self.actionSkyscraper_Diagrams)
        self.menuDiagrams.addAction(self.actionDiagram_Search)
        self.menuDiagrams.addAction(self.actionBrowse_by_Cities)
        self.menuDiagrams.addSeparator()
        self.menuDiagrams.addAction(self.actionDiagram_Statistics)

        self.menuBrowse.addAction(self.actionBy_Metropolitan_Areas_2)
        self.menuBrowse.addAction(self.actionBy_Cities_2)
        self.menuBrowse.addAction(self.actionBy_Countries_2)
        self.menuBrowse.addAction(self.actionBy_Continents)

        self.menuDatabase.addAction(self.menuBrowse.menuAction())
        self.menuDatabase.addAction(self.actionSearch)
        self.menuDatabase.addAction(self.actionNewest_Entries)
        self.menuDatabase.addSeparator()
        self.menuDatabase.addAction(self.actionStatistics)

        self.menubar.addAction(self.menuDiagrams.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())

        self.MainWindow.setMenuBar(self.menubar)

    def addText(self):
        self.MainWindow.setWindowTitle("MainWindow")
        self.Title1Label.setText("A GUI Client for")
        self.Title2Label.setText("SkyscraperPage.com")
        self.ToDiagramButton.setText("Diagrams")
        self.ToDatabaseButton.setText("Database")
        self.menuDiagrams.setTitle("Diagrams")
        self.menuDatabase.setTitle("Database")
        self.menuBrowse.setTitle("Browse")
        self.actionSkyscraper_Diagrams.setText("Featured")
        self.actionBrowse_by_Cities.setText("By Cities")
        self.actionDiagram_Search.setText("Search")
        self.actionDiagram_Statistics.setText("Statistics")
        self.actionSearch.setText("Search")
        self.actionMetropolitan_Areas.setText("By Continents")
        self.actionBy_Metropolitan_Areas.setText("By Metropolitan Areas")
        self.actionNewest_Entries.setText("Newest Entries")
        self.actionBy_Countries.setText("By Countries")
        self.actionBy_Cities.setText("By Cities")
        self.actionBy_Metropolitan_Areas_2.setText("By Metropolitan Areas")
        self.actionBy_Cities_2.setText("By Cities")
        self.actionBy_Countries_2.setText("By Countries")
        self.actionBy_Continents.setText("By Continents")
        self.actionStatistics.setText("Statistics")
        self.actionInteractive_Maps.setText("Interactive Maps")

    def linkSignals(self):
        self.ToDiagramButton.clicked.connect(self.toDiagrams)
        self.ToDatabaseButton.clicked.connect(self.toDatabase)

    def toDiagrams(self):
        url = 'https://skyscraperpage.com/diagrams/'
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))

        self.nam = QtNetwork.QNetworkAccessManager()
        self.Statusbar.showMessage("Fetching data from " + url)
        self.nam.finished.connect(self.parseDiagramsRawData)
        self.nam.get(req)

    def toDatabase(self):
        pass

    def parseDiagramsRawData(self, res):
        self.Statusbar.showMessage(
            "Parsing data from " + res.url().toString() + "...")
        er = res.error()

        if er == QtNetwork.QNetworkReply.NetworkError.NoError:
            bytes_string = res.readAll()
            raw = str(bytes_string, 'utf-8')
            soup = bs(raw, 'html.parser')
            data = [
                [
                    i['href'],
                    i.select_one("span").text,
                    i.select_one("img")['src']
                ] for i in soup.select("table.med:nth-child(1) a[href]")
                if i['href'].startswith('?') and i.select_one("img")
            ]

            self.MainWindow.DiagramsWindow.UiDiagrams.data = data
            self.MainWindow.DiagramsWindow.UiDiagrams.updateContent()

            if self.MainWindow.DiagramsWindow.isHidden():
                self.MainWindow.hide()
                self.MainWindow.DiagramsWindow.show()
            else:
                assert not self.MainWindow.DiagramsWindow.isHidden()
                self.MainWindow.DiagramsWindow.hide()

        else:
            dlg = ErrorDialog("An error occurred while fetching data from " +
                              res.url().toString() + ".")

            dlg.exec()
