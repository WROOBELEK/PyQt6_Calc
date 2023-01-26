
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon

import ui.degradUI


class DegRadCalc(QWidget):
    def __init__(self):
        """
        Initializes the DegRadCalc window (QWidget) and sets the window title, icon, size and calls the degradUI function to create the UI.
        """
        super().__init__()
        self.setWindowTitle("Deg Rad")
        self.setWindowIcon(QIcon("ico/calculator.ico"))
        self.setFixedSize(250, 70)
        ui.degradUI.UI(self)

