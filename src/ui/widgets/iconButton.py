from PyQt6.QtWidgets import QPushButton, QStyleOption, QStyle
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPainter

class IconButton(QPushButton):
    def __init__(self, path = "", parent = None, fixed_size = 80):
        super().__init__(parent)
        self.setFixedSize(QSize(fixed_size, fixed_size))
        self.setIcon(QIcon(path))
        
        offset = fixed_size / 6

        self.setIconSize(QSize(
            int(fixed_size - offset),
            int(fixed_size - offset)
        ))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)
