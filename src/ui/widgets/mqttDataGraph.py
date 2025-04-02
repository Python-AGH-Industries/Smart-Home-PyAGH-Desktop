from PyQt6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg
from random import randint

class MqttDataGraph(QWidget):
    def __init__(self, leftLabel, data):
        super().__init__()
        layout = QVBoxLayout(self)
        plot_graph = pg.PlotWidget()

        time = [t for (_, t) in data]
        data = [d for (d, _) in data]
        pen = pg.mkPen(color=(255,0,0))

        plot_graph.plot(time, data, pen = pen)
        plot_graph.setLabel("left", leftLabel)
        plot_graph.setLabel("bottom", "Time (min)")
        plot_graph.setTitle(leftLabel + " vs Time", color="w", size="10pt")

        layout.addWidget(plot_graph)