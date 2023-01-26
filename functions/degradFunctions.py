
import math

def onDegreeEdit(degreeEdit, radianEdit):
    """
    Converts degrees to radians and vice versa.
    Params:
        degreeEdit (QLineEdit) - used to get the degrees
        radianEdit (QLineEdit) - used to display the radians
    """
    if degreeEdit.text() and degreeEdit.text() != ",":
        rad = str(round(math.radians(float(degreeEdit.text().replace(",", "."))), 5))
        radianEdit.setText(rad.replace(".", ","))
    else:
        radianEdit.clear()

def onRadianEdit(radianEdit, degreeEdit):
    """
    Converts radians to degrees and vice versa.
    Params:
        radianEdit (QLineEdit) - used to get the radians
        degreeEdit (QLineEdit) - used to display the degrees
    """
    if radianEdit.text() and radianEdit.text() != ",":
        deg = str(round(math.degrees(float(radianEdit.text().replace(",", "."))), 5))
        degreeEdit.setText(deg.replace(".", ","))
    else:
        degreeEdit.clear()