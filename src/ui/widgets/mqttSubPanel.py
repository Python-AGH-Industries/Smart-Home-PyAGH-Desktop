from PyQt6.QtWidgets import QWidget, QVBoxLayout
from src.ui.widgets.mqttDataRow import MqttDataRow
from src.model.dataRowSpecs import DataRowSpecs
from random import randint

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

        tempData = [(round(randint(100, 350) / 10, 3), i + 1) for i in range(10)]
        humiData = [(round(randint(100, 300) / 10, 3), i + 1) for i in range(10)]
        presData = [(round(randint(980000, 1030000) / 100, 3), i + 1) for i in range(10)]
        lighData = [(round(randint(3000, 12000), 3), i + 1) for i in range(10)]

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