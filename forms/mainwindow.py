from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6 import QtWidgets


class Ui_MainWindow:
    def setup_ui(self, parent):
        # parent = QtWidgets.QMainWindow() # REMOVE
        parent.setWindowTitle("Simple Login Screen")
        parent.resize(800, 600)

        # Set central widget
        self.central_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.central_widget.setLayout(self.main_layout)
        parent.setCentralWidget(self.central_widget)

        # Create widgets
        self.top_label = QtWidgets.QLabel("You have successfully logged in!")
        self.sign_out_button = QtWidgets.QPushButton("Sign out")
        self.horizontal_line = QtWidgets.QFrame()

        # Update widgets
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

        # Set style sheets
        self.top_label.setStyleSheet(self.label_style_sheet)
        self.central_widget.setStyleSheet(self.widget_style_sheet)
        self.sign_out_button.setStyleSheet(self.button_style_sheet)

        # Layouts
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.addWidget(self.sign_out_button)

        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.addWidget(self.top_label)
        self.vertical_layout.addWidget(self.horizontal_line)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.main_layout.addLayout(self.vertical_layout, 0, 0)
