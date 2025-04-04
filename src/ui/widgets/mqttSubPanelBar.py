from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout

class MqttSubPanelBar(QWidget):
    def __init__(self):
        super().__init__()
        label = QPushButton("Kitchen")
        label2 = QPushButton("Living Room")
        label3 = QPushButton("+")
        self.setFixedHeight(40)
        self.setStyleSheet("background-color: rgb(225, 225, 225); color: rgb(20, 20, 20);")
        layout = QHBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addStretch(1)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)