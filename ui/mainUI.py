
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QAction

import functions.mainFunctions as mf


def UI(self):
    """
    Creates the UI for the main window.
    """

    # Widgets ####################################################################################################

    self.number1Screen = QLineEdit()
    self.number1Screen.setMaxLength(15)
    self.number1Screen.setReadOnly(True)
    self.number1Screen.setAlignment(Qt.AlignmentFlag.AlignRight)

    self.operationScreen = QLineEdit()
    self.operationScreen.setMaxLength(3)
    self.operationScreen.setReadOnly(True)
    self.operationScreen.setMaximumWidth(30)
    self.operationScreen.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.number2Screen = QLineEdit()
    self.number2Screen.setMaxLength(15)
    self.number2Screen.setReadOnly(True)
    self.number2Screen.setAlignment(Qt.AlignmentFlag.AlignRight)

    self.resultScreen = QLineEdit()
    self.resultScreen.setMaxLength(10)
    self.resultScreen.setReadOnly(True)
    self.resultScreen.setAlignment(Qt.AlignmentFlag.AlignRight)
    
    self.buttonZero = QPushButton("0")
    self.buttonZero.setMinimumHeight(50)
    self.buttonOne = QPushButton("1")
    self.buttonOne.setMinimumHeight(50)
    self.buttonTwo = QPushButton("2")
    self.buttonTwo.setMinimumHeight(50)
    self.buttonThree = QPushButton("3")
    self.buttonThree.setMinimumHeight(50)
    self.buttonFour = QPushButton("4")
    self.buttonFour.setMinimumHeight(50)
    self.buttonFive = QPushButton("5")
    self.buttonFive.setMinimumHeight(50)
    self.buttonSix = QPushButton("6")
    self.buttonSix.setMinimumHeight(50)
    self.buttonSeven = QPushButton("7")
    self.buttonSeven.setMinimumHeight(50)
    self.buttonEight = QPushButton("8")
    self.buttonEight.setMinimumHeight(50)
    self.buttonNine = QPushButton("9")
    self.buttonNine.setMinimumHeight(50)
    
    self.buttonAdd = QPushButton("+")
    self.buttonAdd.setMinimumHeight(50)
    self.buttonSubtract = QPushButton("-")
    self.buttonSubtract.setMinimumHeight(50)
    self.buttonMultiply = QPushButton("×")
    self.buttonMultiply.setMinimumHeight(50)
    self.buttonDivide = QPushButton("/")
    self.buttonDivide.setMinimumHeight(50)

    self.buttonResult = QPushButton("=")
    self.buttonResult.setMinimumHeight(50)

    self.buttonCE = QPushButton("C/CE")
    self.buttonCE.setMinimumHeight(50)
    self.buttonBackspace = QPushButton("⌫")
    self.buttonBackspace.setMinimumHeight(50)

    self.buttonModulo = QPushButton("%")
    self.buttonModulo.setMinimumHeight(50)
    self.buttonInvert = QPushButton("+/-")
    self.buttonInvert.setMinimumHeight(50)
    self.buttonComma = QPushButton(".")
    self.buttonComma.setMinimumHeight(50)
    self.buttonPower = QPushButton("x^y")
    self.buttonPower.setMinimumHeight(50)
    self.buttonRoot = QPushButton("√")
    self.buttonRoot.setMinimumHeight(50)
    self.buttonOneBy = QPushButton("1/x")
    self.buttonOneBy.setMinimumHeight(50)

    self.buttonOne.clicked.connect(lambda: mf.buttonOne(self))
    self.buttonTwo.clicked.connect(lambda: mf.buttonTwo(self))
    self.buttonThree.clicked.connect(lambda: mf.buttonThree(self))
    self.buttonFour.clicked.connect(lambda: mf.buttonFour(self))
    self.buttonFive.clicked.connect(lambda: mf.buttonFive(self))
    self.buttonSix.clicked.connect(lambda: mf.buttonSix(self))
    self.buttonSeven.clicked.connect(lambda: mf.buttonSeven(self))
    self.buttonEight.clicked.connect(lambda: mf.buttonEight(self))
    self.buttonNine.clicked.connect(lambda: mf.buttonNine(self))
    self.buttonZero.clicked.connect(lambda: mf.buttonZero(self))

    self.buttonAdd.clicked.connect(lambda: mf.buttonAdd(self))
    self.buttonSubtract.clicked.connect(lambda: mf.buttonSubtract(self))
    self.buttonMultiply.clicked.connect(lambda: mf.buttonMultiply(self))
    self.buttonDivide.clicked.connect(lambda: mf.buttonDivide(self))
    self.buttonPower.clicked.connect(lambda: mf.buttonPower(self))
    self.buttonRoot.clicked.connect(lambda: mf.buttonRoot(self))
    self.buttonOneBy.clicked.connect(lambda: mf.buttonOneBy(self))
    self.buttonModulo.clicked.connect(lambda: mf.buttonModulo(self))
    self.buttonComma.clicked.connect(lambda: mf.buttonComma(self))
    self.buttonInvert.clicked.connect(lambda: mf.buttonInvert(self))

    self.buttonCE.clicked.connect(lambda: mf.buttonCE(self))
    self.buttonBackspace.clicked.connect(lambda: mf.buttonBackspace(self))

    self.buttonResult.clicked.connect(lambda: mf.buttonResult(self))

    # Layouts ####################################################################################################
    
    self.mainWidget = QWidget()
    mainLayout = QVBoxLayout()
    screenLayout = QHBoxLayout()
    buttonLayout = QGridLayout()


    screenLayout.addWidget(self.number1Screen)
    
    self.operationScreen.setAlignment(Qt.AlignmentFlag.AlignCenter)

    screenLayout.addWidget(self.operationScreen)
    

    screenLayout.addWidget(self.number2Screen)
    
    
    mainLayout.addLayout(screenLayout)

    mainLayout.addWidget(self.resultScreen)
    self.resultScreen.setMaxLength(20)
    self.resultScreen.setReadOnly(True)
    self.resultScreen.setMinimumHeight(50)
    self.resultScreen.setAlignment(Qt.AlignmentFlag.AlignRight)

    buttonLayout.addWidget(self.buttonModulo, 0, 0)
    buttonLayout.addWidget(self.buttonCE, 0, 1)
    buttonLayout.addWidget(self.buttonBackspace, 0, 2, 1, 2)
    buttonLayout.addWidget(self.buttonOneBy, 1, 0)
    buttonLayout.addWidget(self.buttonPower, 1, 1)
    buttonLayout.addWidget(self.buttonRoot, 1, 2)
    buttonLayout.addWidget(self.buttonDivide, 1, 3)
    buttonLayout.addWidget(self.buttonSeven, 2, 0)
    buttonLayout.addWidget(self.buttonEight, 2, 1)
    buttonLayout.addWidget(self.buttonNine, 2, 2)
    buttonLayout.addWidget(self.buttonMultiply, 2, 3)
    buttonLayout.addWidget(self.buttonFour, 3, 0)
    buttonLayout.addWidget(self.buttonFive, 3, 1)
    buttonLayout.addWidget(self.buttonSix, 3, 2)
    buttonLayout.addWidget(self.buttonSubtract, 3, 3)
    buttonLayout.addWidget(self.buttonOne, 4, 0)
    buttonLayout.addWidget(self.buttonTwo, 4, 1)
    buttonLayout.addWidget(self.buttonThree, 4, 2)
    buttonLayout.addWidget(self.buttonAdd, 4, 3)
    buttonLayout.addWidget(self.buttonInvert, 5, 0)
    buttonLayout.addWidget(self.buttonZero, 5, 1)
    buttonLayout.addWidget(self.buttonComma, 5, 2)
    buttonLayout.addWidget(self.buttonResult, 5, 3)
    
    buttonLayout.setRowStretch(0,0)
    buttonLayout.setColumnStretch(0,0)

    mainLayout.addLayout(buttonLayout)

    self.mainWidget.setLayout(mainLayout)

    self.setCentralWidget(self.mainWidget)

    # Menu Bar ####################################################################################################

    menu = self.menuBar()

    menu_button_calculator_programmer = QAction(QIcon("ico/calculator.ico"), "Programmer", self)
    menu_button_calculator_calendar = QAction(QIcon("ico/calculator.ico"), "Calendar", self)

    menu_button_converter_degrad = QAction(QIcon("ico/calculator.ico"), "Degrees - Radians", self)
    menu_button_converter_temperature = QAction(QIcon("ico/calculator.ico"), "Temperature", self)

    menu_button_plots_plot = QAction(QIcon("ico/calculator.ico"), "Plot", self)
    

    menu_calculator = menu.addMenu("Calculators")
    menu_calculator.addAction(menu_button_calculator_programmer)
    menu_calculator.addAction(menu_button_calculator_calendar)

    menu_converter = menu.addMenu("Converters")
    menu_converter.addAction(menu_button_converter_temperature)
    menu_converter.addAction(menu_button_converter_degrad)

    menu_plots = menu.addMenu("Plot")
    menu_plots.addAction(menu_button_plots_plot)

    menu_button_calculator_programmer.triggered.connect(lambda: mf.openProgrammerCalc(self))
    menu_button_calculator_calendar.triggered.connect(lambda: mf.openCalendarCalc(self))

    menu_button_converter_temperature.triggered.connect(lambda: mf.openTemperatureCalc(self))
    menu_button_converter_degrad.triggered.connect(lambda: mf.openDegRadCalc(self))

    menu_button_plots_plot.triggered.connect(lambda: mf.openPlotCalc(self))

    # Styles ####################################################################################################

    self.setStyleSheet('''QLineEdit { background-color: rgb(104, 121, 89); color: rgb(0, 0, 0); font-weight: bold; font-size: 20px; border: 1px solid gray; }
                        QPushButton { color: rgb(0, 0, 0); font-weight: bold; font-size: 20px; border: 1px solid gray; }
                        QPushButton::hover { color: rgb(0, 0, 0); font-weight: bold; font-size: 20px; border: 1px solid blue; }''')

    self.buttonSeven.setStyleSheet("background-color: rgb(143, 240, 164);")
    self.buttonEight.setStyleSheet("background-color: rgb(143, 240, 164);")
    self.buttonNine.setStyleSheet("background-color: rgb(143, 240, 164);")
    self.buttonFour.setStyleSheet("background-color: rgb(143, 240, 164);")
    self.buttonFive.setStyleSheet("background-color: rgb(143, 240, 164);")
    self.buttonSix.setStyleSheet("background-color: rgb(143, 240, 164);")
    self.buttonOne.setStyleSheet("background-color: rgb(143, 240, 164);")
    self.buttonTwo.setStyleSheet("background-color: rgb(143, 240, 164);")
    self.buttonThree.setStyleSheet("background-color: rgb(143, 240, 164);")
    self.buttonZero.setStyleSheet("background-color: rgb(143, 240, 164);")

    self.resultScreen.setStyleSheet("font-size: 50px;")