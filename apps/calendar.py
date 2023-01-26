
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon

import ui.calendarUI


class CalendarCalc(QWidget):
    def __init__(self):
        """
        Initializes the CalendarCalc window (QWidget) and sets the window title, icon, size and calls the calendarUI function to create the UI.
        """
        super().__init__()
        self.setWindowTitle("Calendar")
        self.setWindowIcon(QIcon("ico/calculator.ico"))
        self.setFixedSize(250, 93)
        ui.calendarUI.UI(self)

