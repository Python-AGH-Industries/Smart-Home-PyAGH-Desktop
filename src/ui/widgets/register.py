from PyQt6.QtWidgets import QPushButton, QWidget, \
    QVBoxLayout, QHBoxLayout, QLabel, \
    QSizePolicy, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal,QFile

from src.ui.widgets.iconButton import IconButton
from src.ui.widgets.textInput import TextInput
from src.model.loginController import LoginController

class Register(QWidget):
    goBack = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.loginWidgetLayout = QVBoxLayout(self)

        self.loginWelcomeLabel = QLabel("Registration panel", self)
        self.loginWelcomeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.loginButtonLayout = QHBoxLayout()

        loginButton = QPushButton("Register", self)
        loginButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        loginButton.clicked.connect(self.registerUser)


        self.loginButtonLayout.addStretch(1)
        self.loginButtonLayout.addWidget(loginButton, stretch = 2)

        self.loginButtonLayout.addStretch(1)

        self.loginButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.loginButtonLayout.setSpacing(0)

        self.loginWidgetLayout.addWidget(self.loginWelcomeLabel, stretch = 1)
        self.usernameField = TextInput("Username")
        self.usernameField.append(self.loginWidgetLayout)
        self.email = TextInput("email")
        self.email.append(self.loginWidgetLayout)
        self.passwordField = TextInput("Password")
        self.passwordField.append(self.loginWidgetLayout)

        self.loginWidgetLayout.addLayout(self.loginButtonLayout, stretch = 1)
        iconPath = "src/resources/icons/"

        homeButton = IconButton(iconPath + "home.png", self)
        homeButton.clicked.connect(self.returnToLogin)
        self.loginWidgetLayout.addWidget(homeButton)

        self.setLayout(self.loginWidgetLayout)

    def registerUser(self):
        print("register")
        loginController = LoginController()
    def returnToLogin(self):
        self.goBack.emit()
