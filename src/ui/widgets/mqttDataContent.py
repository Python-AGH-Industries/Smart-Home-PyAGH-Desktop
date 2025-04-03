from PyQt6.QtWidgets import QWidget, QHBoxLayout
from src.ui.widgets.mqttDataGraph import MqttDataGraph
from src.ui.widgets.mqttDataDetails import MqttDataDetails
from src.model.unitConverter import UnitConverter
from datetime import datetime, timedelta

class MqttDataContent(QWidget):
    def __init__(self, rowSpecs, mqttData):
        super().__init__()
        dataContentLayout = QHBoxLayout(self)

        self.allMqttData = mqttData
        self.usedMqttData = mqttData
        self.specs = rowSpecs

        self.converter = UnitConverter()
        self.dataGraph = MqttDataGraph(self.specs.title)
        self.dataDetails = MqttDataDetails(self.specs)

        self.dataDetails.userChangedUnit.connect(self.onUnitsChanged)
        self.dataDetails.userChangedTimeRange.connect(self.onPeriodChanged)

        self.dataDetails.updateDetails([v for (v, _) in self.usedMqttData])
        self.onPeriodChanged()

        self.dataGraph.drawGraph(self.usedMqttData)

        dataContentLayout.addWidget(self.dataGraph, stretch = 5)
        dataContentLayout.addWidget(self.dataDetails, stretch = 4)

        dataContentLayout.setContentsMargins(0, 0, 0, 0)
        dataContentLayout.setSpacing(0)

    def onUnitsChanged(self):
        newValuesAll = self.converter.convertUnits(
                self.specs.title, 
                self.dataDetails.chosenUnit,
                self.specs.units[self.dataDetails.unitSelection.comboBox.currentIndex()], 
                [v for (v, _) in self.allMqttData]
            )
        newValuesUsed = self.converter.convertUnits(
            self.specs.title,
            self.dataDetails.chosenUnit,
            self.specs.units[self.dataDetails.unitSelection.comboBox.currentIndex()],
            [v for (v, _) in self.usedMqttData]
        )

        self.usedMqttData = list(zip(newValuesUsed, [t for _, t in self.usedMqttData]))
        self.allMqttData = list(zip(newValuesAll, [t for _, t in self.allMqttData]))

        self.dataDetails.updateDetails([v for v, _ in self.usedMqttData])
        self.dataGraph.drawGraph(self.usedMqttData)

    def onPeriodChanged(self):
        period = self.dataDetails.periods[self.dataDetails.periodSelection.comboBox.currentIndex()]
        now = datetime.now()
        offset = now

        if period == "7 days":
            offset = now - timedelta(days = 7)
        else:
            hs = int(period[: period.index("h")])
            offset = now - timedelta(hours = hs)

        self.usedMqttData = [(v, t) for v, t in self.allMqttData if t >= offset]
        self.dataDetails.updateDetails([v for v, _ in self.usedMqttData])
        self.dataGraph.drawGraph(self.usedMqttData)