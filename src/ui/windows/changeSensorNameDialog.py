from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, 
                             QPushButton, QHBoxLayout)

class ChangeSensorNameDialog(QDialog):
    def __init__(self, sensors_data, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Change sensors' names")
        self.setFixedSize(600, 300 * (len(sensors_data) // 3))

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        self.row_data = []
        it = 1

        for sensor_name, _ in sensors_data:
            self.row_data.append((
                QLabel(str(it) + ". sensor"),
                QLineEdit(sensor_name)
            ))
            it += 1

        for label, edit in self.row_data:
            layout.addWidget(label)
            layout.addWidget(edit)

        button_layout = QHBoxLayout()
        self.cancel_button = QPushButton("Cancel")
        self.ok_button = QPushButton("OK")
        button_layout.addStretch()
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.ok_button)

        layout.addStretch(1)
        layout.addLayout(button_layout)

        self.cancel_button.clicked.connect(self.reject)
        self.ok_button.clicked.connect(self.accept)

    def getNewSensorData(self):
        result = []

        for _, edit in self.row_data:
            result.append(edit.text())

        return result