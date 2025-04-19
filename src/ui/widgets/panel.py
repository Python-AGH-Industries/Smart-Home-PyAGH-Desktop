from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from src.ui.widgets.mqttSubPanel import MqttSubPanel
from src.ui.widgets.publicSubPanel import PublicSubPanel
from src.ui.widgets.mqttSubPanelBar import MqttSubPanelBar

class Panel(QWidget):
    def __init__(self):
        super().__init__()

        self.panelLayout = QHBoxLayout(self)
        self.mqttSubPanelLayout = QVBoxLayout()

        self.mqttSubPanelBar = MqttSubPanelBar()
        self.mqttDataWidget = MqttSubPanel()
        self.publicDataWidget = PublicSubPanel()

        self.mqttSubPanelBar.userChangedPeriod.connect(self.updatePeriods)

        self.updatePeriods()

        self.mqttSubPanelLayout.addWidget(self.mqttSubPanelBar)
        self.mqttSubPanelLayout.addWidget(self.mqttDataWidget) 

        self.panelLayout.addLayout(self.mqttSubPanelLayout, stretch = 2)
        self.panelLayout.addWidget(self.publicDataWidget, stretch = 1)

        self.panelLayout.setContentsMargins(0, 0, 0, 0)
        self.panelLayout.setSpacing(0)

    def updatePeriods(self):
        currentPeriod = self.mqttSubPanelBar.periods[
            self.mqttSubPanelBar.periodSelection.comboBox.currentIndex()
        ]

        self.mqttDataWidget.temperatureRow.rowContent.onPeriodChanged(
            currentPeriod
        )
        self.mqttDataWidget.humidityRow.rowContent.onPeriodChanged(
            currentPeriod
        )
        self.mqttDataWidget.pressureRow.rowContent.onPeriodChanged(
            currentPeriod
        )
        self.mqttDataWidget.lightRow.rowContent.onPeriodChanged(
            currentPeriod
        )