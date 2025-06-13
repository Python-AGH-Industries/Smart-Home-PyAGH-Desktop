from PyQt6.QtWidgets import QWidget, QHBoxLayout
from src.ui.widgets.stackedLabels import StackedLabels

class MqttLabelGroup(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout(self)

        self.avg_stack = StackedLabels("AVG", self)
        self.min_stack = StackedLabels("MIN", self)
        self.max_stack = StackedLabels("MAX", self)

        main_layout.addStretch(1)
        main_layout.addWidget(self.avg_stack)
        main_layout.addStretch(1)
        main_layout.addWidget(self.min_stack)
        main_layout.addStretch(1)
        main_layout.addWidget(self.max_stack)
        main_layout.addStretch(1)
        
    def setText(self, avg_text, min_text, max_text):
        self.avg_stack.lower_label.setText(avg_text)
        self.min_stack.lower_label.setText(min_text)
        self.max_stack.lower_label.setText(max_text)