import numpy
from PyQt6.QtWidgets import QWidget, QHBoxLayout
from tornado.http1connection import parse_int

from src.model.unitConverter import UnitConverter
from src.ui.widgets.mqttDataGraph import MqttDataGraph
from src.ui.widgets.mqttDataDetails import MqttDataDetails

class MqttDataContent(QWidget):
    def __init__(self, rowSpecs, mqttData):
        super().__init__()

        dataContentLayout = QHBoxLayout(self)
        self.data = mqttData
        self.currentData = self.data
        self.rowSpecs = rowSpecs
        self.dataGraph = MqttDataGraph(rowSpecs, self.data)
        dataDetails = MqttDataDetails(rowSpecs, mqttData,self.changeTimeframe,self.changeUnit)

        dataContentLayout.addWidget(self.dataGraph, stretch = 5)
        dataContentLayout.addWidget(dataDetails, stretch = 4)
        dataContentLayout.setContentsMargins(0, 0, 0, 0)
        dataContentLayout.setSpacing(0)
        self.unit = self.rowSpecs.units[0]
        self.changeTimeframe("4h")

    def changeTimeframe(self,newTimeframe):
        self.timeFrame = newTimeframe
        print("NEWUNIT: "+self.unit)
        def helper(a):
            return a[0],a[1]/60


        if newTimeframe[-1]=='h':
            limit = parse_int(newTimeframe.split("h")[0])

            data = self.data[0:limit*60]
            print(data)

            data = list(map(helper,data))
            print(data)
            self.dataGraph.updateGraph(data,self.unit)
        else:
            limit = parse_int(newTimeframe.split(" ")[0])
            data = self.data[0:limit*60*24]
            data = list(map(helper,data))
            self.dataGraph.updateGraph(data,self.unit)


    def changeUnit(self,newUnit):
        print("changed")
        self.unit = newUnit
        self.changeTimeframe(self.timeFrame)