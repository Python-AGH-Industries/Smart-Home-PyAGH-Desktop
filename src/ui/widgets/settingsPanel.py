from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QStyle, QStyleOption
from PyQt6.QtGui import QPainter

class SettingsPanel(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel("Panel under construction")
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)