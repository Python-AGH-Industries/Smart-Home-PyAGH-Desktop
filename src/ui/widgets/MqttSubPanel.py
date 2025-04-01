from PyQt6.QtWidgets import QWidget, QVBoxLayout
from src.ui.widgets.mqttDataRow import MqttDataRow

class MqttSubPanel(QWidget):
    def __init__(self):
        super().__init__()
        mqttDataLayout = QVBoxLayout(self)

        temperatureRow = MqttDataRow("Temperature", ["C", "F", "K"])
        humidityRow = MqttDataRow("Humidity", ["%", "g/m³", "kg/m³"])
        pressureRow = MqttDataRow("Pressure", ["Pa", "bar", "psi", "atm", "mmHg"])
        lightRow = MqttDataRow("Light", ["Lm", "Lx", "Cd"])

        mqttDataLayout.addWidget(temperatureRow)
        mqttDataLayout.addWidget(humidityRow)
        mqttDataLayout.addWidget(pressureRow)
        mqttDataLayout.addWidget(lightRow)

        mqttDataLayout.setContentsMargins(0, 0, 0, 0)
        mqttDataLayout.setSpacing(0)