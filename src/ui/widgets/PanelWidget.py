from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

class PanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel("Hello to panel widget", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(label, stretch = 1)