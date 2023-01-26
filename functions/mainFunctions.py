
import apps.programmer
import apps.calendar
import apps.temperature
import apps.degrad
import apps.plot

# Digits ####################################################################################################

def buttonZero(self):
    if not self.operationScreen.text():
        self.number1Screen.insert("0")
    elif self.operationScreen.text() and not self.resultScreen.text():
        self.number2Screen.insert("0")

def buttonOne(self):
    if not self.operationScreen.text():
        self.number1Screen.insert("1")
    elif self.operationScreen.text() and not self.resultScreen.text():
        self.number2Screen.insert("1")

def buttonTwo(self):
    if not self.operationScreen.text():
        self.number1Screen.insert("2")
    elif self.operationScreen.text() and not self.resultScreen.text():
        self.number2Screen.insert("2")

def buttonThree(self):
    if not self.operationScreen.text():
        self.number1Screen.insert("3")
    elif self.operationScreen.text() and not self.resultScreen.text():
        self.number2Screen.insert("3")

def buttonFour(self):
    if not self.operationScreen.text():
        self.number1Screen.insert("4")
    elif self.operationScreen.text() and not self.resultScreen.text():
        self.number2Screen.insert("4")

def buttonFive(self):
    if not self.operationScreen.text():
        self.number1Screen.insert("5")
    elif self.operationScreen.text() and not self.resultScreen.text():
        self.number2Screen.insert("5")

def buttonSix(self):
    if not self.operationScreen.text():
        self.number1Screen.insert("6")
    elif self.operationScreen.text() and not self.resultScreen.text():
        self.number2Screen.insert("6")

def buttonSeven(self):
    if not self.operationScreen.text():
        self.number1Screen.insert("7")
    elif self.operationScreen.text() and not self.resultScreen.text():
        self.number2Screen.insert("7")

def buttonEight(self):
    if not self.operationScreen.text():
        self.number1Screen.insert("8")
    elif self.operationScreen.text() and not self.resultScreen.text():
        self.number2Screen.insert("8")

def buttonNine(self):
    if not self.operationScreen.text():
        self.number1Screen.insert("9")
    elif self.operationScreen.text() and not self.resultScreen.text():
        self.number2Screen.insert("9")

# Functions ####################################################################################################

def buttonAdd(self):
    if self.number1Screen.text() and not self.number2Screen.text():
        self.operationScreen.setText("+")
    elif self.resultScreen.text():
        self.number1Screen.setText(self.resultScreen.text())
        self.operationScreen.setText("+")
        self.number2Screen.clear()
        self.resultScreen.clear()

def buttonSubtract(self):
    if self.number1Screen.text() and not self.number2Screen.text():
        if (self.operationScreen.text() == "^" or self.operationScreen.text() == "*" or self.operationScreen.text() == "/"):
            self.number2Screen.setText("-")
        else:
            self.operationScreen.setText("-")
    elif self.resultScreen.text():
        self.number1Screen.setText(self.resultScreen.text())
        self.operationScreen.setText("-")
        self.number2Screen.clear()
        self.resultScreen.clear()

def buttonMultiply(self):
    if self.number1Screen.text() and not self.number2Screen.text():
        self.operationScreen.setText("×")
    elif self.resultScreen.text():
        self.number1Screen.setText(self.resultScreen.text())
        self.operationScreen.setText("×")
        self.number2Screen.clear()
        self.resultScreen.clear()

def buttonDivide(self):
    if self.number1Screen.text() and not self.number2Screen.text():
        self.operationScreen.setText("/")
    elif self.resultScreen.text():
        self.number1Screen.setText(self.resultScreen.text())
        self.operationScreen.setText("/")
        self.number2Screen.clear()
        self.resultScreen.clear()

def buttonPower(self):
    if self.number1Screen.text() and not self.number2Screen.text():
        self.operationScreen.setText("^")
    elif self.resultScreen.text():
        self.number1Screen.setText(self.resultScreen.text())
        self.operationScreen.setText("^")
        self.number2Screen.clear()
        self.resultScreen.clear()

def buttonRoot(self):
    if self.number1Screen.text() and not self.number2Screen.text():
        self.operationScreen.setText("√")
        result = float(self.number1Screen.text()) ** (1/2)
        self.resultScreen.setText(str(formatInt(result)))

