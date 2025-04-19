from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout
from src.ui.widgets.labelComboBox import LabelComboBox
from PyQt6.QtCore import pyqtSignal

class MqttSubPanelBar(QWidget):
    userChangedPeriod = pyqtSignal()
    userChangedColor = pyqtSignal()
    userChangedBackground = pyqtSignal()

    def __init__(self):
        super().__init__()
        room1 = QPushButton("Kitchen")
        room2 = QPushButton("Living Room")
        add_button = QPushButton("+")

        self.periods = ["4h", "8h", "12h", "24h", "48h", "7 days"]
        self.colors = ["red", "black", "white"]
        self.backgrounds = ["white", "gray"] 

        self.periodSelection = LabelComboBox(
            f"Data period ",
            self.periods,
            self
        )
        self.colorSelection = LabelComboBox(
            f"Color ",
            self.colors,
            self
        )
        self.backgroundSelection = LabelComboBox(
            f"Background ",
            self.backgrounds,
            self
        )

        self.periodSelection.comboBox.currentTextChanged.connect(
            lambda: self.userChangedPeriod.emit()
        )

        self.colorSelection.comboBox.currentIndexChanged.connect(
            lambda: self.userChangedColor.emit()
        )

        self.backgroundSelection.comboBox.currentTextChanged.connect(
            lambda: self.userChangedBackground.emit()
        )

        self.setFixedHeight(30)
        layout = QHBoxLayout(self)
        layout.addWidget(room1)
        layout.addWidget(room2)
        layout.addWidget(add_button)
        layout.addStretch(1)
        layout.addWidget(self.periodSelection)
        layout.addWidget(self.colorSelection)
        layout.addWidget(self.backgroundSelection)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        