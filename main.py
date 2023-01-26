import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

import ui.mainUI


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initializes the MainWindow window (QMainWindow) and sets the window title, icon, size and calls the mainUI function to create the UI.
        """
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("ico/calculator.ico"))
        self.setFixedSize(400, 500)
        ui.mainUI.UI(self)

    def closeEvent(self, event):
        """
        Overrides the closeEvent method to close all windows when the main window is closed.
        Params:
            event: QCloseEvent
        """
        for window in QApplication.topLevelWidgets():
            window.close()
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())