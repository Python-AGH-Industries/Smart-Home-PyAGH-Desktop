from PyQt6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg

class MqttDataGraph(QWidget):
    def __init__(self, leftLabel):
        super().__init__()
        self.plot_widget = pg.PlotWidget()

        self.plot_widget.setLabel('left', leftLabel)
        date_axis = pg.DateAxisItem(orientation='bottom')
        self.plot_widget.setAxisItems({'bottom': date_axis})
        self.plot_widget.setTitle(f"{leftLabel} vs Time")
        self.plot_widget.setLabel('bottom', 'Time')

        self.timestamps = []
        self.values = []

        layout = QVBoxLayout(self)
        layout.addWidget(self.plot_widget)

    def drawGraph(self, values, timestamps):
        self.values = values
        self.timestamps = timestamps
        self.plot_widget.clear()
        self.plot_widget.plot(self.timestamps, self.values, pen = 'r')
        self.plot_widget.enableAutoRange()

    def updateGraphValues(self, values):
        self.values = values
        self.plot_widget.clear()
        self.plot_widget.plot(self.timestamps, values, pen = 'r')

    def updateGraphTimestamps(self, timestamps):
        self.timestamps = timestamps
        self.plot_widget.clear()
        self.plot_widget.plot(self.timestamps, self.values, pen = 'r')