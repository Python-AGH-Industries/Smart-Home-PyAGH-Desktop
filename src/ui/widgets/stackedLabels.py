from PyQt6.QtWidgets import QWidget, QVBoxLayout, \
                            QLabel, QStyle, QStyleOption
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt

class StackedLabels(QWidget):
    def __init__(self, title, parent = None):
        super().__init__(parent)
    
        main_layout = QVBoxLayout(self)

        self.upper_label = QLabel(title, self)
        self.lower_label = QLabel("", self)

        self.upper_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lower_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(self.upper_label)
        main_layout.addWidget(self.lower_label)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)