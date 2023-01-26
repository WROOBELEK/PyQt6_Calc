
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon

import ui.programmerUI


class ProgrammerCalc(QWidget):
    def __init__(self):
        """
        Initializes the ProgrammerCalc window (QWidget) and sets the window title, icon, size and calls the programmerUI function to create the UI.
        """
        super().__init__()
        self.setWindowTitle("Programmer")
        self.setWindowIcon(QIcon("ico/calculator.ico"))
        self.setFixedSize(250, 130)
        ui.programmerUI.UI(self)

