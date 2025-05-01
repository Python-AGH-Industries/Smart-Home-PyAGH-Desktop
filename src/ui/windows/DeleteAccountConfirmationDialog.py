from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, 
                             QPushButton, QHBoxLayout)

class DeleteAccountConfirmationDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Confirm Account Deletion")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        self.label = QLabel("Enter your password:")

        self.passwordInput = QLineEdit()
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        buttonLayout = QHBoxLayout()
        self.cancelButton = QPushButton("Cancel")
        self.okButton = QPushButton("OK")
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.cancelButton)
        buttonLayout.addWidget(self.okButton)

        layout.addWidget(self.label)
        layout.addWidget(self.passwordInput)
        layout.addStretch(1)
        layout.addLayout(buttonLayout)

        self.cancelButton.clicked.connect(self.reject)
        self.okButton.clicked.connect(self.accept)

    def getPassword(self):
        return self.passwordInput.text()
