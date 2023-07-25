import sys
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))
sys.path.append(PARENT_DIR)

from PyQt6 import QtWidgets
from forms.mainwindow import Ui_MainWindow


class SimpleLoginScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = SimpleLoginScreen()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
