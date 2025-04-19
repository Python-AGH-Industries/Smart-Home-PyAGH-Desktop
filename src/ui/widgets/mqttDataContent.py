from PyQt6.QtWidgets import QWidget, QHBoxLayout, QFileDialog
from src.ui.widgets.mqttDataGraph import MqttDataGraph
from src.ui.widgets.mqttDataDetails import MqttDataDetails
from src.model.unitConverter import UnitConverter
from datetime import datetime, timedelta
import pyqtgraph.exporters
import json

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

        self.dataDetails.updateDetails([v for (v, _) in self.usedMqttData])

        self.dataGraph.drawGraph(self.usedMqttData)

        dataContentLayout.addWidget(self.dataGraph, stretch = 5)
        dataContentLayout.addWidget(self.dataDetails, stretch = 4)

        dataContentLayout.setContentsMargins(0, 0, 0, 0)
        dataContentLayout.setSpacing(0)

    def onUnitsChanged(self):
        newValuesAll = self.converter.convertUnits(
                self.specs.title, 
                self.dataDetails.chosenUnit,
                self.specs.units[
                    self.dataDetails.unitSelection.comboBox.currentIndex()
                ],
                [v for (v, _) in self.allMqttData]
            )
        
        newValuesUsed = self.converter.convertUnits(
                self.specs.title,
                self.dataDetails.chosenUnit,
                self.specs.units[
                    self.dataDetails.unitSelection.comboBox.currentIndex()
                ],
                [v for (v, _) in self.usedMqttData]
            )

        self.usedMqttData = list(zip(
            newValuesUsed,
            [t for _, t in self.usedMqttData]
        ))

        self.allMqttData = list(zip(
            newValuesAll,
            [t for _, t in self.allMqttData]
        ))

        self.dataDetails.updateDetails([v for v, _ in self.usedMqttData])
        self.dataGraph.drawGraph(self.usedMqttData)

    def onPeriodChanged(self, newPeriod):
        now = datetime.now()
        offset = now

        if newPeriod == "7 days":
            offset = now - timedelta(days = 7)
        else:
            hs = int(newPeriod[: newPeriod.index("h")])
            offset = now - timedelta(hours = hs)

        self.usedMqttData = [(v, t) for v, t in self.allMqttData if t >= offset]
        self.dataDetails.updateDetails([v for v, _ in self.usedMqttData], newPeriod)
        self.dataGraph.drawGraph(self.usedMqttData)

    def onColorChanged(self):
        newColor = "" # TO DO

        if newColor == "red":
            newColor = "#fc0303"
        elif newColor == "black":
            newColor = "#000000"
        elif newColor == "white":
            newColor = "#f0f0f0"

        self.dataGraph.changePenColor(newColor)

    def onBackgroundChanged(self):
        newColor = "" # TO DO

        if newColor == "gray":
            newColor = "#7a7a7a"
        elif newColor == "black":
            newColor = "#000000"
        elif newColor == "white":
            newColor = "#f0f0f0"

        self.dataGraph.changeGraphBackground(newColor)

    def saveDataInJson(self):
        jsonData = {}
        jsonData[self.specs.title] = {}

        for value, time in self.usedMqttData:
            jsonData[self.specs.title][str(time)] = value

        jsonData = json.dumps(jsonData, indent = 4)

        response = QFileDialog.getSaveFileName(
            parent = self,
            caption = "Select location to save",
            filter = "JSON Files (*.json);;All Files (*)"
        )

        fileName = response[0]

        if fileName:
            if not fileName.lower().endswith(".json"):
                fileName += ".json"

            file = open(fileName, "w")
            file.write(jsonData)
            file.close()

    def saveDataInCsv(self):
        csvData = []
        csvData.append(("Date", f"{self.specs.title} value"))

        for value, time in self.usedMqttData:
            csvData.append((time, value))

        response = QFileDialog.getSaveFileName(
            parent = self,
            caption = "Select location to save",
            filter = "CSV Files (*.csv);;All Files (*)"
        )

        fileName = response[0]

        if fileName:
            if not fileName.lower().endswith(".csv"):
                fileName += ".csv"

            file = open(fileName, "w+")
            for time, value in csvData:
                file.write(f"{time},{value}\n")
            file.close()

    def saveDataInPng(self):
        response = QFileDialog.getSaveFileName(
            parent = self,
            caption = "Select location to save",
            filter = "PNG Files (*.png);;All Files (*)"
        )

        fileName = response[0]

        if fileName:
            if not fileName.lower().endswith(".png"):
                fileName += ".png"
            exporter = pyqtgraph.exporters.ImageExporter(
                self.dataGraph.plot_widget.plotItem
            )
            exporter.export(fileName)
            