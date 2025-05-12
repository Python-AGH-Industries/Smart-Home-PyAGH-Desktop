from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QCheckBox,
                             QPushButton, QHBoxLayout)
from src.ui.widgets.labelComboBox import LabelComboBox

class GenerateReportDialog(QDialog):
    def __init__(self, data, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Your report")
        self.setFixedSize(400, 600)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)

        self.label = QLabel("Report generation")

        self.publicDataFlag = QCheckBox("Include public data", self)
        self.temperatureUnitBox = LabelComboBox(
            "Choose temperature unit",
            data[0].units,
            self
        )
        self.humidityUnitBox = LabelComboBox(
            "Choose humidity unit",
            data[1].units,
            self
        )
        self.pressureUnitBox = LabelComboBox(
            "Choose pressure unit",
            data[2].units,
            self
        )
        self.lightUnitBox = LabelComboBox(
            "Choose light unit",
            data[3].units,
            self
        )

        buttonLayout = QHBoxLayout()
        self.cancelButton = QPushButton("Cancel")
        self.okButton = QPushButton("Generate")
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.cancelButton)
        buttonLayout.addWidget(self.okButton)

        layout.addWidget(self.label)
        layout.addWidget(self.publicDataFlag)
        layout.addWidget(self.temperatureUnitBox)
        layout.addWidget(self.humidityUnitBox)
        layout.addWidget(self.pressureUnitBox)
        layout.addWidget(self.lightUnitBox)
        layout.addStretch(1)
        layout.addLayout(buttonLayout)

        self.cancelButton.clicked.connect(self.reject)
        self.okButton.clicked.connect(self.accept)
