
from PyQt6.QtWidgets import QFormLayout, QLineEdit, QLabel
from PyQt6.QtGui import QIntValidator

import functions.programmerFunctions as pf


def UI(self):
    """
    Creates the UI for the ProgrammerCalc window (QWidget).
    """

    # Widgets ####################################################################################################

    self.decLabel = QLabel("DEC: ")
    self.decEdit = QLineEdit()
    self.decEdit.setValidator(QIntValidator())
    self.decEdit.textEdited.connect(lambda: pf.onDecEdit(self.decEdit, self.hexEdit, self.octEdit, self.binEdit))

    self.hexLabel = QLabel("HEX: ")
    self.hexEdit = QLineEdit()
    self.hexEdit.setReadOnly(True)

    self.octLabel = QLabel("OCT: ")
    self.octEdit = QLineEdit()
    self.octEdit.setReadOnly(True)

    self.binLabel = QLabel("BIN: ")
    self.binEdit = QLineEdit()
    self.binEdit.setReadOnly(True)

    # Layouts ####################################################################################################

    layout = QFormLayout()
    layout.addRow(self.decLabel, self.decEdit)
    layout.addRow(self.hexLabel, self.hexEdit)
    layout.addRow(self.octLabel, self.octEdit)
    layout.addRow(self.binLabel, self.binEdit)
    self.setLayout(layout)