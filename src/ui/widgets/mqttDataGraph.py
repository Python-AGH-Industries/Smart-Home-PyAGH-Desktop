from PyQt6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg

from src.model.unitConverter import UnitConverter


class MqttDataGraph(QWidget):
    def __init__(self, rowSpecs, data):
        super().__init__()
        self.rowSpecs = rowSpecs
        self.converter = UnitConverter()
        self.layout = QVBoxLayout(self)
        self.plot_widget = pg.PlotWidget()  # Store as instance variable
        self.leftLabel = rowSpecs.title
        self.initial_data = data

        # Initial setup
        self.setUpPlot(rowSpecs.units[0])
        self.layout.addWidget(self.plot_widget)

    def setUpPlot(self,unit):
        self.plot_widget.clear()
        time = [t for (_, t) in self.initial_data]
        data = [d for (d, _) in self.initial_data]
        data = self.converter.convertUnits(self.rowSpecs.title,self.rowSpecs.units[0],unit,data)
        self.plot_line = self.plot_widget.plot(time, data, pen=pg.mkPen(color=(255, 0, 0)))

        self.plot_widget.setLabel("left", self.leftLabel)
        self.plot_widget.setLabel("bottom", "Time (h)")
        self.plot_widget.setTitle(f"{self.leftLabel} vs Time", color="w", size="10pt")

    def updateGraph(self, new_data,unit):
        self.plot_widget.removeItem(self.plot_line)

        time = [t for (_, t) in new_data]
        data = [d for (d, _) in new_data]
        print("==")

        print(data)
        print(self.rowSpecs.units[0])
        print(unit)

        data = self.converter.convertUnits(self.rowSpecs.title,self.rowSpecs.units[0],unit,data)
        print(data)
        print("==")

        self.plot_line = self.plot_widget.plot(time, data, pen=pg.mkPen(color=(255, 0, 0)))

        self.plot_widget.autoRange()

