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
        self.setFixedSize(400, 300)

        self.converter = UnitConverter()
        self.rounder = FloatRounder()
        self.report_periods = ["day", "week", "month"]

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

        self.period_box = LabelComboBox(
            "Include data from the last",
            self.report_periods,
            self
        )
        self.temperature_unit_box = LabelComboBox(
            "Choose temperature unit",
            temperature_specs.units,
            self
        )
        self.humidity_unit_box = LabelComboBox(
            "Choose humidity unit",
            humidity_specs.units,
            self
        )
        self.pressure_unit_box = LabelComboBox(
            "Choose pressure unit",
            pressure_specs.units,
            self
        )
        self.light_unit_box = LabelComboBox(
            "Choose light unit",
            light_specs.units,
            self
        )

        button_layout = QHBoxLayout()
        self.cancel_button = QPushButton("Cancel")
        self.ok_button = QPushButton("Generate")

        self.ok_button.clicked.connect(self.generate_report)

        button_layout.addStretch()
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.ok_button)

        layout.addWidget(self.label)
        layout.addWidget(self.period_box)
        layout.addWidget(self.temperature_unit_box)
        layout.addWidget(self.humidity_unit_box)
        layout.addWidget(self.pressure_unit_box)
        layout.addWidget(self.light_unit_box)
        layout.addStretch(1)
        layout.addLayout(button_layout)

        self.cancel_button.clicked.connect(self.reject)
        self.ok_button.clicked.connect(self.accept)

    def generate_report(self):
        self.period = self.period_box.combo_box.currentText()
        self.temperature_unit = self.temperature_unit_box.combo_box.currentText()
        self.pressure_unit = self.pressure_unit_box.combo_box.currentText()
        self.humidity_unit = self.humidity_unit_box.combo_box.currentText()
        self.light_unit = self.light_unit_box.combo_box.currentText()

        self.filter_by_timerange()
        file_name = self.create_report_on_disk()

        if file_name:
            if not file_name.lower().endswith(".md"):
                file_name += ".md"

            fp = open(file_name, "w+")
            self.write_report(fp)
            fp.close()

    def write_report(self, file):
        self.write_report_header(file)
        self.write_report_sensor_data(
            file,
            self.data[0],
            "Temperature",
            self.temperature_unit,
            "C"
        )
        self.write_sensor_closure(
            file,
            self.data[0],
            "temperature",
            self.temperature_unit,
            [0, 35]
        )
        self.write_report_sensor_data(
            file,
            self.data[1],
            "Humidity",
            self.humidity_unit,
            "%"
        )
        self.write_sensor_closure(
            file,
            self.data[1],
            "humidity",
            self.humidity_unit,
            [25, 70]
        )
        self.write_report_sensor_data(
            file,
            self.data[2],
            "Pressure",
            self.pressure_unit,
            "hPa"
        )
        self.write_sensor_closure(
            file,
            self.data[2],
            "pressure",
            self.pressure_unit,
            [980, 1030]
        )
        self.write_report_sensor_data(
            file,
            self.data[3],
            "Light",
            self.light_unit,
            "Cd"
        )
        self.write_sensor_closure(
            file,
            self.data[3],
            "light",
            self.light_unit,
            [100, 50000]
        )

    def write_report_header(self, file):
        header_text = f"# Report from {datetime.now().strftime("%d-%m-%Y %H:%M")} " \
                      f"for {Login.getCurrentUser().username}\n"
        file.write(header_text)

        intro_text = f"Thank you for sticking with our offer! " \
                        f"Here is you report from the last {self.period}.\n"
        file.write(intro_text)

    def write_report_sensor_data(self, file, sensor_data, header, unit, base_unit):
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
                base_unit,
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
                base_unit,
                unit,
                [max_value]
            )

            max_value = self.rounder.roundFloat5(max_value)

            row_max += f"|{max_value} {unit}"

        row_max += "|\n"
        file.write(row_max)

        row_mean = "|AVG"
        for name, value_list in sensor_data:
            mean_value = round(
                sum([value for value, _ in value_list]) / len(value_list),
                2
            )

            [mean_value] = self.converter.convertUnits(
                header,
                base_unit,
                unit,
                [mean_value]
            )

            mean_value = self.rounder.roundFloat5(mean_value)

            row_mean += f"|{mean_value} {unit}"
            
        row_mean += "|\n"
        file.write(row_mean)

    def write_sensor_closure(self, file, sensor_data, title, unit, extremes):
        def format_time_interval(dates):
            formatted_dates = [
                str(d).split(".")[0] for d in dates
            ]
            
            if len(formatted_dates) == 1:
                return f"on {formatted_dates[0]}"
            return f"from {formatted_dates[0]} to {formatted_dates[-1]}"
        
        file.write("\n")
        [base_low, base_high] = extremes 

        for sensor_name, readings in sensor_data:
            negatives = [(v, d) for v, d in readings if v < base_low]
            highs = [(v, d) for v, d in readings if v >= base_high]

            [extreme_low, extreme_high] = self.converter.convertTemperature(
                "C",
                unit,
                extremes
            )

            extreme_low = self.rounder.roundFloat5(extreme_low)
            extreme_high = self.rounder.roundFloat5(extreme_high)

            if negatives:
                dates = [d for _, d in negatives]
                interval = format_time_interval(dates)
                file.write(f"Sensor {sensor_name} recorded extremely low " \
                           f"{title} {interval}, below {extreme_low} {unit} " \
                           f"({len(negatives)} occurrence(s)).\n")

            if highs:
                dates = [d for _, d in highs]
                interval = format_time_interval(dates)
                file.write(f"Sensor {sensor_name} recorded high {title} " \
                           f"(≥ {extreme_high} {unit}) {interval} ({len(highs)} occurrence(s)).\n")

            if not negatives and not highs:
                file.write(f"Sensor {sensor_name} had no extreme " \
                           f"{title} readings.\n")

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