def buttonOneBy(self):
    if self.number1Screen.text() and not self.number2Screen.text():
        self.operationScreen.setText("1/x")
        result = 1 / float(self.number1Screen.text())
        self.resultScreen.setText(str(formatInt(result)))

def buttonModulo(self):
    if self.number1Screen.text() and not self.number2Screen.text():
        self.operationScreen.setText("%")
    elif self.resultScreen.text():
        self.number1Screen.setText(self.resultScreen.text())
        self.operationScreen.setText("%")
        self.number2Screen.clear()
        self.resultScreen.clear()

def buttonComma(self):
    if not self.operationScreen.text() and self.number1Screen.text() and '.' not in self.number1Screen.text():
        self.number1Screen.insert(".")
    elif self.operationScreen.text() and self.number2Screen.text() and '.' not in self.number2Screen.text() and not self.resultScreen.text():
        self.number2Screen.insert(".")

def buttonInvert(self):
    if self.number1Screen.text() and not self.number2Screen.text():
        if self.number1Screen.text() != "0":
            self.number1Screen.setText(str(formatInt(float(self.number1Screen.text()) * -1)))
    elif self.number1Screen.text() and self.number2Screen.text() and not self.resultScreen.text():
        if self.number2Screen.text() != "0":
            self.number2Screen.setText(str(formatInt(float(self.number2Screen.text()) * -1)))

def buttonResult(self):
    if self.operationScreen.text() == "+" and self.number2Screen.text():
        one = float(self.number1Screen.text())
        two = float(self.number2Screen.text())
        result = one + two
        self.resultScreen.setText(str(formatInt(result)))

    elif self.operationScreen.text() == "-" and self.number2Screen.text():
        one = float(self.number1Screen.text())
        two = float(self.number2Screen.text())
        result = one - two
        self.resultScreen.setText(str(formatInt(result)))

    elif self.operationScreen.text() == "×" and self.number2Screen.text():
        one = float(self.number1Screen.text())
        two = float(self.number2Screen.text())
        result = one * two
        self.resultScreen.setText(str(formatInt(result)))

    elif self.operationScreen.text() == "/" and self.number2Screen.text():
        one = float(self.number1Screen.text())
        two = float(self.number2Screen.text())
        try:
            result = one / two
        except:
            self.resultScreen.setText("Error")
            pass
        self.resultScreen.setText(str(formatInt(result)))
            
    elif self.operationScreen.text() == "^" and self.number2Screen.text():
        one = float(self.number1Screen.text())
        two = float(self.number2Screen.text())
        result = one ** two
        self.resultScreen.setText(str(formatInt(result)))

    elif self.operationScreen.text() == "%" and self.number2Screen.text():
        one = float(self.number1Screen.text())
        two = float(self.number2Screen.text())
        result = one % two
        self.resultScreen.setText(str(formatInt(result)))

def buttonBackspace(self):
    if self.number1Screen.text() and not self.operationScreen.text():
        self.number1Screen.setText(self.number1Screen.text()[:-1])
    elif self.number2Screen.text() and not self.resultScreen.text():
        self.number2Screen.setText(self.number2Screen.text()[:-1])

def buttonCE(self):
    if self.resultScreen.text():
        self.number1Screen.clear()
        self.operationScreen.clear()
        self.number2Screen.clear()
        self.resultScreen.clear()
    elif self.number2Screen.text() and not self.resultScreen.text():
        self.number2Screen.clear()
    elif self.number1Screen.text() and not self.operationScreen.text():
        self.number1Screen.clear()
    elif self.number1Screen.text() and self.operationScreen.text():
        self.number1Screen.clear()
        self.operationScreen.clear()

def formatInt(num):
    """
    Format integer numbers to remove trailing zeros
    Param:
        num: number to format
    """
    if (num % 1 == 0):
        return int(num)
    else:
        return num

# Menu ####################################################################################################

def openProgrammerCalc(self):
    self.pc = apps.programmer.ProgrammerCalc()
    self.pc.show()

def openCalendarCalc(self):
    self.sc = apps.calendar.CalendarCalc()
    self.sc.show()

def openTemperatureCalc(self):
    self.sc = apps.temperature.TemperatureCalc()
    self.sc.show()

def openDegRadCalc(self):
    self.dc = apps.degrad.DegRadCalc()
    self.dc.show()

def openPlotCalc(self):
    self.gc = apps.plot.PlotCalc()
    self.gc.show()
