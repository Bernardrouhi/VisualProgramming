from dataclasses import dataclass

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from VisualProgramming.UI.GraphSystem.GraphUtilities import drawBackground, drawGuideline
from VisualProgramming.Core.PkgResource import PkgResource


@dataclass
class GraphNavigationMode:
    drag: bool = False
    pan: bool = False
    zoom: bool = False


@dataclass
class GraphBackendData:
    mousePosition: None | QPoint = None
    """ Position of the mouse."""


class GraphViewer(QGraphicsView):
    onMouseLocation = Signal(QPointF)

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self._mode = GraphNavigationMode()
        self._backend = GraphBackendData()
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
        self.setScene(QGraphicsScene(QRectF(10000, 10000, 10000, 10000)))
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet(PkgResource.stylesheet("GraphViewer"))

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        On mouse key pressed.
        :param event: reference object of QMouseEvent
        """
        if event.button() == Qt.MiddleButton:
            self._backend.mousePosition = event.pos()
            self.setCursor(Qt.ClosedHandCursor)
            self._mode.pan = True
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        On mouse move.
        :param event: reference object of QMouseEvent
        """
        self.onMouseLocation.emit(self.mapToScene(self.mapFromGlobal(QCursor.pos())))
        if self._mode.pan:
            diffLocation = event.pos() - self._backend.mousePosition
            self._backend.mousePosition = event.pos()
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - diffLocation.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - diffLocation.y())
            self.repaint()
            event.accept()
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """
        On mouse key released.
        :param event: reference object of QMouseEvent
        """
        # reset pan mode
        self._backend.mousePosition = None
        self._mode.pan = False
        self.setCursor(Qt.ArrowCursor)
        super().mouseReleaseEvent(event)

    def wheelEvent(self, event: QWheelEvent) -> None:
        """
        On mouse wheel changed.
        :param event: reference object of QWheelEvent
        """
        super().wheelEvent(event)

    def drawBackground(self, painter: QPainter, rect: QRectF | QRect) -> None:
        super().drawBackground(painter, rect)
        # Background Colour
        drawBackground(painter, rect, QColor(38, 38, 38))
        # 10 pixel guidelines
        drawGuideline(painter, rect, QColor(50, 50, 50), 10)
        # 100 pixel guidelines
        drawGuideline(painter, rect, QColor(15, 15, 15), 100)
