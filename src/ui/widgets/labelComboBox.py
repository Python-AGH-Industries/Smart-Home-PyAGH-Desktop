from PyQt6.QtWidgets import QWidget, QLabel, QComboBox, QHBoxLayout

class LabelComboBox(QWidget):
    def __init__(self, text, options, parent = None):
        super().__init__()
        comboBoxLayout = QHBoxLayout(self)
        self.setParent(parent)

        description = QLabel(text, self)
        description.setWordWrap(True)

        self.comboBox = QComboBox(self)
        self.comboBox.addItems(options)

        comboBoxLayout.addWidget(description)
        comboBoxLayout.addWidget(self.comboBox)

        comboBoxLayout.setContentsMargins(0, 0, 0, 0)
        comboBoxLayout.setSpacing(0)