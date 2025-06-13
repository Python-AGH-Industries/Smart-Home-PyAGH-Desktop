from datetime import time

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QFileDialog

from src.model.loginController import LoginController
from src.ui.widgets.mqttDataGraph import MqttDataGraph
from src.ui.widgets.mqttDataDetails import MqttDataDetails
from src.model.unitConverter import UnitConverter
from datetime import datetime, timedelta
import pyqtgraph.exporters
import json

class MqttDataContent(QWidget):
    COLOR_MAP = {
        "red": "#fc0303",
        "black": "#000000",
        "white": "#f0f0f0"
    }

    BACKGROUND_MAP = {
        "midnight": "#283c5a",
        "navy": "#325078",
        "slate": "#506ea0"
    }

    def __init__(self, row_specs):
        super().__init__()
        data_content_layout = QHBoxLayout(self)
        self.current_sensor = row_specs.sensors[0][1]

        # downloading data from server
        controller = LoginController()
        mqtt_data = controller.getSensorData(self.current_sensor)
        mqtt_data = mqtt_data["sensor_data"]
        mqtt_data = list(
            map(
                lambda x: (
                    x['measurementValue'],
                    datetime.combine(
                        datetime.strptime(
                            x['measurementDate'],
                            '%a, %d %b %Y %H:%M:%S GMT'
                        ),
                        time.fromisoformat(x['measurementTime'])
                    )
                ),
                mqtt_data
            )
        )

        if len(mqtt_data) == 0:
            mqtt_data.append((1, datetime.now()))

        mqtt_data.sort(key = lambda x: x[1])

        self.all_mqtt_data = mqtt_data
        self.used_mqtt_data = mqtt_data
    
        self.specs = row_specs

        self.converter = UnitConverter()
        self.data_graph = MqttDataGraph(self.specs.title)
        self.data_details = MqttDataDetails(self.specs)

        self.data_details.userChangedUnit.connect(self.onUnitsChanged)
        self.data_details.userChangedSensor.connect(self.onSensorChanged)

        self.data_details.updateDetails([v for (v, _) in self.used_mqtt_data])

        data_content_layout.addWidget(self.data_graph, stretch = 5)
        data_content_layout.addWidget(self.data_details, stretch = 4)

        data_content_layout.setContentsMargins(0, 0, 0, 0)
        data_content_layout.setSpacing(0)

        # downloading data
        self.timer = QTimer(self)
        self.timer.setInterval(10000)  # 5000 ms = 5 seconds
        self.timer.timeout.connect(lambda: self.getData(self.current_sensor))
        self.timer.start()

    def getData(self, sensor_id):
        controller = LoginController()
        mqtt_data = controller.getSensorData(sensor_id)
        mqtt_data = mqtt_data["sensor_data"]
        mqtt_data = list(
            map(
                lambda x: (
                    x['measurementValue'],
                    datetime.combine(
                        datetime.strptime(
                            x['measurementDate'],
                            '%a, %d %b %Y %H:%M:%S GMT'
                        ),
                        time.fromisoformat(x['measurementTime'])
                    )
                ),
                mqtt_data
            )
        )
        
        if len(mqtt_data) == 0:
            mqtt_data.append((1, datetime.now()))

        mqtt_data.sort(key = lambda x: x[1])

        self.all_mqtt_data = mqtt_data
        self.used_mqtt_data = mqtt_data
        self.onPeriodChanged(self.current_period)

    def onSensorChanged(self):
        self.data_details.updateSensor()
        self.getData(self.data_details.chosen_sensor[1])
        self.onPeriodChanged(self.current_period)

    def onUnitsChanged(self):
        newValuesAll = self.converter.convertUnits(
                self.specs.title, 
                self.data_details.chosen_unit,
                self.specs.units[
                    self.data_details.unit_selection.combo_box.currentIndex()
                ],
                [v for (v, _) in self.all_mqtt_data]
            )
        
        newValuesUsed = self.converter.convertUnits(
                self.specs.title,
                self.data_details.chosen_unit,
                self.specs.units[
                    self.data_details.unit_selection.combo_box.currentIndex()
                ],
                [v for (v, _) in self.used_mqtt_data]
            )

        self.used_mqtt_data = list(zip(
            newValuesUsed,
            [t for _, t in self.used_mqtt_data]
        ))

        self.all_mqtt_data = list(zip(
            newValuesAll,
            [t for _, t in self.all_mqtt_data]
        ))

        self.data_details.updateDetails([v for v, _ in self.used_mqtt_data])
        self.data_graph.drawGraph(self.used_mqtt_data)

    def onPeriodChanged(self, new_period):
        self.current_period = new_period
        now = datetime.now()
        offset = now

        if new_period == "7 days":
            offset = now - timedelta(days = 7)
        else:
            hs = int(new_period[: new_period.index("h")])
            offset = now - timedelta(hours = hs)

        self.used_mqtt_data = [(v, t) for v, t in self.all_mqtt_data if t >= offset]
        self.data_details.updateDetails([v for v, _ in self.used_mqtt_data], new_period)
        
        self.data_graph.drawGraph(self.used_mqtt_data)

    def updateColor(self, new_color):
        self.data_graph.changePenColor(self.COLOR_MAP[new_color])

    def updateBackground(self, new_color):
        self.data_graph.changeGraphBackground(self.BACKGROUND_MAP[new_color])

    def saveDataInJson(self):
        json_data = {}
        json_data[self.specs.title] = {}

        for value, time in self.used_mqtt_data:
            json_data[self.specs.title][str(time)] = value

        json_data = json.dumps(json_data, indent = 4)

        response = QFileDialog.getSaveFileName(
            parent = self,
            caption = "Select location to save",
            filter = "JSON Files (*.json);;All Files (*)"
        )

        file_name = response[0]

        if file_name:
            if not file_name.lower().endswith(".json"):
                file_name += ".json"

            file = open(file_name, "w")
            file.write(json_data)
            file.close()

    def saveDataInCsv(self):
        csv_data = []
        csv_data.append(("Date", f"{self.specs.title} value"))

        for value, time in self.used_mqtt_data:
            csv_data.append((time, value))

        response = QFileDialog.getSaveFileName(
            parent = self,
            caption = "Select location to save",
            filter = "CSV Files (*.csv);;All Files (*)"
        )

        file_name = response[0]

        if file_name:
            if not file_name.lower().endswith(".csv"):
                file_name += ".csv"

            file = open(file_name, "w+")
            for time, value in csv_data:
                file.write(f"{time},{value}\n")
            file.close()

    def saveDataInPng(self):
        response = QFileDialog.getSaveFileName(
            parent = self,
            caption = "Select location to save",
            filter = "PNG Files (*.png);;All Files (*)"
        )

        file_name = response[0]

        if file_name:
            if not file_name.lower().endswith(".png"):
                file_name += ".png"

            exporter = pyqtgraph.exporters.ImageExporter(
                self.data_graph.plot_widget.plotItem
            )
            
            exporter.export(file_name)
