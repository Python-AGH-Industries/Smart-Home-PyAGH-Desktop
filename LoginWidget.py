from PyQt6.QtWidgets import QPushButton, QWidget, \
                            QVBoxLayout, QHBoxLayout, QLabel, \
                            QSizePolicy
from PyQt6.QtCore import Qt

class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()

        loginWidgetLayout = QVBoxLayout(self)

        loginWelcomeLabel = QLabel("Welcome to you Smart Home Panel", self)
        loginWelcomeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        loginButtonLayout = QHBoxLayout()
        loginButton = QPushButton("Login", self)
        loginButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        loginButtonLayout.addStretch(1)
        loginButtonLayout.addWidget(loginButton, stretch = 5)
        loginButtonLayout.addStretch(1)

        loginButtonLayout.setContentsMargins(0, 0, 0, 0)
        loginButtonLayout.setSpacing(0)

        loginWidgetLayout.addWidget(loginWelcomeLabel, stretch = 2)
        loginWidgetLayout.addLayout(loginButtonLayout, stretch = 1)

        loginWidgetLayout.setContentsMargins(0, 0, 0, 0)
        loginWidgetLayout.setSpacing(0)

        self.setLayout(loginWidgetLayout)

        
