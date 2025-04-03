from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from src.ui.widgets.labelComboBox import LabelComboBox
from src.model.unitConverter import UnitConverter

class MqttDataDetails(QWidget):
    def __init__(self, specs, mqttData,changeTimeFrame,changeUnits):
        super().__init__()
        self.specs = specs
        self.changeTimeFrame = changeTimeFrame
        self.changeUnits = changeUnits
        layout = QVBoxLayout(self)
        periods = ["4h", "8h", "12h", "24h", "48h", "7 days"]

        self.sensorSelection = LabelComboBox("Chosen " + specs.title.lower() + 
                                            " sensor", specs.sensors, self)
        self.periodSelection = LabelComboBox("Showing " + specs.title.lower() +
                                        " from the last", periods, self)
        self.unitSelection = LabelComboBox(specs.title + " unit ", specs.units, self)

        self.chosenPeriod = periods[self.periodSelection.comboBox.currentIndex()]
        self.chosenUnit = specs.units[self.unitSelection.comboBox.currentIndex()]

        self.times = [t for (_, t) in mqttData]
        self.data = [d for (d, _) in mqttData]

        self.meanLabel = QLabel("", self)
        self.minLabel = QLabel("", self)
        self.maxLabel = QLabel("", self)
        
        self.updateDetails()
        
        self.converter = UnitConverter()
        self.unitSelection.comboBox.currentTextChanged.connect(self.onUnitsChanged)
        self.periodSelection.comboBox.currentTextChanged.connect(self.onTimeframeChanged)

        layout.addWidget(self.sensorSelection)
        layout.addWidget(self.periodSelection)
        layout.addWidget(self.unitSelection)
        layout.addWidget(self.meanLabel)
        layout.addWidget(self.minLabel)
        layout.addWidget(self.maxLabel)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

    def updateDetails(self):
        self.meanLabel.setText("Last " + self.chosenPeriod + " mean: " + 
                            str(round(sum(self.data) / len(self.data), 3)) + " " + self.chosenUnit)
        self.minLabel.setText("Last " + self.chosenPeriod + " minimum: " +
                            str(round(min(self.data), 3)) + " " + self.chosenUnit)
        self.maxLabel.setText("Last " + self.chosenPeriod + " maximum: " +
                            str(round(max(self.data), 3)) + " " + self.chosenUnit)

    def onUnitsChanged(self, newText):
        self.data = self.converter.convertUnits(self.specs.title, self.chosenUnit, 
                                    newText, self.data)
        self.chosenUnit = newText
        print(self.chosenUnit)
        self.changeUnits(self.chosenUnit)

    def onTimeframeChanged(self,newText):
        self.chosenPeriod = newText
        print(self.chosenPeriod)
        self.changeTimeFrame(newText)