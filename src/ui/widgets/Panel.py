from PyQt6.QtWidgets import QWidget, QHBoxLayout
from src.ui.widgets.MqttData import MqttData
from src.ui.widgets.PublicData import PublicData

class Panel(QWidget):
    def __init__(self):
        super().__init__()

        panelLayout = QHBoxLayout(self)

        mqttDataWidget = MqttData()
        publicDataWidget = PublicData()

        panelLayout.addWidget(mqttDataWidget, stretch = 3)
        panelLayout.addWidget(publicDataWidget, stretch = 2)

        panelLayout.setContentsMargins(0, 0, 0, 0)
        panelLayout.setSpacing(0)