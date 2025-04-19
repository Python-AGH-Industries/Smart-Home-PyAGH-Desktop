from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter
from src.ui.widgets.iconButton import IconButton

class MqttDataBar(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        iconPath = "src/resources/icons/"
        self.height = 30
        self.setFixedHeight(self.height)
        self.setStyleSheet("QWidget {background-color: rgb(80, 80, 80);}")

        barLayout = QHBoxLayout(self)

        barTitle = QLabel(title, self)
        self.minimizeButton = IconButton(
            f"{iconPath}minimize.png",
            self,
            self.height - 5
        )
        self.maximizeButton = IconButton(
            f"{iconPath}maximize.png",
            self,
            self.height - 5
        )
        self.jsonButton = IconButton(
            f"{iconPath}json.png",
            self,
            self.height - 5
        )
        self.csvButton = IconButton(
            f"{iconPath}csv.png",
            self,
            self.height - 5
        )
        self.imageButton = IconButton(
            f"{iconPath}image.png",
            self,
            self.height - 5
        )

        barLayout.addWidget(barTitle)
        barLayout.addStretch(1)
        barLayout.addWidget(self.imageButton)
        barLayout.addWidget(self.csvButton)
        barLayout.addWidget(self.jsonButton)
        barLayout.addWidget(self.minimizeButton)
        barLayout.addWidget(self.maximizeButton)

        barLayout.setContentsMargins(0, 0, 0, 0)
        barLayout.setSpacing(5)
    
    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.fillRect(self.rect(), self.palette().window())
        return super().paintEvent(a0)