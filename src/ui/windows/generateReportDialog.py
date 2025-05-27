from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QCheckBox,
                             QPushButton, QHBoxLayout, QFileDialog)
from src.ui.widgets.labelComboBox import LabelComboBox
from src.model.loginController import LoginController 
from datetime import datetime, timedelta, time
from src.ui.widgets.login import Login
from src.model.unitConverter import UnitConverter
from src.model.floatRounder import FloatRounder

class GenerateReportDialog(QDialog):
    def __init__(self, specs, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Your report")
        self.setFixedSize(400, 600)

        self.converter = UnitConverter()
        self.rounder = FloatRounder()
        self.reportPeriods = ["day", "week", "month"]

        temperature_specs, humidity_specs, pressure_specs, light_specs = specs

        self.temperature_data, self.humidity_data = [], []
        self.pressure_data, self.light_data = [], []

        self.data = [
            self.temperature_data,
            self.humidity_data,
            self.pressure_data,
            self.light_data
        ]

        controller = LoginController()

        for d, spec in zip(self.data, specs):
            for name, id in spec.sensors:
                mqttData = controller.getSensorData(id)
                mqttData = mqttData["sensor_data"]
                mqttData = list(
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
                        mqttData
                    )
                )
                mqttData.sort(key = lambda x : x[1])
                d.append((name, mqttData))

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        self.label = QLabel("Report generation")

        self.publicDataFlag = QCheckBox("Include public data", self)
        self.includeGraphsFlag = QCheckBox("Include graphs", self)

        self.periodBox = LabelComboBox(
            "Include data from the last",
            self.reportPeriods,
            self
        )
        self.temperatureUnitBox = LabelComboBox(
            "Choose temperature unit",
            temperature_specs.units,
            self
        )
        self.humidityUnitBox = LabelComboBox(
            "Choose humidity unit",
            humidity_specs.units,
            self
        )
        self.pressureUnitBox = LabelComboBox(
            "Choose pressure unit",
            pressure_specs.units,
            self
        )
        self.lightUnitBox = LabelComboBox(
            "Choose light unit",
            light_specs.units,
            self
        )

        buttonLayout = QHBoxLayout()
        self.cancelButton = QPushButton("Cancel")
        self.okButton = QPushButton("Generate")

        self.okButton.clicked.connect(self.generate_report)

        buttonLayout.addStretch()
        buttonLayout.addWidget(self.cancelButton)
        buttonLayout.addWidget(self.okButton)

        layout.addWidget(self.label)
        layout.addWidget(self.periodBox)
        layout.addWidget(self.temperatureUnitBox)
        layout.addWidget(self.humidityUnitBox)
        layout.addWidget(self.pressureUnitBox)
        layout.addWidget(self.lightUnitBox)
        layout.addWidget(self.publicDataFlag)
        layout.addWidget(self.includeGraphsFlag)
        layout.addStretch(1)
        layout.addLayout(buttonLayout)

        self.cancelButton.clicked.connect(self.reject)
        self.okButton.clicked.connect(self.accept)

    def generate_report(self):
        self.period = self.periodBox.comboBox.currentText()
        self.temperature_unit = self.temperatureUnitBox.comboBox.currentText()
        self.pressure_unit = self.pressureUnitBox.comboBox.currentText()
        self.humidity_unit = self.humidityUnitBox.comboBox.currentText()
        self.light_unit = self.lightUnitBox.comboBox.currentText()

        self.filter_by_timerange()
        file_name = self.create_report_on_disk()

        if file_name:
            if not file_name.lower().endswith(".md"):
                file_name += ".md"

            fp = open(file_name, "w+")
            self.write_report(fp)
            fp.close()

    def print_data(self):
        for sensors_data in self.data:
            for name, values in sensors_data:
                for reading, date in values:
                    print(name, reading, date)

    def write_report(self, file):
        self.write_report_header(file)
        self.write_report_sensor_data(
            file,
            self.data[0],
            "Temperature",
            self.temperature_unit,
            "C"
        )
        self.write_report_sensor_data(
            file,
            self.data[1],
            "Humidity",
            self.humidity_unit,
            "%"
        )
        self.write_report_sensor_data(
            file,
            self.data[2],
            "Pressure",
            self.pressure_unit,
            "hPa"
        )
        self.write_report_sensor_data(
            file,
            self.data[3],
            "Light",
            self.light_unit,
            "Cd"
        )

    def write_report_header(self, file):
        header_text = f"# Report from {datetime.now().strftime("%d-%m-%Y %H:%M")} " \
                      f"for {Login.getCurrentUser().username}\n"
        file.write(header_text)

        intro_text = f"Thank you for sticking with our offer! " \
                        f"Here is you report from the last {self.period}.\n"
        file.write(intro_text)

    def write_report_sensor_data(self, file, sensor_data, header, unit, baseUnit):
        temperature_header = f"\n## {header} data\n"
        file.write(temperature_header)
        
        sensor_count = len(sensor_data)

        temperature_intro = f"You have {sensor_count} {header.lower()} " \
                            f"sensors in your place. " \
                            f"Let's see what they measured!\n"
        file.write(temperature_intro)

        table_header = "|"
        for name, _ in sensor_data:
            table_header += f"|{name}"
        table_header += "|\n"
        file.write(table_header)

        table_sep = "|---"
        for _ in sensor_data:
            table_sep += "|---"
        table_sep += "|\n"
        file.write(table_sep)

        row_min = "|MIN"
        for name, value_list in sensor_data:
            min_value, _ = min(
                value_list,
                key = lambda x : x[0]
            )

            [min_value] = self.converter.convertUnits(
                header,
                baseUnit,
                unit,
                [min_value]
            )

            min_value = self.rounder.roundFloat5(min_value)

            row_min += f"|{min_value} {unit}"

        row_min += "|\n"
        file.write(row_min)

        row_max = "|MAX"
        for name, value_list in sensor_data:
            max_value, _ = max(
                value_list,
                key = lambda x : x[0]
            )

            [max_value] = self.converter.convertUnits(
                header,
                baseUnit,
                unit,
                [max_value]
            )

            max_value = self.rounder.roundFloat5(max_value)

            row_max += f"|{max_value} {unit}"

        row_max += "|\n"
        file.write(row_max)

        row_mean = "|MEAN"
        for name, value_list in sensor_data:
            mean_value = round(
                sum([value for value, _ in value_list]) / len(value_list),
                2
            )

            [mean_value] = self.converter.convertUnits(
                header,
                baseUnit,
                unit,
                [mean_value]
            )

            mean_value = self.rounder.roundFloat5(mean_value)

            row_mean += f"|{mean_value} {unit}"
            
        row_mean += "|\n"
        file.write(row_mean)

    def create_report_on_disk(self):
        return QFileDialog.getSaveFileName(
            parent = self,
            caption = "Select location for you report",
            filter = "MD Files (*.md);;All Files (*)"
        )[0]

    def filter_by_timerange(self):
        if self.period == "day": offset = timedelta(days = 1)
        elif self.period == "week": offset = timedelta(weeks = 1)
        else: offset = timedelta(weeks = 4)

        now = datetime.now()
        
        # list[list[tuple[SENSOR_NAME, list[tuple[READING, DATE]]]]]
        for sensors_data in self.data:
            for i, (name, values) in enumerate(sensors_data):
                filtered_values = [
                    (reading, date) for reading, date in values 
                    if now - offset <= date <= now
                ]
                sensors_data[i] = (name, filtered_values)