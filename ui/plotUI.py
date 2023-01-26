
from PyQt6.QtWidgets import QLineEdit, QVBoxLayout, QGridLayout, QPushButton, QCheckBox
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT

import functions.plotFunctions as pf


def UI(self):
    """
    Creates the UI for the PlotCalc window (QWidget).
    """

    # Widgets ####################################################################################################

    self.functionInput = QLineEdit()
    self.functionInput.setPlaceholderText("Enter a mathematical expression")
    self.functionInput.setText('x^3')

    self.startXInput = QLineEdit()
    self.startXInput.setPlaceholderText("Enter horizontal start point")
    self.startXInput.setText('-10')

    self.endXInput = QLineEdit()
    self.endXInput.setPlaceholderText("Enter horizontal section end point")
    self.endXInput.setText('10')

    self.startYInput = QLineEdit()
    self.startYInput.setPlaceholderText("Enter vertical section start point")
    self.startYInput.setText('-10')

    self.endYInput = QLineEdit()
    self.endYInput.setPlaceholderText("Enter vertical section end point")
    self.endYInput.setText('10')

    self.derivative1 = QCheckBox("First derivative")
    self.derivative1.setChecked(True)
    self.derivative2 = QCheckBox("Second derivative")
    self.derivative2.setChecked(True)


    pc = pf.PlotCanvas()
    self.toolbar = NavigationToolbar2QT(pc)

    self.savePlotButton = QPushButton("Save Plot")
    self.savePlotButton.clicked.connect(lambda: pc.savePlot())

    self.functionInput.textEdited.connect(lambda: pc.updatePlot(self.functionInput.text(), self.startXInput.text(), self.endXInput.text(), self.startYInput.text(), self.endYInput.text(), self.derivative1.isChecked(), self.derivative2.isChecked()))

    self.endXInput.textEdited.connect(lambda: pc.updatePlot(self.functionInput.text(), self.startXInput.text(), self.endXInput.text(), self.startYInput.text(), self.endYInput.text(), self.derivative1.isChecked(), self.derivative2.isChecked()))
    self.startXInput.textEdited.connect(lambda: pc.updatePlot(self.functionInput.text(), self.startXInput.text(), self.endXInput.text(), self.startYInput.text(), self.endYInput.text(), self.derivative1.isChecked(), self.derivative2.isChecked()))
    self.endYInput.textEdited.connect(lambda: pc.updatePlot(self.functionInput.text(), self.startXInput.text(), self.endXInput.text(), self.startYInput.text(), self.endYInput.text(), self.derivative1.isChecked(), self.derivative2.isChecked()))
    self.startYInput.textEdited.connect(lambda: pc.updatePlot(self.functionInput.text(), self.startXInput.text(), self.endXInput.text(), self.startYInput.text(), self.endYInput.text(), self.derivative1.isChecked(), self.derivative2.isChecked()))
    self.derivative1.stateChanged.connect(lambda: pc.updatePlot(self.functionInput.text(), self.startXInput.text(), self.endXInput.text(), self.startYInput.text(), self.endYInput.text(), self.derivative1.isChecked(), self.derivative2.isChecked()))
    self.derivative2.stateChanged.connect(lambda: pc.updatePlot(self.functionInput.text(), self.startXInput.text(), self.endXInput.text(), self.startYInput.text(), self.endYInput.text(), self.derivative1.isChecked(), self.derivative2.isChecked()))

    pc.updatePlot(self.functionInput.text(), self.startXInput.text(), self.endXInput.text(), self.startYInput.text(), self.endYInput.text(), self.derivative1.isChecked(), self.derivative2.isChecked())

    # Layouts ####################################################################################################

    layout = QVBoxLayout()
    inputLayout = QGridLayout()

    layout.addWidget(self.toolbar)
    inputLayout.addWidget(self.functionInput, 0, 0)
    inputLayout.addWidget(self.derivative1, 0, 1)
    inputLayout.addWidget(self.endYInput, 0, 2)
    inputLayout.addWidget(self.derivative2, 0, 3)
    inputLayout.addWidget(self.savePlotButton, 1, 0)
    inputLayout.addWidget(self.startXInput, 1, 1)
    inputLayout.addWidget(self.startYInput, 1, 2)
    inputLayout.addWidget(self.endXInput, 1, 3)
    inputLayout.setColumnStretch(0, 2)
    inputLayout.setColumnStretch(1, 1)
    inputLayout.setColumnStretch(2, 1)
    inputLayout.setColumnStretch(3, 1)
    layout.addLayout(inputLayout)
    layout.addWidget(pc)

    self.setLayout(layout)

    # Styles ####################################################################################################

    self.savePlotButton.setStyleSheet("background-color: rgb(143, 240, 164);")
    self.derivative1.setStyleSheet("color: red;")
    self.derivative2.setStyleSheet("color: green;")