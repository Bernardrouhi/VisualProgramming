from PySide6.QtWidgets import *
from PySide6.QtCore import *
from VisualProgramming.UI.GraphSystem.GraphViewer import GraphViewer


class GraphWidget(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._init_ui()

    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignTop)

        view = GraphViewer()
        view.onMouseLocation.connect(self.updateMouseLocation)
        self.mouseLocationLabel = QLabel("X:0.000 ,y:0.000")

        layout.addWidget(view)
        layout.addWidget(self.mouseLocationLabel)

    def updateMouseLocation(self, pos: QPointF) -> None:
        self.mouseLocationLabel.setText(f"X:{pos.x():.3f}, Y:{pos.y():.3f}")
