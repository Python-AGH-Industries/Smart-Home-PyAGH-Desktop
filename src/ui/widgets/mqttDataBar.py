from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from src.ui.widgets.iconButton import IconButton

class MqttDataBar(QWidget):
    def __init__(self, title):
        super().__init__()
        iconPath = "src/resources/icons/"
        self.setFixedHeight(30)
        self.setStyleSheet("background-color: green; border: 1px solid black;")

        barLayout = QHBoxLayout(self)

        barTitle = QLabel(title, self)
        self.minimizeButton = IconButton(iconPath + "minimize.png", self, 25)
        self.maximizeButton = IconButton(iconPath + "maximize.png", self, 25)

        barLayout.addWidget(barTitle)
        barLayout.addStretch(1)
        barLayout.addWidget(self.minimizeButton)
        barLayout.addWidget(self.maximizeButton)

        barLayout.setContentsMargins(0, 0, 0, 0)
        barLayout.setSpacing(5)