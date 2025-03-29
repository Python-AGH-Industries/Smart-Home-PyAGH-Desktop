from PyQt6.QtWidgets import QWidget, QVBoxLayout
from src.ui.widgets.mqttDataRow import MqttDataRow

class MqttData(QWidget):
    def __init__(self):
        super().__init__()
        mqttDataLayout = QVBoxLayout(self)

        temperatureRow = MqttDataRow("Temperature")
        humidityRow = MqttDataRow("Humidity")
        pressureRow = MqttDataRow("Pressure")
        lightRow = MqttDataRow("Light")

        mqttDataLayout.addWidget(temperatureRow)
        mqttDataLayout.addWidget(humidityRow)
        mqttDataLayout.addWidget(pressureRow)
        mqttDataLayout.addWidget(lightRow)

        mqttDataLayout.setContentsMargins(0, 0, 0, 0)
        mqttDataLayout.setSpacing(0)