from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QCheckBox,
                             QPushButton, QHBoxLayout)
from src.ui.widgets.labelComboBox import LabelComboBox
from src.model.loginController import LoginController 

class GenerateReportDialog(QDialog):
    def __init__(self, specs, periods, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Your report")
        self.setFixedSize(400, 600)

        temperature_specs, humidity_specs, pressure_specs, light_specs = specs
        self.temperature_data, self.humidity_data = [], []
        self.pressure_data, self.light_data = [], []

        controller = LoginController()
        
        for name, id in temperature_specs.sensors:
            self.temperature_data.append((name, controller.getSensorData(id)))

        for name, id in humidity_specs.sensors:
            self.humidity_data.append((name, controller.getSensorData(id)))

        for name, id in pressure_specs.sensors:
            self.pressure_data.append((name, controller.getSensorData(id)))

        for name, id in light_specs.sensors:
            self.light_data.append((name, controller.getSensorData(id)))

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        self.label = QLabel("Report generation")

        self.publicDataFlag = QCheckBox("Include public data", self)
        self.includeGraphsFlag = QCheckBox("Include graphs", self)

        self.periodBox = LabelComboBox(
            "Choose period to consider",
            periods,
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
        period = self.periodBox.comboBox.currentText()
        temperature_unit = self.temperatureUnitBox.comboBox.currentText()
        humidity_unit = self.humidityUnitBox.comboBox.currentText()
        pressure_unit = self.pressureUnitBox.comboBox.currentText()
        light_unit = self.lightUnitBox.comboBox.currentText()

        for name, sensor_data in self.temperature_data:
            for _, values in sensor_data.items():
                for val in values:
                    print(name, val)

        print(period, temperature_unit, humidity_unit, pressure_unit, light_unit)