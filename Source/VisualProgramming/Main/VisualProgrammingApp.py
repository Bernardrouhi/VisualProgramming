import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QtMsgType, qInstallMessageHandler
from VisualProgramming.UI.MainGraphWindow import MainGraphWindow


def messageHandler(mode, context, message):
    if mode == QtMsgType.QtDebugMsg:
        print(f"[QML DEBUG] {message}")
    elif mode == QtMsgType.QtWarningMsg:
        print(f"[QML WARNING] {message}")
    elif mode == QtMsgType.QtCriticalMsg:
        print(f"[QML CRITICAL] {message}")
    elif mode == QtMsgType.QtFatalMsg:
        print(f"[QML FATAL] {message}")


def main() -> None:
    qInstallMessageHandler(messageHandler)
    instance = QApplication(sys.argv)
    app = MainGraphWindow()
    app.show()
    instance.exec()


if __name__ == "__main__":
    main()
