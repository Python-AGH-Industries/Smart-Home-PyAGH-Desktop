from PyQt6.QtWidgets import QWidget, QVBoxLayout
from src.ui.widgets.mqttDataRow import MqttDataRow
from src.model.dataRowSpecs import DataRowSpecs
from random import randint
from datetime import datetime, timedelta

class MqttSubPanel(QWidget):
    def __init__(self):
        super().__init__()
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
            tempData.append((round(randint(100, 350) / 10, 3), current_time))
            humiData.append((round(randint(100, 300) / 10, 3), current_time))
            presData.append((round(randint(980000, 1030000) / 100, 3), current_time))
            lighData.append((round(randint(3000, 12000), 3), current_time))
            current_time += timedelta(hours = 1)

        temperatureRow = MqttDataRow(tempSpecs, tempData)
        humidityRow = MqttDataRow(humiditySpecs, humiData)
        pressureRow = MqttDataRow(pressureSpecs, presData)
        lightRow = MqttDataRow(lightSpecs, lighData)

        mqttDataLayout.addWidget(temperatureRow)
        mqttDataLayout.addWidget(humidityRow)
        mqttDataLayout.addWidget(pressureRow)
        mqttDataLayout.addWidget(lightRow)

        mqttDataLayout.setContentsMargins(0, 0, 0, 0)
        mqttDataLayout.setSpacing(0)