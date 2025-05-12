from PyQt6.QtWidgets import QWidget, QVBoxLayout, QDialog, QMessageBox
from src.ui.widgets.mqttDataContent import MqttDataContent
from src.ui.widgets.mqttDataBar import MqttDataBar
from src.ui.windows.changeSensorNameDialog import ChangeSensorNameDialog
from src.ui.windows.generateReportDialog import GenerateReportDialog
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
        self.rowBar.reportButton.clicked.connect(
            lambda: self.generateReportLogic(rowSpecs)
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
        
        newNames = [name.strip() for name in dialog.getNewSensorData()]
        resultData = []

        for (oldName, id), newName in zip(sensorList, newNames):
            if newName == oldName: 
                resultData.append((newName, id))
                continue

            response = self.session.post(
                "http://127.0.0.1:5000/changeSensorName",
                json = {
                    "username": Login.getCurrentUser().username,
                    "oldName": oldName,
                    "newName": newName
                }    
            )

            if response.status_code == 200:
                resultData.append((newName, id))
                QMessageBox.information(
                    self,
                    "Changed name",
                    f"Changed sensor name from {oldName} to {newName}"
                )
            else:
                resultData.append((oldName, id))
                QMessageBox.warning(
                    self,
                    "Change failed",
                    f"Could not change sensor name from {oldName} to "
                    f"{newName} because:\n{response.json().get("error")}"
                )

        self.rowContent.dataDetails.updataSensorNames(resultData)

    def generateReportLogic(self, rowSpecs):
        dialog = GenerateReportDialog(rowSpecs, self)
        
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return