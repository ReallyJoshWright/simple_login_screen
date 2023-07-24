import sys
from PyQt6 import QtWidgets


class SimpleLoginScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = SimpleLoginScreen()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
