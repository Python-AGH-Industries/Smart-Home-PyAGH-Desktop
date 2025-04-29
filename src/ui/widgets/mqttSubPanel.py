import requests
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from src.model.loginController import LoginController
from src.ui.widgets.mqttDataRow import MqttDataRow
from src.model.dataRowSpecs import DataRowSpecs
from src.model.floatRounder import FloatRounder
from random import randint
from datetime import datetime, timedelta

class MqttSubPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.rounder = FloatRounder()
        self.login = LoginController()

        mqttDataLayout = QVBoxLayout(self)

        tempSpecs = DataRowSpecs("Temperature", ["C", "F", "K"],
                                self.create_sensor_list(1))
        humiditySpecs = DataRowSpecs("Humidity", ["%", "g/m³", "kg/m³"],
                                self.create_sensor_list(2))
        pressureSpecs = DataRowSpecs("Pressure", ["Pa", "bar", "atm"],
                                self.create_sensor_list(3))
        lightSpecs = DataRowSpecs("Light", ["Cd"],
                               self.create_sensor_list(4))

        cnt = 18
        current_time = datetime.now() - timedelta(hours = cnt)
        tempData, humiData, presData, lighData = [], [], [], []

        for _ in range(cnt):
            tempData.append(
                (
                    self.rounder.roundFloat5(randint(100, 350) / 10),
                    current_time
                )
            )
            humiData.append(
                (
                    self.rounder.roundFloat5(randint(100, 300) / 10),
                    current_time
                )
            )
            presData.append(
                (
                    self.rounder.roundFloat5(randint(980000, 1030000) / 10),
                    current_time
                )
            )
            lighData.append(
                (
                    self.rounder.roundFloat5(randint(3000, 12000)),
                    current_time
                )
            )
            current_time += timedelta(hours = 1)

        # print(tempData)
        self.temperatureRow = MqttDataRow(tempSpecs, tempData)
        self.humidityRow = MqttDataRow(humiditySpecs, humiData) 
        self.pressureRow = MqttDataRow(pressureSpecs, presData)
        self.lightRow = MqttDataRow(lightSpecs, lighData)

        mqttDataLayout.addWidget(self.temperatureRow)
        mqttDataLayout.addWidget(self.humidityRow)
        mqttDataLayout.addWidget(self.pressureRow)
        mqttDataLayout.addWidget(self.lightRow)
        mqttDataLayout.addStretch(2)

        mqttDataLayout.setContentsMargins(0, 0, 0, 0)
        mqttDataLayout.setSpacing(0)

    def create_sensor_list(self,type_id):
        response = self.login.getSensors(type_id)
        result = []
        for sensor in response["sensors"]:
            result.append((sensor["name"],sensor["id"]))
        return result