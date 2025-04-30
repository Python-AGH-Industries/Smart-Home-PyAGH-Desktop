from PyQt6.QtWidgets import QWidget, QVBoxLayout
from src.ui.widgets.mqttDataContent import MqttDataContent
from src.ui.widgets.mqttDataBar import MqttDataBar

class MqttDataRow(QWidget):
    def __init__(self, rowSpecs):
        super().__init__()
        wrapperLayout = QVBoxLayout(self)

        self.rowBar = MqttDataBar(rowSpecs.title)
        self.rowContent = MqttDataContent(rowSpecs)

        self.rowBar.minimizeButton.clicked.connect(self.rowContent.hide)
        self.rowBar.maximizeButton.clicked.connect(self.rowContent.show)
        self.rowBar.jsonButton.clicked.connect(self.rowContent.saveDataInJson)
        self.rowBar.csvButton.clicked.connect(self.rowContent.saveDataInCsv)
        self.rowBar.imageButton.clicked.connect(self.rowContent.saveDataInPng)

        wrapperLayout.addWidget(self.rowBar)
        wrapperLayout.addWidget(self.rowContent)

        wrapperLayout.setContentsMargins(0, 0, 0, 0)
        wrapperLayout.setSpacing(0)
