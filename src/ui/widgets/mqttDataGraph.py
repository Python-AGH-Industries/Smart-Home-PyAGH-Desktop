from PyQt6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg
from random import randint

class MqttDataGraph(QWidget):
    def __init__(self, leftLabel):
        super().__init__()
        layout = QVBoxLayout(self)
        plot_graph = pg.PlotWidget()

        time = [i for i in range(20)]
        temp = [randint(i, i + 10) for i in range(20)]
        pen = pg.mkPen(color=(255,0,0))

        plot_graph.plot(time, temp, pen = pen)
        plot_graph.setLabel("left", leftLabel)
        plot_graph.setLabel("bottom", "Time (min)")
        plot_graph.setTitle(leftLabel + " vs Time", color="w", size="10pt")

        layout.addWidget(plot_graph)