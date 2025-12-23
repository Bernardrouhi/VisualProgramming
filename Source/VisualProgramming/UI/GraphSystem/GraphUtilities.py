from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


def drawBackground(painter: QPainter, rect: QRectF | QRect, colour: QColor) -> None:
    """
    Draw the background.
    :param painter:
    :param rect:
    :param colour:
    """
    brush = QBrush(colour)
    painter.setPen(Qt.NoPen)
    painter.setBrush(brush)
    painter.drawRect(rect)


def drawGuideline(painter: QPainter, rect: QRectF | QRect, colour: QColor, perPixel: int) -> None:
    """
    Draw guideline accurately on the screen.
    :param painter:
    :param rect:
    :param colour: Colour of the line
    :param perPixel: draw per pixel for the entire screen
    """

    def _drawGuides(painterRef: QPainter, rectRef: QRectF | QRect, pixel: int) -> None:
        r = rectRef.toRect()
        xmin = r.left() - r.left() % pixel - pixel
        ymin = r.top() - r.top() % pixel - pixel
        xmax = r.right() - r.right() % pixel + pixel
        ymax = r.bottom() - r.bottom() % pixel + pixel
        x = xmin
        while x <= xmax:
            painterRef.drawLine(x, r.top(), x, r.bottom())
            x += pixel
        y = ymin
        while y <= ymax:
            painterRef.drawLine(r.left(), y, r.right(), y)
            y += pixel

    pen = QPen()
    pen.setWidth(1)
    pen.setColor(colour)
    pen.setStyle(Qt.SolidLine)
    painter.setPen(pen)
    _drawGuides(painter, rect, perPixel)
