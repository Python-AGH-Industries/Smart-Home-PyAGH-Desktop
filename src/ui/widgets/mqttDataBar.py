from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from src.ui.widgets.iconButton import IconButton

class MqttDataBar(QWidget):
    def __init__(self, title):
        super().__init__()
        iconPath = "src/resources/icons/"
        self.height = 40
        self.setFixedHeight(self.height)
        self.setStyleSheet("background-color: green; border: 1px solid black;")

        barLayout = QHBoxLayout(self)

        barTitle = QLabel(title, self)
        self.minimizeButton = IconButton(f"{iconPath}minimize.png", self, self.height - 5)
        self.maximizeButton = IconButton(f"{iconPath}maximize.png", self, self.height - 5)
        self.jsonButton = IconButton(f"{iconPath}json.png", self, self.height - 5)
        self.csvButton = IconButton(f"{iconPath}csv.png", self, self.height - 5)
        self.imageButton = IconButton(f"{iconPath}image.png", self, self.height - 5)

        barLayout.addWidget(barTitle)
        barLayout.addStretch(1)
        barLayout.addWidget(self.imageButton)
        barLayout.addWidget(self.csvButton)
        barLayout.addWidget(self.jsonButton)
        barLayout.addWidget(self.minimizeButton)
        barLayout.addWidget(self.maximizeButton)

        barLayout.setContentsMargins(0, 0, 0, 0)
        barLayout.setSpacing(5)