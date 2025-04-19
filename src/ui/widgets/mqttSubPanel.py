from PyQt6.QtWidgets import QWidget, QVBoxLayout
from src.ui.widgets.mqttDataRow import MqttDataRow
from src.model.dataRowSpecs import DataRowSpecs
from src.model.floatRounder import FloatRounder
from random import randint
from datetime import datetime, timedelta

class MqttSubPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.rounder = FloatRounder()
        mqttDataLayout = QVBoxLayout(self)

        tempSpecs = DataRowSpecs("Temperature", ["C", "F", "K"],
                                ["Oven", "Floor"])
        humiditySpecs = DataRowSpecs("Humidity", ["%", "g/m³", "kg/m³"],
                                ["Ceiling"])
        pressureSpecs = DataRowSpecs("Pressure", ["Pa", "bar", "atm"],
                                ["Floor P1", "Floor P2"])
        lightSpecs = DataRowSpecs("Light", ["Cd"],
                               ["Table", "Desk"])

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