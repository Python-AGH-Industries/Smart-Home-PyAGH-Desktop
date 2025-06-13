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

        mqtt_data_layout = QVBoxLayout(self)

        self.temp_specs = DataRowSpecs("Temperature", ["C", "F", "K"],
                                self.create_sensor_list(1))
        self.humidity_specs = DataRowSpecs("Humidity", ["%", "g/m³", "kg/m³"],
                                self.create_sensor_list(2))
        self.pressure_specs = DataRowSpecs("Pressure", ["hPa", "bar", "atm"],
                                self.create_sensor_list(3))
        self.light_specs = DataRowSpecs("Light", ["Cd"],
                               self.create_sensor_list(4))

        self.temperature_row = MqttDataRow(self.temp_specs)
        self.humidity_row = MqttDataRow(self.humidity_specs)
        self.pressure_row = MqttDataRow(self.pressure_specs)
        self.light_row = MqttDataRow(self.light_specs)

        mqtt_data_layout.addWidget(self.temperature_row)
        mqtt_data_layout.addWidget(self.humidity_row)
        mqtt_data_layout.addWidget(self.pressure_row)
        mqtt_data_layout.addWidget(self.light_row)
        mqtt_data_layout.addStretch(2)

        mqtt_data_layout.setContentsMargins(0, 0, 0, 0)
        mqtt_data_layout.setSpacing(0)

    def create_sensor_list(self, type_id):
        response = self.login.getSensors(type_id)
        result = []
        for sensor in response["sensors"]:
            result.append((sensor["name"], sensor["id"]))
        return result