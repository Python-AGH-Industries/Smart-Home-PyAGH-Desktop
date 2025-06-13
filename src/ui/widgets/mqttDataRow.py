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

        self.rowBar.minimize_button.clicked.connect(self.rowContent.hide)
        self.rowBar.maximize_button.clicked.connect(self.rowContent.show)
        self.rowBar.settings_button.clicked.connect(
            lambda: self.changeSensorNameLogic(rowSpecs.sensors)
        )
        self.rowBar.json_button.clicked.connect(self.rowContent.saveDataInJson)
        self.rowBar.csv_button.clicked.connect(self.rowContent.saveDataInCsv)
        self.rowBar.image_button.clicked.connect(self.rowContent.saveDataInPng)

        wrapperLayout.addWidget(self.rowBar)
        wrapperLayout.addWidget(self.rowContent)

        wrapperLayout.setContentsMargins(0, 0, 0, 0)
        wrapperLayout.setSpacing(0)

    def changeSensorNameLogic(self, sensor_list):
        dialog = ChangeSensorNameDialog(sensor_list, self)

        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        
        new_names = [name.strip() for name in dialog.getNewSensorData()]
        result_data = []

        for (old_name, id), new_name in zip(sensor_list, new_names):
            if new_name == old_name: 
                result_data.append((new_name, id))
                continue

            response = self.session.post(
                "http://127.0.0.1:5000/changeSensorName",
                json = {
                    "username": Login.getCurrentUser().username,
                    "old_name": old_name,
                    "new_name": new_name
                }    
            )

            if response.status_code == 200:
                result_data.append((new_name, id))
                QMessageBox.information(
                    self,
                    "Changed name",
                    f"Changed sensor name from {old_name} to {new_name}"
                )
            else:
                result_data.append((old_name, id))
                QMessageBox.warning(
                    self,
                    "Change failed",
                    f"Could not change sensor name from {old_name} to "
                    f"{new_name} because:\n{response.json().get("error")}"
                )

        self.rowContent.data_details.updataSensorNames(result_data)
