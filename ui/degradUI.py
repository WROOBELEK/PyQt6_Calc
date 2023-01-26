
from PyQt6.QtWidgets import QFormLayout, QLineEdit, QLabel
from PyQt6.QtGui import QDoubleValidator

import functions.degradFunctions as df


def UI(self):
    """
    Creates the UI for the DegRadCalc window (QWidget).
    """

    # Widgets ####################################################################################################

    self.degreeLabel = QLabel("Degrees: ")
    self.degreeEdit = QLineEdit()
    self.degreeEdit.setValidator(QDoubleValidator(9, 9, 5))

    self.radianLabel = QLabel("Radians: ")
    self.radianEdit = QLineEdit()
    self.radianEdit.setValidator(QDoubleValidator(9, 9, 5))

    self.degreeEdit.textEdited.connect(lambda: df.onDegreeEdit(self.degreeEdit, self.radianEdit))
    self.radianEdit.textEdited.connect(lambda: df.onRadianEdit(self.radianEdit, self.degreeEdit))

    # Layouts ####################################################################################################

    layout = QFormLayout()
    layout.addRow(self.degreeLabel, self.degreeEdit)
    layout.addRow(self.radianLabel, self.radianEdit)
    self.setLayout(layout)