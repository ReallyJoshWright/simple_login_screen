from PyQt6 import QtWidgets
from PyQt6 import QtCore


class CreateAccountDialog:
    def setup_ui(self, parent):
        # parent = QtWidgets.QDialog() # REMOVE
        parent.setWindowTitle("Simple Login Screen")
        parent.resize(800, 600)

        self.main_layout = QtWidgets.QGridLayout()
        parent.setLayout(self.main_layout)

        # Create widgets
        self.first_name_line_edit = QtWidgets.QLineEdit()
        self.last_name_line_edit = QtWidgets.QLineEdit()
        self.username_line_edit = QtWidgets.QLineEdit()
        self.password_line_edit = QtWidgets.QLineEdit()
        self.verify_password_line_edit = QtWidgets.QLineEdit()
        self.first_name_label = QtWidgets.QLabel("Enter First Name")
        self.last_name_label = QtWidgets.QLabel("Enter Last Name")
        self.username_label = QtWidgets.QLabel("Create a Username")
        self.password_label = QtWidgets.QLabel("Create a Password")
        self.verify_password_label = QtWidgets.QLabel("Verify Password")
        self.empty_label = QtWidgets.QLabel()
        self.save_button = QtWidgets.QPushButton("Save")
        self.cancel_button = QtWidgets.QPushButton("Cancel")

        # Update widgets
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.verify_password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        # Create style sheets
        self.label_style_sheet = [
            "QLabel {",
            "background-color: white;",
            "border-color: black;",
            "border-style: solid;",
            "border-width: 1px;",
            "font-size: 24px;",
            "}"
        ]
        self.label_style_sheet = " ".join(self.label_style_sheet)
        self.widget_style_sheet = [
            "QWidget {",
            "background-color: gray;",
            "}"
        ]
        self.widget_style_sheet = " ".join(self.widget_style_sheet)
        self.button_style_sheet = [
            "QPushButton {",
            "background-color: blue;",
            "color: white;",
            "}"
        ]
        self.button_style_sheet = " ".join(self.button_style_sheet)
        self.line_edit_style_sheet = [
            "QLineEdit {",
            "background-color: white;",
            "}"
        ]
        self.line_edit_style_sheet = " ".join(self.line_edit_style_sheet)

        # Set style sheets
        parent.setStyleSheet(self.widget_style_sheet)
        self.save_button.setStyleSheet(self.button_style_sheet)
        self.cancel_button.setStyleSheet(self.button_style_sheet)
        self.first_name_line_edit.setStyleSheet(self.line_edit_style_sheet)
        self.last_name_line_edit.setStyleSheet(self.line_edit_style_sheet)
        self.username_line_edit.setStyleSheet(self.line_edit_style_sheet)
        self.password_line_edit.setStyleSheet(self.line_edit_style_sheet)
        self.verify_password_line_edit.setStyleSheet(self.line_edit_style_sheet)

        # Layouts
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.addWidget(self.save_button)
        self.horizontal_layout.addWidget(self.cancel_button)

        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.addRow(self.first_name_label, self.first_name_line_edit)
        self.form_layout.addRow(self.last_name_label, self.last_name_line_edit)
        self.form_layout.addRow(self.username_label, self.username_line_edit)
        self.form_layout.addRow(self.password_label, self.password_line_edit)
        self.form_layout.addRow(self.verify_password_label, self.verify_password_line_edit)
        self.form_layout.addRow(self.empty_label, self.horizontal_layout)

        self.main_layout.addLayout(self.form_layout, 0, 0)
