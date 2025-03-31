from PyQt6.QtWidgets import QWidget, QHBoxLayout
from src.ui.widgets.MqttSubPanel import MqttSubPanel
from src.ui.widgets.PublicSubPanel import PublicSubPanel

class Panel(QWidget):
    def __init__(self):
        super().__init__()

        panelLayout = QHBoxLayout(self)

        mqttDataWidget = MqttSubPanel()
        publicDataWidget = PublicSubPanel()

        panelLayout.addWidget(mqttDataWidget, stretch = 3)
        panelLayout.addWidget(publicDataWidget, stretch = 2)

        panelLayout.setContentsMargins(0, 0, 0, 0)
        panelLayout.setSpacing(0)
