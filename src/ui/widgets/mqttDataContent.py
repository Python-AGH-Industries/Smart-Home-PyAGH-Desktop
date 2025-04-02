from PyQt6.QtWidgets import QWidget, QHBoxLayout
from src.ui.widgets.mqttDataGraph import MqttDataGraph
from src.ui.widgets.mqttDataDetails import MqttDataDetails

class MqttDataContent(QWidget):
    def __init__(self, rowSpecs, mqttData):
        super().__init__()
        dataContentLayout = QHBoxLayout(self)

        dataGraph = MqttDataGraph(rowSpecs.title, mqttData)
        dataDetails = MqttDataDetails(rowSpecs, mqttData)

        dataContentLayout.addWidget(dataGraph, stretch = 5)
        dataContentLayout.addWidget(dataDetails, stretch = 4)

        dataContentLayout.setContentsMargins(0, 0, 0, 0)
        dataContentLayout.setSpacing(0)