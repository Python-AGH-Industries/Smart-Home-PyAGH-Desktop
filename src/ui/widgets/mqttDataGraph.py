from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class MqttDataGraph(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel("some graph")
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)