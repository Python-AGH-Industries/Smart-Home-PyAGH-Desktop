from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout, 
                             QLineEdit, QPushButton, QStyle, QStyleOption,
                             QHBoxLayout, QMessageBox, QDialog)
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import pyqtSignal
from src.ui.widgets.login import Login
from src.ui.windows.deleteAccountConfirmationDialog import DeleteAccountConfirmationDialog
from src.ui.widgets.labelComboBox import LabelComboBox

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
        
        self.username_label = QLabel("Hello, " + str(self.user.username))
        layout.addWidget(self.username_label)
        
        form_layout = QGridLayout()
        form_layout.setVerticalSpacing(10)
        form_layout.setHorizontalSpacing(15)
        
        current_pass_label = QLabel("Current Password:")
        self.current_pass_input = QLineEdit()
        form_layout.addWidget(current_pass_label)
        form_layout.addWidget(self.current_pass_input)
        
        new_pass_label = QLabel("New Password:")
        self.new_pass_input = QLineEdit()
        form_layout.addWidget(new_pass_label)
        form_layout.addWidget(self.new_pass_input)
        
        repeat_pass_label = QLabel("Repeat New Password:")
        self.repeat_pass_input = QLineEdit()
        form_layout.addWidget(repeat_pass_label)
        form_layout.addWidget(self.repeat_pass_input)
        
        layout.addLayout(form_layout)
        
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save Changes")
        self.cancel_button = QPushButton("Cancel")

        self.save_button.clicked.connect(self.saveChanges)
        self.cancel_button.clicked.connect(self.clearForm)

        button_layout.addStretch()
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.save_button)

        layout.addLayout(button_layout)

        self.theme_combo_box = LabelComboBox(
            "Application theme ",
            ["dark", "light"],
            self,
            True
        )
        layout.addWidget(self.theme_combo_box)

        delete_layout = QHBoxLayout()
        delete_account_label = QLabel("Delete your account")
        delete_button = QPushButton("Delete")

        delete_layout.addWidget(delete_account_label)
        delete_layout.addWidget(delete_button)
        delete_layout.addStretch(1)

        delete_button.clicked.connect(self.accountDeletionConfirmation)

        layout.addLayout(delete_layout)
        layout.addStretch(1)
        
    def saveChanges(self):
        current = self.current_pass_input.text()
        new = self.new_pass_input.text()
        repeated = self.repeat_pass_input.text()
        
        if new != repeated:
            QMessageBox.warning(
                self,
                "Password mismatch",
                "New password and repeated password has to be the same!"
            )
            return
        
        if current == "" or new == "" or repeated == "":
            QMessageBox.warning(
                self,
                "Empty field",
                "One of the fields is empty"
            )
            return
        
        self.session.post(
            'http://127.0.0.1:5000/changePassword',
            json = {
                "username": self.user.username,
                "newPassword": new,
                "oldPassword": current
            }
        )

        self.clearForm()
    
    def clearForm(self):
        self.current_pass_input.clear()
        self.new_pass_input.clear()
        self.repeat_pass_input.clear()

    def accountDeletionConfirmation(self):
        dialog = DeleteAccountConfirmationDialog(self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        password = dialog.getPassword()
        if password == "":
            QMessageBox.warning(
                self,
                "Input Error",
                "Password cannot be empty."
            )
            return

        response = self.session.post(
            'http://127.0.0.1:5000/deleteAccount',
            json = {
                "username": self.user.username,
                "password": password
            }
        )

        if response.status_code == 200:
            QMessageBox.information(
                self,
                "Account Deleted",
                "Your account has been successfully deleted."
            )
        else:
            QMessageBox.warning(
                self,
                "Error",
                f"Failed to delete account: {response.json().get("error")}"
            )
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(
            QStyle.PrimitiveElement.PE_Widget,
            opt,
            painter,
            self
        )
        super().paintEvent(event)