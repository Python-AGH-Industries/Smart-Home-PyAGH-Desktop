from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QStyle, QStyleOption
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter
from src.ui.widgets.iconButton import IconButton

class MqttDataBar(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        iconPath = "src/resources/icons/"
        self.height = 40
        self.setFixedHeight(self.height)

        offset = 10

        barLayout = QHBoxLayout(self)

        barTitle = QLabel(title, self)
        self.minimizeButton = IconButton(
            f"{iconPath}minimize.png",
            self,
            self.height - offset
        )
        self.maximizeButton = IconButton(
            f"{iconPath}maximize.png",
            self,
            self.height - offset
        )
        self.jsonButton = IconButton(
            f"{iconPath}json.png",
            self,
            self.height - offset
        )
        self.csvButton = IconButton(
            f"{iconPath}csv.png",
            self,
            self.height - offset
        )
        self.imageButton = IconButton(
            f"{iconPath}image.png",
            self,
            self.height - offset
        )
        self.settingsButton = IconButton(
            f"{iconPath}gear.png",
            self,
            self.height - offset
        )

        barLayout.addWidget(barTitle)
        barLayout.addStretch(1)
        barLayout.addWidget(self.imageButton)
        barLayout.addWidget(self.csvButton)
        barLayout.addWidget(self.jsonButton)
        barLayout.addWidget(self.settingsButton)
        barLayout.addWidget(self.minimizeButton)
        barLayout.addWidget(self.maximizeButton)

        barLayout.setContentsMargins(0, 0, 0, 0)
        barLayout.setSpacing(10)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)