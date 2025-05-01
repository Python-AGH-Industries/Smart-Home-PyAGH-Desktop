from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, 
                             QPushButton, QHBoxLayout)

class ChangeSensorNameDialog(QDialog):
    def __init__(self, sensorsData, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Change sensors' names")
        self.setFixedSize(400, 200)

        print(sensorsData)

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        self.label = QLabel("Test")

        buttonLayout = QHBoxLayout()
        self.cancelButton = QPushButton("Cancel")
        self.okButton = QPushButton("OK")
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.cancelButton)
        buttonLayout.addWidget(self.okButton)

        layout.addWidget(self.label)
        layout.addStretch(1)
        layout.addLayout(buttonLayout)

        self.cancelButton.clicked.connect(self.reject)
        self.okButton.clicked.connect(self.accept)
