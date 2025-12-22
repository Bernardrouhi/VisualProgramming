import sys
from PySide6.QtWidgets import *
from VisualProgramming.UI.MainGraphWindow import MainGraphWindow


def main() -> None:
    instance = QApplication(sys.argv)
    app = MainGraphWindow()
    app.show()
    instance.exec()


if __name__ == "__main__":
    main()
