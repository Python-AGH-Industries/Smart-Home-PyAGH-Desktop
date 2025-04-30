from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout, 
                             QLineEdit, QPushButton, QStyle, QStyleOption,
                             QHBoxLayout, QMessageBox)
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import pyqtSignal
from src.ui.widgets.login import Login

import requests

class SettingsPanel(QWidget):
    showSettingsSignal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        self.user = Login.getCurrentUser()
        self.session = requests.session()
        
        self.usernameLabel = QLabel("Hello, " + str(self.user.username))
        self.usernameLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(self.usernameLabel)
        
        formLayout = QGridLayout()
        formLayout.setVerticalSpacing(10)
        formLayout.setHorizontalSpacing(15)
        
        currentPassLabel = QLabel("Current Password:")
        self.currentPassInput = QLineEdit()
        formLayout.addWidget(currentPassLabel)
        formLayout.addWidget(self.currentPassInput)
        
        newPassLabel = QLabel("New Password:")
        self.newPassInput = QLineEdit()
        formLayout.addWidget(newPassLabel)
        formLayout.addWidget(self.newPassInput)
        
        repeatPassLabel = QLabel("Repeat New Password:")
        self.repeatPassInput = QLineEdit()
        formLayout.addWidget(repeatPassLabel)
        formLayout.addWidget(self.repeatPassInput)
        
        layout.addLayout(formLayout)
        
        buttonLayout = QHBoxLayout()
        self.saveButton = QPushButton("Save Changes")
        self.cancelButton = QPushButton("Cancel")
        
        self.saveButton.clicked.connect(self.saveChanges)
        self.cancelButton.clicked.connect(self.clearForm)
        
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.cancelButton)
        buttonLayout.addWidget(self.saveButton)
        
        layout.addLayout(buttonLayout)
        layout.addStretch(1)
        
    def saveChanges(self):
        current = self.currentPassInput.text()
        new = self.newPassInput.text()
        repeated = self.repeatPassInput.text()
        
        if new != repeated:
            QMessageBox.warning(
                self,
                "Password mismatch",
                "New password and repeated password has to be the same!"
            )
            return
        
        self.session.post(
            'http://127.0.0.1:5000/changePassword',
            json={
                "username": self.user.username,
                "newPassword": new,
                "oldPassword": current
            }
        )

        self.clearForm()
    
    def clearForm(self):
        self.currentPassInput.clear()
        self.newPassInput.clear()
        self.repeatPassInput.clear()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)
        super().paintEvent(event)