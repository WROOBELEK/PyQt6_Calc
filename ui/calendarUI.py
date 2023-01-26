
from PyQt6.QtWidgets import QVBoxLayout, QDateEdit, QLabel

import functions.calendarFunctions as cf


def UI(self):
    """
    Creates the UI for the CalendarCalc window (QWidget).
    """

    # Widgets ####################################################################################################

    self.calendar1 = QDateEdit(calendarPopup = True)
    self.calendar2 = QDateEdit(calendarPopup = True)
    self.label = QLabel("Difference: 0 years 0 months and 0 days")
    self.calendar1.dateChanged.connect(lambda: cf.calcudateDays(self.calendar1, self.calendar2, self.label))
    self.calendar2.dateChanged.connect(lambda: cf.calcudateDays(self.calendar1, self.calendar2, self.label))

    # Layouts ####################################################################################################

    layout = QVBoxLayout()
    layout.addWidget(self.calendar1)
    layout.addWidget(self.calendar2)
    layout.addWidget(self.label)
    self.setLayout(layout)