from PyQt6.QtWidgets import QWidget, QLabel, QSizePolicy, QVBoxLayout

class MqttDataWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: green;")
        mqttDataLayout = QVBoxLayout(self)
        label = QLabel("center", self)
        mqttDataLayout.addWidget(label)

        mqttDataLayout.setContentsMargins(0, 0, 0, 0)
        mqttDataLayout.setSpacing(0)