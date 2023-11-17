from PyQt6 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        QtCore.QDir.addSearchPath('welcome', 'assets/welcome/')

        self.initializeComponents()
        self.setupComponents(MainWindow)
        self.placeComponents()

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menuDiagrams = QtWidgets.QMenu(self.menubar)
        self.menuDatabase = QtWidgets.QMenu(self.menubar)

        self.menuBrowse = QtWidgets.QMenu(self.menuDatabase)
        MainWindow.setMenuBar(self.menubar)
        self.actionSkyscraper_Diagrams = QtGui.QAction(MainWindow)
        self.actionBrowse_by_Cities = QtGui.QAction(MainWindow)
        self.actionDiagram_Search = QtGui.QAction(MainWindow)
        self.actionDiagram_Statistics = QtGui.QAction(MainWindow)
        self.actionSearch = QtGui.QAction(MainWindow)
        self.actionMetropolitan_Areas = QtGui.QAction(MainWindow)
        self.actionBy_Metropolitan_Areas = QtGui.QAction(MainWindow)
        self.actionNewest_Entries = QtGui.QAction(MainWindow)
        self.actionBy_Countries = QtGui.QAction(MainWindow)
        self.actionBy_Cities = QtGui.QAction(MainWindow)
        self.actionBy_Metropolitan_Areas_2 = QtGui.QAction(MainWindow)
        self.actionBy_Cities_2 = QtGui.QAction(MainWindow)
        self.actionBy_Countries_2 = QtGui.QAction(MainWindow)
        self.actionBy_Continents = QtGui.QAction(MainWindow)
        self.actionStatistics = QtGui.QAction(MainWindow)
        self.actionInteractive_Maps = QtGui.QAction(MainWindow)
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

        self.addText(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def initializeComponents(self):
        self.MainWrapper = QtWidgets.QWidget(MainWindow)
        self.MainContainer = QtWidgets.QVBoxLayout(self.MainWrapper)
        self.CoverImage = QtWidgets.QLabel(self.MainWrapper)
        self.Title1Label = QtWidgets.QLabel(self.MainWrapper)
        self.Title2Label = QtWidgets.QLabel(self.MainWrapper)
        self.ButtonWrapper = QtWidgets.QHBoxLayout()
        self.ButtonContainer = QtWidgets.QVBoxLayout()
        self.ToDiagramButton = QtWidgets.QPushButton(self.MainWrapper)
        self.ToDatabaseButton = QtWidgets.QPushButton(self.MainWrapper)
        self.QuitButton = QtWidgets.QPushButton(self.MainWrapper)
        self.ButtonWrapperHorizontalSpacerLeft = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.ButtonWrapperHorizontalSpacerRight = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.SpacerBetweenButtonsAndTitle = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)

    def setupComponents(self, MainWindow):
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
        self.QuitButton.setFont(font)

        self.ToDiagramButton.setMinimumHeight(60)
        self.ToDatabaseButton.setMinimumHeight(60)
        self.QuitButton.setMinimumHeight(60)

        self.ToDatabaseButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ToDiagramButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.QuitButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 600)
        MainWindow.setCentralWidget(self.MainWrapper)
        centerPoint = QtGui.QScreen.availableGeometry(
            QtGui.QGuiApplication.primaryScreen()).center()
        frame = MainWindow.frameGeometry()
        frame.moveCenter(centerPoint)
        self.MainContainer.setContentsMargins(-1, -1, -1, 20)

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
        self.ButtonContainer.addWidget(self.QuitButton)

    def addText(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title1Label.setText(_translate("MainWindow", "A GUI Client for"))
        self.Title2Label.setText(_translate(
            "MainWindow", "SkyscraperPage.com"))
        self.ToDiagramButton.setText(_translate("MainWindow", "Diagrams"))
        self.ToDatabaseButton.setText(_translate("MainWindow", "Database"))
        self.QuitButton.setText(_translate("MainWindow", "Quit"))
        self.menuDiagrams.setTitle(_translate("MainWindow", "Diagrams"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.menuBrowse.setTitle(_translate("MainWindow", "Browse"))
        self.actionSkyscraper_Diagrams.setText(
            _translate("MainWindow", "Featured"))
        self.actionBrowse_by_Cities.setText(
            _translate("MainWindow", "By Cities"))
        self.actionDiagram_Search.setText(_translate("MainWindow", "Search"))
        self.actionDiagram_Statistics.setText(
            _translate("MainWindow", "Statistics"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))
        self.actionMetropolitan_Areas.setText(
            _translate("MainWindow", "By Continents"))
        self.actionBy_Metropolitan_Areas.setText(
            _translate("MainWindow", "By Metropolitan Areas"))
        self.actionNewest_Entries.setText(
            _translate("MainWindow", "Newest Entries"))
        self.actionBy_Countries.setText(
            _translate("MainWindow", "By Countries"))
        self.actionBy_Cities.setText(_translate("MainWindow", "By Cities"))
        self.actionBy_Metropolitan_Areas_2.setText(
            _translate("MainWindow", "By Metropolitan Areas"))
        self.actionBy_Cities_2.setText(_translate("MainWindow", "By Cities"))
        self.actionBy_Countries_2.setText(
            _translate("MainWindow", "By Countries"))
        self.actionBy_Continents.setText(
            _translate("MainWindow", "By Continents"))
        self.actionStatistics.setText(_translate("MainWindow", "Statistics"))
        self.actionInteractive_Maps.setText(
            _translate("MainWindow", "Interactive Maps"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
