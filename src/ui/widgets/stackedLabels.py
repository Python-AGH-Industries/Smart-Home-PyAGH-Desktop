from PyQt6.QtWidgets import QWidget, QVBoxLayout, \
                            QLabel, QStyle, QStyleOption
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt

class StackedLabels(QWidget):
    def __init__(self, title, parent = None):
        super().__init__(parent)
    
        mainLayout = QVBoxLayout(self)

        self.upperLabel = QLabel(title, self)
        self.lowerLabel = QLabel("", self)

        self.upperLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lowerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        mainLayout.addWidget(self.upperLabel)
        mainLayout.addWidget(self.lowerLabel)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)