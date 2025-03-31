from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout

class MqttDataContent(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel("Content wrapper", self)
        layout = QHBoxLayout(self)
        layout.addWidget(label)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)