from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout

class MqttSubPanelBar(QWidget):
    def __init__(self):
        super().__init__()
        label = QPushButton("Room 1")
        label2 = QPushButton("Room 2")
        self.setFixedHeight(40)
        self.setStyleSheet("background-color: red;")
        layout = QHBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addStretch(1)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)