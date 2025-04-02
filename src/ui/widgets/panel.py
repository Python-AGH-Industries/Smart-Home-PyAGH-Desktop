from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from src.ui.widgets.mqttSubPanel import MqttSubPanel
from src.ui.widgets.publicSubPanel import PublicSubPanel
from src.ui.widgets.mqttSubPanelBar import MqttSubPanelBar

class Panel(QWidget):
    def __init__(self):
        super().__init__()

        panelLayout = QHBoxLayout(self)
        mqttSubPanelLayout = QVBoxLayout()

        mqttSubPanelBar = MqttSubPanelBar()
        mqttDataWidget = MqttSubPanel()
        publicDataWidget = PublicSubPanel()

        mqttSubPanelLayout.addWidget(mqttSubPanelBar)
        mqttSubPanelLayout.addWidget(mqttDataWidget) 

        panelLayout.addLayout(mqttSubPanelLayout, stretch = 2)
        panelLayout.addWidget(publicDataWidget, stretch = 1)

        panelLayout.setContentsMargins(0, 0, 0, 0)
        panelLayout.setSpacing(0)
