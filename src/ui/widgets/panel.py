from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QStyleOption, QStyle, QDialog
from PyQt6.QtCore import Qt
from src.ui.widgets.mqttSubPanel import MqttSubPanel
from src.ui.widgets.publicSubPanel import PublicSubPanel
from src.ui.widgets.mqttSubPanelBar import MqttSubPanelBar
from src.ui.windows.generateReportDialog import GenerateReportDialog
from PyQt6.QtGui import QPainter

class Panel(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.panelLayout = QHBoxLayout(self)
        self.mqttSubPanelLayout = QVBoxLayout()

        self.mqttSubPanelBar = MqttSubPanelBar()
        self.mqttDataWidget = MqttSubPanel()
        self.publicDataWidget = PublicSubPanel()

        self.mqttSubPanelBar.userChangedPeriod.connect(self.updatePeriods)
        self.mqttSubPanelBar.userChangedColor.connect(self.updateColor)
        self.mqttSubPanelBar.userChangedBackground.connect(self.updateBackground)
        self.mqttSubPanelBar.reportButton.clicked.connect(self.generateReportLogic)

        self.updatePeriods()
        self.updateBackground()
        self.updateColor()

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

    def updateColor(self):
        currentColor = self.mqttSubPanelBar.colors[
            self.mqttSubPanelBar.colorSelection.comboBox.currentIndex()
        ]

        self.mqttDataWidget.temperatureRow.rowContent.updateColor(
            currentColor
        )
        self.mqttDataWidget.humidityRow.rowContent.updateColor(
            currentColor
        )
        self.mqttDataWidget.pressureRow.rowContent.updateColor(
            currentColor
        )
        self.mqttDataWidget.lightRow.rowContent.updateColor(
            currentColor
        )

    def updateBackground(self):
        currentColor = self.mqttSubPanelBar.backgrounds[
            self.mqttSubPanelBar.backgroundSelection.comboBox.currentIndex()
        ]

        self.mqttDataWidget.temperatureRow.rowContent.updateBackground(
            currentColor
        )
        self.mqttDataWidget.humidityRow.rowContent.updateBackground(
            currentColor
        )
        self.mqttDataWidget.pressureRow.rowContent.updateBackground(
            currentColor
        )
        self.mqttDataWidget.lightRow.rowContent.updateBackground(
            currentColor
        )

    def generateReportLogic(self):
        dialog = GenerateReportDialog(
            (
                self.mqttDataWidget.tempSpecs,
                self.mqttDataWidget.humiditySpecs,
                self.mqttDataWidget.pressureSpecs,
                self.mqttDataWidget.lightSpecs
            ),
            self.mqttSubPanelBar.periods,
            self
        )

        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)