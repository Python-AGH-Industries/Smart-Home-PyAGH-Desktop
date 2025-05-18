from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QCheckBox,
                             QPushButton, QHBoxLayout, QFileDialog)
from src.ui.widgets.labelComboBox import LabelComboBox
from src.model.loginController import LoginController 
from datetime import datetime, timedelta, time
from src.ui.widgets.login import Login

class GenerateReportDialog(QDialog):
    def __init__(self, specs, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Your report")
        self.setFixedSize(400, 600)

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
        self.filter_by_timerange()
        file_name = self.create_report_on_disk()

        if file_name:
            if not file_name.lower().endswith(".md"):
                file_name += ".md"

            fp = open(file_name, "w+")
            self.write_report_content(fp)
            fp.close()

    def print_data(self):
        for sensors_data in self.data:
            for name, values in sensors_data:
                for reading, date in values:
                    print(name, reading, date)

    def write_report_content(self, file):
        header_text = f"# Report from {datetime.now()} " \
                      f"for user {Login.getCurrentUser().username}"
        file.write(header_text)

    def create_report_on_disk(self):
        return QFileDialog.getSaveFileName(
            parent = self,
            caption = "Select location for you report",
            filter = "MD Files (*.md);;All Files (*)"
        )[0]

    def filter_by_timerange(self):
        period = self.periodBox.comboBox.currentText()

        if period == "day": offset = timedelta(days = 1)
        elif period == "week": offset = timedelta(weeks = 1)
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