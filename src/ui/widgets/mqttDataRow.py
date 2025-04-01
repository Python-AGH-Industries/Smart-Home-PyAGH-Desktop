from PyQt6.QtWidgets import QWidget, QVBoxLayout
from src.ui.widgets.mqttDataContent import MqttDataContent
from src.ui.widgets.mqttDataBar import MqttDataBar

class MqttDataRow(QWidget):
    def __init__(self, title, units):
        super().__init__()

        wrapperLayout = QVBoxLayout(self)

        rowBar = MqttDataBar(title)
        rowContent = MqttDataContent(title, units)

        wrapperLayout.addWidget(rowBar)
        wrapperLayout.addWidget(rowContent)

        wrapperLayout.setContentsMargins(0, 0, 0, 0)
        wrapperLayout.setSpacing(0)