from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from VisualProgramming.UI.GraphSystem.GraphUtilities import drawBackground, drawGuideline


class GraphViewer(QGraphicsView):
    onMouseLocation = Signal(QPointF)

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        # Scene properties
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setFrameShape(QFrame.NoFrame)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.ViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setScene(QGraphicsScene(QRectF(200, 200, 200, 200)))
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.onMouseLocation.emit(self.mapToScene(self.mapFromGlobal(QCursor.pos())))

    def drawBackground(self, painter: QPainter, rect: QRectF | QRect) -> None:
        super().drawBackground(painter, rect)
        # Background Colour
        drawBackground(painter, rect, QColor(38, 38, 38))
        # 10 pixel guidelines
        drawGuideline(painter, rect, QColor(50, 50, 50), 10)
        # 100 pixel guidelines
        drawGuideline(painter, rect, QColor(15, 15, 15), 100)
