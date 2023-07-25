import sys
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))
sys.path.append(PARENT_DIR)

from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtSql
import bcrypt
from forms.login_dialog import LoginDialog
from create_account import CreateAccount


class Login(QtWidgets.QDialog):
    def __init__(self, db):
        super().__init__()
        self.ui = LoginDialog()
        self.ui.setup_ui(self)
        self.setWindowFlags(
            QtCore.Qt.WindowType.CustomizeWindowHint
            | QtCore.Qt.WindowType.WindowTitleHint
            | QtCore.Qt.WindowType.WindowMaximizeButtonHint
            | QtCore.Qt.WindowType.WindowMinimizeButtonHint)

        self.db = db
        self.username = ""
        self.password = ""

        # Signals
        self.ui.username_line_edit.textChanged.connect(self.get_username)
        self.ui.password_line_edit.textChanged.connect(self.get_password)
        self.ui.login_button.clicked.connect(self.login)
        self.ui.sign_up_button.clicked.connect(self.sign_up)

    def login(self):
        # Add code here
        query = f"SELECT * FROM simple_login WHERE username = '{self.username}'"
        query_model = QtSql.QSqlQueryModel()
        query_model.setQuery(query, self.db)
        hash = query_model.record(0).value("password")
        if hash is not None:
            good = self.check_password(self.password, hash)
        else:
            good = False
        if good:
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Fail", 
                                          "Your username or password is wrong")
            self.ui.username_line_edit.clear()
            self.ui.password_line_edit.clear()
            self.ui.username_line_edit.setFocus()

    def get_username(self):
        self.username = self.ui.username_line_edit.text()

    def get_password(self):
        self.password = self.ui.password_line_edit.text()

    def check_password(self, plain_text_password, hashed_password):
        return bcrypt.checkpw(plain_text_password, hashed_password)

    def sign_up(self):
        dialog = CreateAccount(self.db)
        dialog.exec()

    def closeEvent(self, event):
        event.accept()
