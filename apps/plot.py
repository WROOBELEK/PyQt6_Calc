
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon

import ui.plotUI


class PlotCalc(QWidget):
    def __init__(self):
        """
        Initializes the PlotCalc window (QWidget) and sets the window title, icon, size and calls the plotUI function to create the UI.
        """
        super().__init__()
        self.setWindowTitle("Plot")
        self.setWindowIcon(QIcon("ico/calculator.ico"))
        ui.plotUI.UI(self)