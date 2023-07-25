import sys
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))
sys.path.append(PARENT_DIR)

from PyQt6 import QtWidgets
from forms.mainwindow import Ui_MainWindow
from login import Login
from config.database import DB


class SimpleLoginScreen(QtWidgets.QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)
        self.db = db

        # Signals
        self.ui.sign_out_button.clicked.connect(self.close)

        # Methods
        self.login()

    def login(self):
        dialog = Login(self.db)
        dialog.exec()

    def closeEvent(self, event):
        event.accept()


def main():
    app = QtWidgets.QApplication(sys.argv)
    db = DB()
    window = SimpleLoginScreen(db.connect)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
