

def onDecEdit(decEdit, hexEdit, octEdit, binEdit):
    """
    Converts decimal to hexadecimal, octal and binary.
    Params:
        decEdit (QLineEdit) - used to get the decimal
        hexEdit (QLineEdit) - used to display the hexadecimal
        octEdit (QLineEdit) - used to display the octal
        binEdit (QLineEdit) - used to display the binary
    """
    if  decEdit.text():
        decval = int(decEdit.text())
        hexEdit.setText(hex(decval).replace("0x", ""))
        octEdit.setText(oct(decval).replace("0o", ""))
        binEdit.setText(bin(decval).replace("0b", ""))
    else:
        hexEdit.clear()
        octEdit.clear()
        binEdit.clear()