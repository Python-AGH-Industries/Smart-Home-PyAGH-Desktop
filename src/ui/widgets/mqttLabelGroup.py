from PyQt6.QtWidgets import QWidget, QHBoxLayout
from src.ui.widgets.stackedLabels import StackedLabels

class MqttLabelGroup(QWidget):
    def __init__(self):
        super().__init__()
        mainLayout = QHBoxLayout(self)

        self.meanStack = StackedLabels("MEAN", self)
        self.minStack = StackedLabels("MIN", self)
        self.maxStack = StackedLabels("MAX", self)

        mainLayout.addStretch(1)
        mainLayout.addWidget(self.meanStack)
        mainLayout.addStretch(1)
        mainLayout.addWidget(self.minStack)
        mainLayout.addStretch(1)
        mainLayout.addWidget(self.maxStack)
        mainLayout.addStretch(1)
        
    def setText(self, meanText, minText, maxText):
        self.meanStack.lowerLabel.setText(meanText)
        self.minStack.lowerLabel.setText(minText)
        self.maxStack.lowerLabel.setText(maxText)