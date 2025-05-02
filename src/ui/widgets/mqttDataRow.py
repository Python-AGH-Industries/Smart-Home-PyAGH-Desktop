from PyQt6.QtWidgets import QWidget, QVBoxLayout, QDialog
from src.ui.widgets.mqttDataContent import MqttDataContent
from src.ui.widgets.mqttDataBar import MqttDataBar
from src.ui.windows.changeSensorNameDialog import ChangeSensorNameDialog
from src.ui.widgets.login import Login

import requests

class MqttDataRow(QWidget):
    def __init__(self, rowSpecs):
        super().__init__()
        wrapperLayout = QVBoxLayout(self)

        self.session = requests.session()

        self.rowBar = MqttDataBar(rowSpecs.title)
        self.rowContent = MqttDataContent(rowSpecs)

        self.rowBar.minimizeButton.clicked.connect(self.rowContent.hide)
        self.rowBar.maximizeButton.clicked.connect(self.rowContent.show)
        self.rowBar.settingsButton.clicked.connect(
            lambda: self.changeSensorNameLogic(rowSpecs.sensors)
        )
        self.rowBar.jsonButton.clicked.connect(self.rowContent.saveDataInJson)
        self.rowBar.csvButton.clicked.connect(self.rowContent.saveDataInCsv)
        self.rowBar.imageButton.clicked.connect(self.rowContent.saveDataInPng)

        wrapperLayout.addWidget(self.rowBar)
        wrapperLayout.addWidget(self.rowContent)

        wrapperLayout.setContentsMargins(0, 0, 0, 0)
        wrapperLayout.setSpacing(0)

    def changeSensorNameLogic(self, sensorList):
        dialog = ChangeSensorNameDialog(sensorList, self)

        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        
        newNames = dialog.getNewSensorData()
        i = 0

        for oldName, _ in sensorList:
            if newNames[i] == oldName: continue
            self.session.post(
                "http://127.0.0.1:5000/changeSensorName",
                json = {
                    "username": Login.getCurrentUser().username,
                    "oldName": oldName,
                    "newName": newNames[i]
                }    
            )
            i += 1
