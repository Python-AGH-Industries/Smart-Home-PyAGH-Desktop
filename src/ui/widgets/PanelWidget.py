from PyQt6.QtWidgets import QWidget, QHBoxLayout
from src.ui.widgets.MqttDataWidget import MqttDataWidget
from src.ui.widgets.PublicDataWidget import PublicDataWidget

class PanelWidget(QWidget):
    def __init__(self):
        super().__init__()

        panelLayout = QHBoxLayout(self)

        mqttDataWidget = MqttDataWidget()
        publicDataWidget = PublicDataWidget()

        panelLayout.addWidget(mqttDataWidget, stretch = 3)
        panelLayout.addWidget(publicDataWidget, stretch = 2)

        panelLayout.setContentsMargins(0, 0, 0, 0)
        panelLayout.setSpacing(0)