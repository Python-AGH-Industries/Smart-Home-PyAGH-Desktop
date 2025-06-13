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

        self.panel_layout = QHBoxLayout(self)
        self.mqtt_sub_panel_layout = QVBoxLayout()

        self.mqtt_sub_panel_bar = MqttSubPanelBar()
        self.mqtt_data_widget = MqttSubPanel()
        self.public_data_widget = PublicSubPanel()

        self.mqtt_sub_panel_bar.userChangedPeriod.connect(self.updatePeriods)
        self.mqtt_sub_panel_bar.userChangedColor.connect(self.updateColor)
        self.mqtt_sub_panel_bar.userChangedBackground.connect(self.updateBackground)
        self.mqtt_sub_panel_bar.report_button.clicked.connect(self.generateReportLogic)

        self.updatePeriods()
        self.updateBackground()
        self.updateColor()

        self.mqtt_sub_panel_layout.addWidget(self.mqtt_sub_panel_bar)
        self.mqtt_sub_panel_layout.addWidget(self.mqtt_data_widget) 

        self.panel_layout.addLayout(self.mqtt_sub_panel_layout, stretch = 2)
        self.panel_layout.addWidget(self.public_data_widget, stretch = 1)

        self.panel_layout.setContentsMargins(0, 0, 0, 0)
        self.panel_layout.setSpacing(0)

    def updatePeriods(self):
        current_period = self.mqtt_sub_panel_bar.periods[
            self.mqtt_sub_panel_bar.period_selection.combo_box.currentIndex()
        ]

        self.mqtt_data_widget.temperature_row.rowContent.onPeriodChanged(
            current_period
        )
        self.mqtt_data_widget.humidity_row.rowContent.onPeriodChanged(
            current_period
        )
        self.mqtt_data_widget.pressure_row.rowContent.onPeriodChanged(
            current_period
        )
        self.mqtt_data_widget.light_row.rowContent.onPeriodChanged(
            current_period
        )

    def updateColor(self):
        current_color = self.mqtt_sub_panel_bar.colors[
            self.mqtt_sub_panel_bar.color_selection.combo_box.currentIndex()
        ]

        self.mqtt_data_widget.temperature_row.rowContent.updateColor(
            current_color
        )
        self.mqtt_data_widget.humidity_row.rowContent.updateColor(
            current_color
        )
        self.mqtt_data_widget.pressure_row.rowContent.updateColor(
            current_color
        )
        self.mqtt_data_widget.light_row.rowContent.updateColor(
            current_color
        )

    def updateBackground(self):
        current_color = self.mqtt_sub_panel_bar.backgrounds[
            self.mqtt_sub_panel_bar.background_selection.combo_box.currentIndex()
        ]

        self.mqtt_data_widget.temperature_row.rowContent.updateBackground(
            current_color
        )
        self.mqtt_data_widget.humidity_row.rowContent.updateBackground(
            current_color
        )
        self.mqtt_data_widget.pressure_row.rowContent.updateBackground(
            current_color
        )
        self.mqtt_data_widget.light_row.rowContent.updateBackground(
            current_color
        )

    def generateReportLogic(self):
        dialog = GenerateReportDialog(
            (
                self.mqtt_data_widget.temp_specs,
                self.mqtt_data_widget.humidity_specs,
                self.mqtt_data_widget.pressure_specs,
                self.mqtt_data_widget.light_specs
            ),
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