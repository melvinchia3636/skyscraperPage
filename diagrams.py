from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):

        Form.resize(926, 878)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)

        self.Title1Label = QtWidgets.QLabel(parent=Form)
        self.Title2Label = QtWidgets.QLabel(parent=Form)
        self.scrollArea = QtWidgets.QScrollArea(parent=Form)
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.label_21 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_22 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.pushButton_10 = QtWidgets.QPushButton(
            parent=self.scrollAreaWidgetContents)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.label_15 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_16 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.pushButton_7 = QtWidgets.QPushButton(
            parent=self.scrollAreaWidgetContents)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.label_17 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_18 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.pushButton_8 = QtWidgets.QPushButton(
            parent=self.scrollAreaWidgetContents)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalFrame = QtWidgets.QFrame(
            parent=self.scrollAreaWidgetContents)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalFrame)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalFrame)
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalFrame)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.label_19 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_20 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.pushButton_9 = QtWidgets.QPushButton(
            parent=self.scrollAreaWidgetContents)
        self.label_27 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_28 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.pushButton_13 = QtWidgets.QPushButton(
            parent=self.scrollAreaWidgetContents)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.label_29 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_30 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.pushButton_14 = QtWidgets.QPushButton(
            parent=self.scrollAreaWidgetContents)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.pushButton_11 = QtWidgets.QPushButton(
            parent=self.scrollAreaWidgetContents)
        self.label_23 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Title1Label.setFont(font)
        self.Title1Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Title1Label)
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setBold(False)
        font.setWeight(50)
        self.Title2Label.setFont(font)
        self.Title2Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Title2Label)
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 900, 853))

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)

        self.verticalLayout_11.addWidget(self.label_21)
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap(":/image/163_2362860507.png"))
        self.label_22.setScaledContents(True)
        self.verticalLayout_11.addWidget(self.label_22)

        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(13)
        self.pushButton_10.setFont(font)

        self.verticalLayout_11.addWidget(self.pushButton_10)
        self.gridLayout.addLayout(self.verticalLayout_11, 1, 1, 1, 1)

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)

        self.verticalLayout_8.addWidget(self.label_15)
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/image/1373_2711838088.png"))
        self.label_16.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_16)

        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(13)
        self.pushButton_7.setFont(font)

        self.verticalLayout_8.addWidget(self.pushButton_7)
        self.gridLayout.addLayout(self.verticalLayout_8, 1, 0, 1, 1)

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)

        self.verticalLayout_9.addWidget(self.label_17)
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap(
            ":/image/world_skyscraper_construction_2330944475.png"))
        self.label_18.setScaledContents(True)

        self.verticalLayout_9.addWidget(self.label_18)

        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(13)
        self.pushButton_8.setFont(font)

        self.verticalLayout_9.addWidget(self.pushButton_8)
        self.gridLayout.addLayout(self.verticalLayout_9, 0, 1, 1, 1)

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(
            ":/image/world_skyscrapers_current_2330813403.png"))
        self.label_4.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_4)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(13)
        self.pushButton.setFont(font)

        self.verticalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addWidget(self.verticalFrame, 0, 0, 1, 1)

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)

        self.verticalLayout_10.addWidget(self.label_19)
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap(
            ":/image/world_skyscrapers_future_2331075547.png"))
        self.label_20.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.label_20)

        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(13)
        self.pushButton_9.setFont(font)

        self.verticalLayout_10.addWidget(self.pushButton_9)
        self.gridLayout.addLayout(self.verticalLayout_10, 0, 2, 1, 1)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)

        self.verticalLayout_14.addWidget(self.label_27)
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap(":/image/4_1842701151.png"))
        self.label_28.setScaledContents(True)

        self.verticalLayout_14.addWidget(self.label_28)

        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(13)
        self.pushButton_13.setFont(font)

        self.verticalLayout_14.addWidget(self.pushButton_13)
        self.gridLayout.addLayout(self.verticalLayout_14, 2, 0, 1, 1)

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)

        self.verticalLayout_15.addWidget(self.label_29)
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap(":/image/807_305618969.png"))
        self.label_30.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.label_30)

        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(13)
        self.pushButton_14.setFont(font)

        self.verticalLayout_15.addWidget(self.pushButton_14)
        self.gridLayout.addLayout(self.verticalLayout_15, 2, 1, 1, 1)

        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)

        self.verticalLayout_12.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap(":/image/24_1023566853.png"))
        self.label_24.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.label_24)

        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(13)
        self.pushButton_11.setFont(font)

        self.verticalLayout_12.addWidget(self.pushButton_11)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_12.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_12, 1, 2, 2, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Skyscraper Diagrams"))
        self.Title1Label.setText(_translate("Form", "Skyscraper Diagrams"))
        self.Title2Label.setText(_translate(
            "Form", "710+ cities, 60,000+ structures, 77,000+ drawings"))
        self.label_21.setText(_translate("Form", "Las Vegas, United States"))
        self.pushButton_10.setText(_translate("Form", "View"))
        self.label_15.setText(_translate("Form", "Ürümqi, China"))
        self.pushButton_7.setText(_translate("Form", "View"))
        self.label_17.setText(_translate(
            "Form", "Word Skyscrapers Construction"))
        self.pushButton_8.setText(_translate("Form", "View"))
        self.label_3.setText(_translate("Form", "Word Skyscrapers 2023"))
        self.pushButton.setText(_translate("Form", "View"))
        self.label_19.setText(_translate("Form", "Word Skyscrapers 2028"))
        self.pushButton_9.setText(_translate("Form", "View"))
        self.label_27.setText(_translate("Form", "Chicago, United States"))
        self.pushButton_13.setText(_translate("Form", "View"))
        self.label_29.setText(_translate("Form", "London, United Kingdom"))
        self.pushButton_14.setText(_translate("Form", "View"))
        self.label_23.setText(_translate("Form", "Shenzhen, China"))
        self.pushButton_11.setText(_translate("Form", "View"))
