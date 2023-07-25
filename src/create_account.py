import sys
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(THIS_DIR, os.pardir))
sys.path.append(PARENT_DIR)

from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtSql
import bcrypt
from forms.create_account_dialog import CreateAccountDialog


class CreateAccount(QtWidgets.QDialog):
    def __init__(self, db):
        super().__init__()
        self.ui = CreateAccountDialog()
        self.ui.setup_ui(self)
        self.setWindowFlags(
            QtCore.Qt.WindowType.CustomizeWindowHint
            | QtCore.Qt.WindowType.WindowTitleHint
            | QtCore.Qt.WindowType.WindowMaximizeButtonHint
            | QtCore.Qt.WindowType.WindowMinimizeButtonHint)

        self.db = db
        self.first_name = ""
        self.last_name = ""
        self.username = ""
        self.password = ""

        # Signals
        self.ui.first_name_line_edit.textChanged.connect(self.get_data)
        self.ui.last_name_line_edit.textChanged.connect(self.get_data)
        self.ui.username_line_edit.textChanged.connect(self.get_data)
        self.ui.password_line_edit.textChanged.connect(self.get_data)
        self.ui.verify_password_line_edit.textChanged.connect(self.get_data)
        self.ui.save_button.clicked.connect(self.save)
        self.ui.cancel_button.clicked.connect(self.close)

    def get_data(self):
        self.sender().setStyleSheet("background: white")

    def save(self):
        fields_filled = self.check_fields()
        password_match = self.check_passwords(fields_filled)
        if fields_filled == True and password_match == True:
            # save info to database
            # ADD a way to check username availability
            hash = self.get_hashed_password(self.ui.password_line_edit.text())
            first = self.ui.first_name_line_edit.text()
            last = self.ui.last_name_line_edit.text()
            username = self.ui.username_line_edit.text()
            query_str = f"INSERT INTO simple_login (first_name, last_name, \
                    username, password, date, created_at, updated_at) \
                    VALUES ($${first}$$, $${last}$$, $${username}$$, \
                    $${hash}$$, now(), now(), now())"
            query = QtSql.QSqlQuery(self.db)
            success = query.exec(query_str)
            if success:
                QtWidgets.QMessageBox.information(self, "Success", 
                                            "Your account has been created")
                self.ui.first_name_line_edit.clear()
                self.ui.last_name_line_edit.clear()
                self.ui.username_line_edit.clear()
                self.ui.password_line_edit.clear()
                self.ui.verify_password_line_edit.clear()
                self.ui.first_name_line_edit.setFocus()
            else:
                print(f"Failed Query: {query_str}")
                print(f"THIS ERROR: {query.lastError().text()}")
                return 1

            self.close()

    def get_hashed_password(self, plain_text_password):
        return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

    def check_fields(self):
        list = []
        list.append(self.ui.first_name_line_edit)
        list.append(self.ui.last_name_line_edit)
        list.append(self.ui.username_line_edit)
        list.append(self.ui.username_line_edit)
        list.append(self.ui.verify_password_line_edit)
        for i in list:
            if i.text() == "":
                i.setStyleSheet("background: red")
                i.setFocus()
                return False
        else:
            return True

    def check_passwords(self, fields_filled):
        if self.ui.password_line_edit.text() == self.ui.verify_password_line_edit.text():
            return True
        else:
            self.ui.password_line_edit.clear()
            self.ui.verify_password_line_edit.clear()
            self.ui.password_line_edit.setStyleSheet("background: red")
            self.ui.verify_password_line_edit.setStyleSheet("background: red")
            if fields_filled == True:
                self.ui.password_line_edit.setFocus()
            return False

    def closeEvent(self, event):
        event.accept()
