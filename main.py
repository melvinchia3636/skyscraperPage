from PyQt6 import QtWidgets
from mainWindow import Ui_MainWindow
from diagrams import Ui_Diagrams
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.WelcomeWindow = Ui_MainWindow()
        self.DiagramsWindow = DiagramsWindow(self)

        self.WelcomeWindow.setupUi(self)


class DiagramsWindow(QtWidgets.QWidget):
    def __init__(self, MainWindow):
        super().__init__()
        self.parent = MainWindow
        self.UiDiagrams = Ui_Diagrams()
        self.UiDiagrams.setupUi(self)

    def closeEvent(self, event):
        self.parent.show()
        event.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
