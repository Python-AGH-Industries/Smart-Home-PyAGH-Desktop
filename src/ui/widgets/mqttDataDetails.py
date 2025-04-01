from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from src.ui.widgets.labelComboBox import LabelComboBox
from random import randint

class MqttDataDetails(QWidget):
    def __init__(self, title, units):
        super().__init__()
        layout = QVBoxLayout(self)
        periods = ["4h", "8h", "12h", "24h", "48h", "7 days"]
        self.periodSelection = LabelComboBox("Showing " + title.lower() +
                                        " from the last", periods, self)
        self.unitSelection = LabelComboBox(title + " unit ", units, self)

        self.chosenPeriod = periods[self.periodSelection.comboBox.currentIndex()]
        self.chosenUnit = units[self.unitSelection.comboBox.currentIndex()]

        self.meanLabel = QLabel("Last " + self.chosenPeriod + " mean: " + 
                           str(randint(100, 300) / 10) + " " + self.chosenUnit)
        self.minLabel = QLabel("Last " + self.chosenPeriod + " min: " +
                               str(randint(0, 150) / 10) + " " + self.chosenUnit)
        self.maxLabel = QLabel("Last " + self.chosenPeriod + " max: " +
                               str(randint(300, 400) / 10) + " " + self.chosenUnit)

        layout.addWidget(self.periodSelection)
        layout.addWidget(self.unitSelection)
        layout.addWidget(self.meanLabel)
        layout.addWidget(self.minLabel)
        layout.addWidget(self.maxLabel)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)