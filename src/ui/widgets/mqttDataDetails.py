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

        self.sensorSelection = LabelComboBox(
            f"Chosen {specs.title.lower()} sensor",
            specs.sensors,
            self
        )

        self.unitSelection = LabelComboBox(
            f"{specs.title} unit ",
            specs.units,
            self
        )

        self.rounder = FloatRounder()

        self.chosenPeriod = ""
        self.chosenUnit = self.specs.units[
            self.unitSelection.comboBox.currentIndex()
        ]
        self.chosenSensor = self.specs.sensors[
            self.sensorSelection.comboBox.currentIndex()
        ]

        self.labelGroup = MqttLabelGroup()
        
        self.sensorSelection.comboBox.currentTextChanged.connect(
            lambda: self.userChangedSensor.emit()
        )
        self.unitSelection.comboBox.currentTextChanged.connect(
            self.userChangedUnit.emit
        )

        layout.addWidget(self.sensorSelection)
        layout.addWidget(self.unitSelection)
        layout.addWidget(self.labelGroup)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

    def updateDetails(self, mqttData, newPeriod = None):
        if newPeriod is not None:
            self.chosenPeriod = newPeriod

        self.chosenUnit = self.specs.units[self.unitSelection.comboBox.currentIndex()]
        if len(mqttData) == 0:
            temp_mean = 0
            temp_min = 0
            temp_max = 0
        else:
            temp_mean = self.rounder.roundFloat5(sum(mqttData) / len(mqttData))
            temp_min = self.rounder.roundFloat5(min(mqttData))
            temp_max = self.rounder.roundFloat5(max(mqttData))

        self.labelGroup.setText(
            f"{temp_mean} {self.chosenUnit}", 
            f"{temp_min} {self.chosenUnit}", 
            f"{temp_max} {self.chosenUnit}"
        )
    
    def updateSensor(self):
        self.chosenSensor = self.specs.sensors[self.sensorSelection.comboBox.currentIndex()]

    def updataSensorNames(self, newNames):
        self.specs.sensors = newNames

        newItems = [item for item, _ in newNames]

        self.sensorSelection.comboBox.clear()
        self.sensorSelection.comboBox.addItems(newItems)
        self.chosenSensor = self.specs.sensors[
            self.sensorSelection.comboBox.currentIndex()
        ]