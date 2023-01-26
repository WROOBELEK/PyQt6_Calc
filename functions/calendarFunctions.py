
from datetime import datetime
from dateutil import relativedelta
import os

def calcudateDays(calendar1, calendar2, label):
    """
    Calculates the difference between two dates (using dateutil.relativedelta) and displays it in a label. 
    After that, it saves the result in a file called "calendar.txt" in the "results" folder.
    Params:
        calendar1 (QDateEdit) - used to get the first date
        calendar2 (QDateEdit) - used to get the second date
        label (QLabel) - the label to display the result
    """
    d1 = datetime.strptime(calendar1.date().toString("d.M.yyyy"), "%d.%m.%Y")
    d2 = datetime.strptime(calendar2.date().toString("d.M.yyyy"), "%d.%m.%Y")
    diff = relativedelta.relativedelta(d2, d1)
    result = "Difference: {} years {} months and {} days".format(diff.years, diff.months, diff.days)
    label.setText(result)
    if not os.path.isdir('./results'):
        os.mkdir('./results')
    fh = open("./results/caldendar.txt", "a")
    fh.write("From: " + calendar1.date().toString("d.M.yyyy") + " To: " + calendar2.date().toString("d.M.yyyy") + "\n"+result+"\n\n")
    fh.close()
    

