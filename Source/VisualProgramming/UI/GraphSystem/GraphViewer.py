from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class GraphViewer(QGraphicsView):
    onMouseLocation = Signal(QPointF)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.onMouseLocation.emit(self.mapToScene(self.mapFromGlobal(QCursor.pos())))
