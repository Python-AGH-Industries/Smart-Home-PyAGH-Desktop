from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from src.ui.widgets.labelComboBox import LabelComboBox
from PyQt6.QtCore import pyqtSignal
from src.model.floatRounder import FloatRounder

class MqttDataDetails(QWidget):
    userChangedUnit = pyqtSignal()
    userChangedTimeRange = pyqtSignal()

    def __init__(self, specs):
        super().__init__()
        self.specs = specs
        layout = QVBoxLayout(self)
        self.periods = ["4h", "8h", "12h", "24h", "48h", "7 days"]

        self.sensorSelection = LabelComboBox(f"Chosen {specs.title.lower()}" 
                                            f" sensor", specs.sensors, self)
        self.periodSelection = LabelComboBox("Showing " + specs.title.lower() +
                                        " from the last", self.periods, self)
        self.unitSelection = LabelComboBox(specs.title + " unit ", specs.units, self)

        self.rounder = FloatRounder()

        self.chosenPeriod = self.periods[self.periodSelection.comboBox.currentIndex()]
        self.chosenUnit = specs.units[self.unitSelection.comboBox.currentIndex()]

        self.meanLabel = QLabel("", self)
        self.minLabel = QLabel("", self)
        self.maxLabel = QLabel("", self)
        
        self.unitSelection.comboBox.currentTextChanged.connect(self.onUnitsChanged)

        layout.addWidget(self.sensorSelection)
        layout.addWidget(self.periodSelection)
        layout.addWidget(self.unitSelection)
        layout.addWidget(self.meanLabel)
        layout.addWidget(self.minLabel)
        layout.addWidget(self.maxLabel)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

    def updateDetails(self, mqttData):
        self.chosenUnit = self.specs.units[self.unitSelection.comboBox.currentIndex()]
        print(mqttData)
        temp_mean = self.rounder.roundFloat5(sum(mqttData) / len(mqttData))
        temp_min = self.rounder.roundFloat5(min(mqttData))
        temp_max = self.rounder.roundFloat5(max(mqttData))

        self.meanLabel.setText(f"Last {self.chosenPeriod} mean is {temp_mean} {self.chosenUnit}")
        self.minLabel.setText(f"Last {self.chosenPeriod} minimum is {temp_min} {self.chosenUnit}")
        self.maxLabel.setText(f"Last {self.chosenPeriod} maximum is {temp_max} {self.chosenUnit}")

    def onUnitsChanged(self):
        self.userChangedUnit.emit()