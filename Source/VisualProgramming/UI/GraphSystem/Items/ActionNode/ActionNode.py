from typing import Any
from pathlib import Path

from PySide6.QtQuick import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtQml import *
from PySide6.QtWidgets import *
from PySide6.QtQuickWidgets import *

# generated using pyside6-rcc <FileName>.qrc -o <FileName>.py
import VisualProgramming.UI.GraphSystem.Items.ActionNode.ActionNodeResources


class ActionNodeProxy(QGraphicsProxyWidget):
    url = QUrl.fromLocalFile(Path(__file__).parent.resolve() / "ActionNode.qml")

    def __init__(self, parent: None | QGraphicsItem = None):
        super().__init__(parent)

        quickWidget = QQuickWidget()
        quickWidget.setSource(self.url)
        quickWidget.setResizeMode(QQuickWidget.SizeRootObjectToView)
        quickWidget.setClearColor(Qt.transparent)
        quickWidget.setAttribute(Qt.WA_TranslucentBackground)
        root = quickWidget.rootObject()
        inputButton = root.findChild(QObject, "ExecuteInput")
        inputButton.onInputClicked.connect(self.onExecuteInputClicked)
        self.setWidget(quickWidget)
        self.setFlag(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

    def setNodeSelection(self, value: bool) -> None:
        """Set the node selection state."""
        root = self.widget().rootObject()
        if root:
            root.setProperty("isSelected", value)

    def onExecuteInputClicked(self) -> None:
        print("Clicked")


class ActionNode(QGraphicsRectItem):
    def __init__(self, parent: None | QGraphicsItem = None):
        self._proxy = None
        super().__init__(parent)
        self.setFlag(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self._proxy = ActionNodeProxy(self)
        self.setRect(self._proxy.boundingRect())
        self.setPen(Qt.NoPen)

    def itemChange(self, change: QGraphicsItem.GraphicsItemChange, value: Any) -> Any:
        if change == QGraphicsItem.ItemSelectedChange:
            self._proxy.setNodeSelection(value)
        return super().itemChange(change, value)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget | None = None) -> None:
        option.state = QStyle.State_None
        return super().paint(painter, option, widget)
