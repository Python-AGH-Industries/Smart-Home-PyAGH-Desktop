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

        bar_layout = QHBoxLayout(self)

        bar_title = QLabel(title, self)
        self.minimize_button = IconButton(
            f"{iconPath}minimize.png",
            self,
            self.height - offset
        )
        self.maximize_button = IconButton(
            f"{iconPath}maximize.png",
            self,
            self.height - offset
        )
        self.json_button = IconButton(
            f"{iconPath}json.png",
            self,
            self.height - offset
        )
        self.csv_button = IconButton(
            f"{iconPath}csv.png",
            self,
            self.height - offset
        )
        self.image_button = IconButton(
            f"{iconPath}image.png",
            self,
            self.height - offset
        )
        self.settings_button = IconButton(
            f"{iconPath}gear.png",
            self,
            self.height - offset
        )

        bar_layout.addWidget(bar_title)
        bar_layout.addStretch(1)
        bar_layout.addWidget(self.image_button)
        bar_layout.addWidget(self.csv_button)
        bar_layout.addWidget(self.json_button)
        bar_layout.addWidget(self.settings_button)
        bar_layout.addWidget(self.minimize_button)
        bar_layout.addWidget(self.maximize_button)

        bar_layout.setContentsMargins(0, 0, 0, 0)
        bar_layout.setSpacing(10)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)