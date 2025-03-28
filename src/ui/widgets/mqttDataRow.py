from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout

class MqttDataRow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: green; border: 1px solid black;")
        layout = QHBoxLayout(self)
        label = QLabel("Data row")
        layout.addWidget(label)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)