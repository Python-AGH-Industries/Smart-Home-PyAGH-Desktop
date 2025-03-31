from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class MqttDataDetails(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel("Data details")
        layout = QVBoxLayout(self)

        layout.addWidget(label)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)