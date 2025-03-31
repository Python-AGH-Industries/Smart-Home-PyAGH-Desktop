from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from src.ui.widgets.IconButton import IconButton

class MqttDataBar(QWidget):
    def __init__(self, title):
        super().__init__()
        iconPath = "src/resources/icons/"
        self.setFixedHeight(20)

        barLayout = QHBoxLayout(self)

        barTitle = QLabel(title, self)
        minimizeButton = IconButton(iconPath + "minimize.png", self, 20)
        maximizeButton = IconButton(iconPath + "maximize.png", self, 20)

        barLayout.addWidget(barTitle)
        barLayout.addStretch(1)
        barLayout.addWidget(minimizeButton)
        barLayout.addWidget(maximizeButton)

        barLayout.setContentsMargins(0, 0, 0, 0)
        barLayout.setSpacing(5)