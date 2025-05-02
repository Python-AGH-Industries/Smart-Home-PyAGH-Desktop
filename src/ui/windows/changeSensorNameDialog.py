from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, 
                             QPushButton, QHBoxLayout)

class ChangeSensorNameDialog(QDialog):
    def __init__(self, sensorsData, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Change sensors' names")
        self.setFixedSize(600, 300 * (len(sensorsData) // 3))

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        self.rowData = []
        it = 1

        for sensorName, _ in sensorsData:
            self.rowData.append((
                QLabel(str(it) + ". sensor"),
                QLineEdit(sensorName)
            ))
            it += 1

        for label, edit in self.rowData:
            layout.addWidget(label)
            layout.addWidget(edit)

        buttonLayout = QHBoxLayout()
        self.cancelButton = QPushButton("Cancel")
        self.okButton = QPushButton("OK")
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.cancelButton)
        buttonLayout.addWidget(self.okButton)

        layout.addStretch(1)
        layout.addLayout(buttonLayout)

        self.cancelButton.clicked.connect(self.reject)
        self.okButton.clicked.connect(self.accept)

    def getNewSensorData(self):
        result = []

        for _, edit in self.rowData:
            result.append(edit.text())

        return result