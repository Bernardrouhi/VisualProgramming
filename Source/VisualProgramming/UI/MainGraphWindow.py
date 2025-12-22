from PySide6.QtWidgets import *
from VisualProgramming.UI.GraphSystem.GraphWidget import GraphWidget


class MainGraphWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Visual Programming")
        self.resize(1000, 1000)
        self._init_ui()

    def _init_ui(self) -> None:
        self.setContentsMargins(0, 0, 0, 0)
        self.setMinimumSize(1, 1)

        widget = GraphWidget()
        self.setCentralWidget(widget)
