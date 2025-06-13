from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from src.ui.widgets.labelComboBox import LabelComboBox
from PyQt6.QtCore import pyqtSignal
from src.model.floatRounder import FloatRounder
from src.ui.widgets.mqttLabelGroup import MqttLabelGroup

class MqttDataDetails(QWidget):
    userChangedUnit = pyqtSignal()
    userChangedSensor = pyqtSignal()

    def __init__(self, specs):
        super().__init__()
        self.specs = specs
        layout = QVBoxLayout(self)

        self.sensor_selection = LabelComboBox(
            f"Chosen {specs.title.lower()} sensor",
            [name for name, _ in self.specs.sensors],
            self
        )

        self.unit_selection = LabelComboBox(
            f"{specs.title} unit ",
            specs.units,
            self
        )

        self.rounder = FloatRounder()

        self.chosen_period = ""
        self.chosen_unit = self.specs.units[
            self.unit_selection.combo_box.currentIndex()
        ]
        self.chosen_sensor = self.specs.sensors[
            self.sensor_selection.combo_box.currentIndex()
        ]

        self.label_group = MqttLabelGroup()
        
        self.sensor_selection.combo_box.currentTextChanged.connect(
            lambda: self.userChangedSensor.emit()
        )
        self.unit_selection.combo_box.currentTextChanged.connect(
            self.userChangedUnit.emit
        )

        layout.addWidget(self.sensor_selection)
        layout.addWidget(self.unit_selection)
        layout.addWidget(self.label_group)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

    def updateDetails(self, mqtt_data, new_period = None):
        if new_period is not None:
            self.chosen_period = new_period

        self.chosen_unit = self.specs.units[self.unit_selection.combo_box.currentIndex()]
        if len(mqtt_data) == 0:
            temp_mean = 0
            temp_min = 0
            temp_max = 0
        else:
            temp_mean = self.rounder.roundFloat5(sum(mqtt_data) / len(mqtt_data))
            temp_min = self.rounder.roundFloat5(min(mqtt_data))
            temp_max = self.rounder.roundFloat5(max(mqtt_data))

        self.label_group.setText(
            f"{temp_mean} {self.chosen_unit}", 
            f"{temp_min} {self.chosen_unit}", 
            f"{temp_max} {self.chosen_unit}"
        )
    
    def updateSensor(self):
        self.chosen_sensor = self.specs.sensors[
            self.sensor_selection.combo_box.currentIndex()
        ]

    def updataSensorNames(self, newNames):
        self.specs.sensors = newNames

        newItems = [item for item, _ in newNames]

        self.sensor_selection.combo_box.clear()
        self.sensor_selection.combo_box.addItems(newItems)
        self.chosen_sensor = self.specs.sensors[
            self.sensor_selection.combo_box.currentIndex()
        ]