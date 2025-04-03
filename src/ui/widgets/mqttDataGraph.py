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
        self.plot_widget.enableAutoRange()

        self.timestamps = []
        self.values = []

        layout = QVBoxLayout(self)
        layout.addWidget(self.plot_widget)

    def drawGraph(self, data):
        self.values = [v for v, _ in data]
        self.timestamps = [t.timestamp() for _, t in data]
        self.plot_widget.clear()
        self.plot_widget.plot(self.timestamps, self.values, pen = 'r')
    