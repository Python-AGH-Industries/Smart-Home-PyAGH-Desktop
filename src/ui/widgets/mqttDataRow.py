from PyQt6.QtWidgets import QWidget, QVBoxLayout
from src.ui.widgets.mqttDataContent import MqttDataContent
from src.ui.widgets.mqttDataBar import MqttDataBar

class MqttDataRow(QWidget):
    def __init__(self, rowSpecs, mqttData):
        super().__init__()

        wrapperLayout = QVBoxLayout(self)

        rowBar = MqttDataBar(rowSpecs.title)
        rowContent = MqttDataContent(rowSpecs, mqttData)

        rowBar.minimizeButton.clicked.connect(rowContent.hide)
        rowBar.maximizeButton.clicked.connect(rowContent.show)

        wrapperLayout.addWidget(rowBar)
        wrapperLayout.addWidget(rowContent)

        wrapperLayout.setContentsMargins(0, 0, 0, 0)
        wrapperLayout.setSpacing(0)
