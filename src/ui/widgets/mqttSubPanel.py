import requests
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from src.model.loginController import LoginController
from src.ui.widgets.mqttDataRow import MqttDataRow
from src.model.dataRowSpecs import DataRowSpecs
from src.model.floatRounder import FloatRounder

class MqttSubPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.rounder = FloatRounder()
        self.login = LoginController()

        mqttDataLayout = QVBoxLayout(self)

        self.tempSpecs = DataRowSpecs("Temperature", ["C", "F", "K"],
                                self.create_sensor_list(1))
        self.humiditySpecs = DataRowSpecs("Humidity", ["%", "g/m³", "kg/m³"],
                                self.create_sensor_list(2))
        self.pressureSpecs = DataRowSpecs("Pressure", ["Pa", "bar", "atm"],
                                self.create_sensor_list(3))
        self.lightSpecs = DataRowSpecs("Light", ["Cd"],
                               self.create_sensor_list(4))

        self.temperatureRow = MqttDataRow(self.tempSpecs)
        self.humidityRow = MqttDataRow(self.humiditySpecs)
        self.pressureRow = MqttDataRow(self.pressureSpecs)
        self.lightRow = MqttDataRow(self.lightSpecs)

        mqttDataLayout.addWidget(self.temperatureRow)
        mqttDataLayout.addWidget(self.humidityRow)
        mqttDataLayout.addWidget(self.pressureRow)
        mqttDataLayout.addWidget(self.lightRow)
        mqttDataLayout.addStretch(2)

        mqttDataLayout.setContentsMargins(0, 0, 0, 0)
        mqttDataLayout.setSpacing(0)

    def create_sensor_list(self, type_id):
        response = self.login.getSensors(type_id)
        result = []
        for sensor in response["sensors"]:
            result.append((sensor["name"], sensor["id"]))
        return result