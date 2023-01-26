
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon

import ui.temperatureUI


class TemperatureCalc(QWidget):
    def __init__(self):
        """
        Initializes the TemperatureCalc window (QWidget) and sets the window title, icon, size and calls the temperatureUI function to create the UI.
        """
        super().__init__()
        self.setWindowTitle("Temperature")
        self.setWindowIcon(QIcon("ico/calculator.ico"))
        self.setFixedSize(250, 70)
        ui.temperatureUI.UI(self)