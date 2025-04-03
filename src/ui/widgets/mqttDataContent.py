from PyQt6.QtWidgets import QWidget, QHBoxLayout
from src.ui.widgets.mqttDataGraph import MqttDataGraph
from src.ui.widgets.mqttDataDetails import MqttDataDetails
from src.model.unitConverter import UnitConverter

class MqttDataContent(QWidget):
    def __init__(self, rowSpecs, mqttData):
        super().__init__()
        dataContentLayout = QHBoxLayout(self)

        self.mqttData = mqttData
        self.specs = rowSpecs
        self.converter = UnitConverter()

        self.dataGraph = MqttDataGraph(self.specs.title)
        self.dataDetails = MqttDataDetails(self.specs)

        self.dataDetails.userChangedUnit.connect(self.onUnitsChanged)
        self.dataDetails.updateDetails([v for (v, _) in self.mqttData])
        self.dataGraph.drawGraph([v for (v, _) in mqttData], [t.timestamp() for (_, t) in mqttData])

        dataContentLayout.addWidget(self.dataGraph, stretch = 5)
        dataContentLayout.addWidget(self.dataDetails, stretch = 4)

        dataContentLayout.setContentsMargins(0, 0, 0, 0)
        dataContentLayout.setSpacing(0)

    def onUnitsChanged(self):
        newValues = self.converter.convertUnits(
                self.specs.title, 
                self.dataDetails.chosenUnit, 
                self.specs.units[self.dataDetails.unitSelection.comboBox.currentIndex()], 
                [v for (v, _) in self.mqttData]
            )
        self.mqttData = [(v, t) for v, t in zip(newValues, self.mqttData)]
        self.dataDetails.updateDetails(newValues)
        self.dataGraph.updateGraphValues(newValues)