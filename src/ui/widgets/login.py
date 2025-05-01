from PyQt6.QtWidgets import QPushButton, QWidget, \
    QVBoxLayout, QHBoxLayout, QLabel, \
    QSizePolicy, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal

from src.model.user import User
from src.model.loginController import LoginController
from src.ui.widgets.textInput import TextInput

class Login(QWidget):
    loginSuccessful = pyqtSignal()
    register = pyqtSignal()

    currentUser = None

    def __init__(self):
        super().__init__()
        self.loginWidgetLayout = QVBoxLayout(self)

        self.loginWelcomeLabel = QLabel("Welcome to you Smart Home Panel", self)
        self.loginWelcomeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.loginButtonLayout = QHBoxLayout()

        loginButton = QPushButton("Login", self)
        loginButton.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        loginButton.clicked.connect(self.loginHandler)

        registerButton = QPushButton("Register", self)
        registerButton.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        registerButton.clicked.connect(self.registerHandler)

        self.loginButtonLayout.addStretch(1)
        self.loginButtonLayout.addWidget(loginButton, stretch = 5)
        self.loginButtonLayout.addWidget(registerButton, stretch = 5)

        self.loginButtonLayout.addStretch(1)

        self.loginButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.loginButtonLayout.setSpacing(0)

        self.loginWidgetLayout.addWidget(self.loginWelcomeLabel, stretch = 1)
        self.usernameField = TextInput("Username")
        self.usernameField.append(self.loginWidgetLayout)
        self.passwordField = TextInput("Password")
        self.passwordField.append(self.loginWidgetLayout)

        self.loginWidgetLayout.addLayout(self.loginButtonLayout, stretch = 1)

        self.setLayout(self.loginWidgetLayout)

    def loginHandler(self):
        global currentUser
        loginController = LoginController()

        username = self.usernameField.getText()
        password = self.passwordField.getText()

        if loginController.login(
            username,
            password
        ):
            Login.currentUser = User(username)
            print("logowanie pomyślne")
            self.loginSuccessful.emit()
        else:
            QMessageBox.information(
                self,
                "Błąd logowania",
                "Zły login lub hasło"
            )

            print("Zły login lub hasło")
            
    def registerHandler(self):
        self.register.emit()
        pass

    @classmethod
    def getCurrentUser(cls):
        return cls.currentUser