
from PyQt6.QtWidgets import QFormLayout, QLineEdit, QComboBox
from PyQt6.QtGui import QDoubleValidator

import functions.temperatureFunctions as tf


def UI(self):
    """
    Creates the UI for the TemperatureCalc window (QWidget).
    """

    # Widgets ####################################################################################################

    self.combo1 = QComboBox()
    self.combo1.addItems(["Celsius", "Fahrenheit", "Kelvin"])
    self.combo2 = QComboBox()
    self.combo2.addItems(["Celsius", "Fahrenheit", "Kelvin"])
    self.combo2.setCurrentIndex(1)

    self.oneEdit = QLineEdit()
    self.oneEdit.setValidator(QDoubleValidator(9, 9, 5))

    self.twoEdit = QLineEdit()
    self.twoEdit.setValidator(QDoubleValidator(9, 9, 5))

    self.combo1.currentIndexChanged.connect(lambda: tf.onCombo(self.combo1, self.combo2, self.oneEdit, self.twoEdit))
    self.combo2.currentIndexChanged.connect(lambda: tf.onCombo(self.combo1, self.combo2, self.oneEdit, self.twoEdit))
    self.oneEdit.textEdited.connect(lambda: tf.onEdit1(self.combo1, self.combo2, self.oneEdit, self.twoEdit))
    self.twoEdit.textEdited.connect(lambda: tf.onEdit2(self.combo1, self.combo2, self.oneEdit, self.twoEdit))

    # Layouts ####################################################################################################
    
    layout = QFormLayout()
    layout.addRow(self.combo1, self.oneEdit)
    layout.addRow(self.combo2, self.twoEdit)
    self.setLayout(layout)
    