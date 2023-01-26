
def onCombo(combo1, combo2, oneEdit, twoEdit):
    """
    This function is called when the user changes the value of the combo boxes.
    Params:
        combo1 (QComboBox) - the first combo box
        combo2 (QComboBox) - the second combo box
        oneEdit (QLineEdit) - the first line edit
        twoEdit (QLineEdit) - the second line edit
    """
    if oneEdit.text():
        if combo1.currentText() == "Celsius":
            if combo2.currentText() == "Celsius":
                twoEdit.setText(oneEdit.text())
            elif combo2.currentText() == "Fahrenheit":
                twoEdit.setText(str(round(float(oneEdit.text().replace(",", ".")) * (9/5) + 32, 5)).replace(".", ","))
            elif combo2.currentText() == "Kelvin":
                twoEdit.setText(str(round(float(oneEdit.text().replace(",", ".")) + 273.15, 5)).replace(".", ","))

        elif combo1.currentText() == "Fahrenheit":
            if combo2.currentText() == "Celsius":
                twoEdit.setText(str(round((float(oneEdit.text().replace(",", ".")) - 32) * (5/9), 5)).replace(".", ","))
            elif combo2.currentText() == "Fahrenheit":
                twoEdit.setText(oneEdit.text())
            elif combo2.currentText() == "Kelvin":
                twoEdit.setText(str(round((float(oneEdit.text().replace(",", ".")) + 459.67) * (5/9), 5)).replace(".", ","))

        elif combo1.currentText() == "Kelvin":
            if combo2.currentText() == "Celsius":
                twoEdit.setText(str(round(float(oneEdit.text().replace(",", ".")) - 273.15, 5)).replace(".", ","))
            elif combo2.currentText() == "Fahrenheit":
                twoEdit.setText(str(round(float(oneEdit.text().replace(",", ".")) * (9/5) - 459.67, 5)).replace(".", ","))
            elif combo2.currentText() == "Kelvin":
                twoEdit.setText(oneEdit.text())

def onEdit1(combo1, combo2, oneEdit, twoEdit):
    """
    This function is called when the user changes the value of the first line edit.
    Params:
        combo1 (QComboBox) - the first combo box
        combo2 (QComboBox) - the second combo box
        oneEdit (QLineEdit) - the first line edit
        twoEdit (QLineEdit) - the second line edit
    """
    if oneEdit.text() and oneEdit.text() != ",":
        if combo1.currentText() == "Celsius":
            if combo2.currentText() == "Celsius":
                twoEdit.setText(oneEdit.text())
            elif combo2.currentText() == "Fahrenheit":
                twoEdit.setText(str(round(float(oneEdit.text().replace(",", ".")) * (9/5) + 32, 5)).replace(".", ","))
            elif combo2.currentText() == "Kelvin":
                twoEdit.setText(str(round(float(oneEdit.text().replace(",", ".")) + 273.15, 5)).replace(".", ","))

        elif combo1.currentText() == "Fahrenheit":
            if combo2.currentText() == "Celsius":
                twoEdit.setText(str(round((float(oneEdit.text().replace(",", ".")) - 32) * (5/9), 5)).replace(".", ","))
            elif combo2.currentText() == "Fahrenheit":
                twoEdit.setText(oneEdit.text())
            elif combo2.currentText() == "Kelvin":
                twoEdit.setText(str(round((float(oneEdit.text().replace(",", ".")) + 459.67) * (5/9), 5)).replace(".", ","))

        elif combo1.currentText() == "Kelvin":
            if combo2.currentText() == "Celsius":
                twoEdit.setText(str(round(float(oneEdit.text().replace(",", ".")) - 273.15, 5)).replace(".", ","))
            elif combo2.currentText() == "Fahrenheit":
                twoEdit.setText(str(round(float(oneEdit.text().replace(",", ".")) * (9/5) - 459.67, 5)).replace(".", ","))
            elif combo2.currentText() == "Kelvin":
                twoEdit.setText(oneEdit.text())
    else:
        twoEdit.clear()

def onEdit2(combo1, combo2, oneEdit, twoEdit):
    """
    This function is called when the user changes the value of the second line edit.
    Params:
        combo1 (QComboBox) - the first combo box
        combo2 (QComboBox) - the second combo box
        oneEdit (QLineEdit) - the first line edit
        twoEdit (QLineEdit) - the second line edit
    """
    if twoEdit.text() and twoEdit.text() != ",":
        if combo2.currentText() == "Celsius":
            if combo1.currentText() == "Celsius":
                oneEdit.setText(twoEdit.text())
            elif combo1.currentText() == "Fahrenheit":
                oneEdit.setText(str(round(float(twoEdit.text().replace(",", ".")) * (9/5) + 32, 5)).replace(".", ","))
            elif combo1.currentText() == "Kelvin":
                oneEdit.setText(str(round(float(twoEdit.text().replace(",", ".")) + 273.15, 5)).replace(".", ","))

        elif combo2.currentText() == "Fahrenheit":
            if combo1.currentText() == "Celsius":
                oneEdit.setText(str(round((float(twoEdit.text().replace(",", ".")) - 32) * (5/9), 5)).replace(".", ","))
            elif combo1.currentText() == "Fahrenheit":
                oneEdit.setText(twoEdit.text())
            elif combo1.currentText() == "Kelvin":
                oneEdit.setText(str(round((float(twoEdit.text().replace(",", ".")) + 459.67) * (5/9), 5)).replace(".", ","))

        elif combo2.currentText() == "Kelvin":
            if combo1.currentText() == "Celsius":
                oneEdit.setText(str(round(float(twoEdit.text().replace(",", ".")) - 273.15, 5)).replace(".", ","))
            elif combo1.currentText() == "Fahrenheit":
                oneEdit.setText(str(round(float(twoEdit.text().replace(",", ".")) * (9/5) - 459.67, 5)).replace(".", ","))
            elif combo1.currentText() == "Kelvin":
                oneEdit.setText(twoEdit.text())
    else:
        oneEdit.clear()