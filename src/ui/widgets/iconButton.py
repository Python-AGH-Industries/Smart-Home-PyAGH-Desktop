from PyQt6.QtWidgets import QPushButton, QStyleOption, QStyle
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPainter

class IconButton(QPushButton):
    def __init__(self, path = "", parent = None, fixedSize = 80):
        super().__init__(parent)
        self.setFixedSize(QSize(fixedSize, fixedSize))
        self.setIcon(QIcon(path))
        
        offset = fixedSize / 6

        self.setIconSize(QSize(
            int(fixedSize - offset),
            int(fixedSize - offset)
        ))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)
