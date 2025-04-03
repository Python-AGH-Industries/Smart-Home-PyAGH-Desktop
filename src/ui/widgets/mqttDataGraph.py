from PyQt6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg
from datetime import datetime

class MqttDataGraph(QWidget):
    def __init__(self, leftLabel, data):
        super().__init__()
        self.plot_widget = pg.PlotWidget()
        layout = QVBoxLayout(self)
        layout.addWidget(self.plot_widget)
        
        timestamps = [t.timestamp() for (_, t) in data]
        values = [v for (v, _) in data]

        date_axis = pg.DateAxisItem(orientation='bottom')
        self.plot_widget.setAxisItems({'bottom': date_axis})

        self.plot_widget.plot(timestamps, values, pen='r')

        self.plot_widget.setLabel('left', leftLabel)
        self.plot_widget.setLabel('bottom', 'Time')
        self.plot_widget.setTitle(f"{leftLabel} vs Time")