from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from src.ui.widgets.labelComboBox import LabelComboBox
from PyQt6.QtCore import pyqtSignal
from src.model.floatRounder import FloatRounder

class MqttDataDetails(QWidget):
    userChangedUnit = pyqtSignal()
    userChangedTimeRange = pyqtSignal()
    userChangedPenColor = pyqtSignal()
    userChangedBackgroundColor = pyqtSignal()

    def __init__(self, specs):
        super().__init__()
        self.specs = specs
        layout = QVBoxLayout(self)
        self.periods = ["4h", "8h", "12h", "24h", "48h", "7 days"]
        self.colors = ["red", "black", "white"]
        self.backgrounds = ["white", "gray", "black"] 

        self.sensorSelection = LabelComboBox(f"Chosen {specs.title.lower()}" 
                                            f" sensor", specs.sensors, self)
        self.periodSelection = LabelComboBox(f"Showing {specs.title.lower()}"
                                        f" from the last", self.periods, self)
        self.unitSelection = LabelComboBox(f"{specs.title} unit ", specs.units, self)
        self.colorSelection = LabelComboBox(f"{specs.title} graph color ", self.colors, self)
        self.backgroundSelection = LabelComboBox(f"{specs.title} graph background ", self.backgrounds, self)

        self.rounder = FloatRounder()

        self.chosenPeriod = self.periods[self.periodSelection.comboBox.currentIndex()]
        self.chosenUnit = specs.units[self.unitSelection.comboBox.currentIndex()]

        self.meanLabel = QLabel("", self)
        self.meanLabel.setWordWrap(True)
        
        self.unitSelection.comboBox.currentTextChanged.connect(self.onUnitsChanged)
        self.periodSelection.comboBox.currentTextChanged.connect(self.onPeriodChanged)
        self.colorSelection.comboBox.currentTextChanged.connect(self.onColorChanged)
        self.backgroundSelection.comboBox.currentTextChanged.connect(self.onBackgroundChanged)

        layout.addWidget(self.sensorSelection)
        layout.addWidget(self.periodSelection)
        layout.addWidget(self.unitSelection)
        layout.addWidget(self.colorSelection)
        layout.addWidget(self.backgroundSelection)
        layout.addWidget(self.meanLabel)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

    def updateDetails(self, mqttData):
        self.chosenUnit = self.specs.units[self.unitSelection.comboBox.currentIndex()]
        self.chosenPeriod = self.periods[self.periodSelection.comboBox.currentIndex()]
        temp_mean = self.rounder.roundFloat5(sum(mqttData) / len(mqttData))
        temp_min = self.rounder.roundFloat5(min(mqttData))
        temp_max = self.rounder.roundFloat5(max(mqttData))

        self.meanLabel.setText(f"Last {self.chosenPeriod} mean = {temp_mean} {self.chosenUnit}, "
                               f"minimum = {temp_min} {self.chosenUnit}, "
                               f"maximum = {temp_max} {self.chosenUnit}")

    def onUnitsChanged(self):
        self.userChangedUnit.emit()

    def onPeriodChanged(self):
        self.userChangedTimeRange.emit()

    def onColorChanged(self):
        self.userChangedPenColor.emit()

    def onBackgroundChanged(self):
        self.userChangedBackgroundColor.emit()