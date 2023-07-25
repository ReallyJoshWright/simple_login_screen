from PyQt6 import QtWidgets
from PyQt6 import QtCore


class LoginDialog:
    def setup_ui(self, parent):
        # parent = QtWidgets.QDialog() # REMOVE
        parent.setWindowTitle("Simple Login Screen")
        parent.resize(800, 600)

        self.main_layout = QtWidgets.QGridLayout()
        parent.setLayout(self.main_layout)

        # Create widgets
        self.top_label = QtWidgets.QLabel("Simple Login Screen")
        self.username_line_edit = QtWidgets.QLineEdit()
        self.password_line_edit = QtWidgets.QLineEdit()
        self.login_button = QtWidgets.QPushButton("Log in")
        self.create_account_label = QtWidgets.QLabel("Don't have an account?")
        self.sign_up_button = QtWidgets.QPushButton("Sign up")
        self.horizontal_line = QtWidgets.QFrame()

        # Update widgets
        self.username_line_edit.setPlaceholderText("Username")
        self.password_line_edit.setPlaceholderText("Password")
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.horizontal_line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.top_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

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
        self.top_label.setStyleSheet(self.label_style_sheet)
        parent.setStyleSheet(self.widget_style_sheet)
        self.login_button.setStyleSheet(self.button_style_sheet)
        self.sign_up_button.setStyleSheet(self.button_style_sheet)
        self.username_line_edit.setStyleSheet(self.line_edit_style_sheet)
        self.password_line_edit.setStyleSheet(self.line_edit_style_sheet)

        # Layouts
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.addWidget(self.create_account_label)
        self.horizontal_layout.addWidget(self.sign_up_button)

        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.addWidget(self.top_label)
        self.vertical_layout.addWidget(self.username_line_edit)
        self.vertical_layout.addWidget(self.password_line_edit)
        self.vertical_layout.addWidget(self.login_button)
        self.vertical_layout.addWidget(self.horizontal_line)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.main_layout.addLayout(self.vertical_layout, 0, 0)
