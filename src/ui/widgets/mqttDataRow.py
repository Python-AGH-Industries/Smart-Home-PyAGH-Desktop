from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from src.ui.widgets.mqttDataGraph import MqttDataGraph

class MqttDataRow(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setStyleSheet("background-color: green; border: 1px solid black;")
        
        wrapperLayout = QVBoxLayout(self)
        titleLabel = QLabel(title)

        layout = QHBoxLayout()
        
        graph1 = MqttDataGraph()
        graph2 = MqttDataGraph()
        graph3 = MqttDataGraph()

        layout.addWidget(graph1)
        layout.addWidget(graph2)
        layout.addWidget(graph3)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        wrapperLayout.addWidget(titleLabel, stretch = 1)
        wrapperLayout.addLayout(layout, stretch = 7)

        wrapperLayout.setContentsMargins(0, 0, 0, 0)
        wrapperLayout.setSpacing(0)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)