from PyQt6.QtWidgets import QPushButton, QWidget, \
    QVBoxLayout, QHBoxLayout, QLabel, \
    QSizePolicy, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal,QFile
from src.ui.widgets.textInput import TextInput
from src.model.loginController import LoginController

class Login(QWidget):
    loginSuccessful = pyqtSignal()
    register = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.loginWidgetLayout = QVBoxLayout(self)

        self.loginWelcomeLabel = QLabel("Welcome to you Smart Home Panel", self)
        self.loginWelcomeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.loginButtonLayout = QHBoxLayout()

        loginButton = QPushButton("Login", self)
        loginButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        loginButton.clicked.connect(self.loginHandler)

        registerButton = QPushButton("Register", self)
        registerButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
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

        loginController = LoginController()

        if loginController.login(self.usernameField.getText(),self.passwordField.getText()):
            print("logowanie pomyślne")
            self.loginSuccessful.emit()

        else:
            QMessageBox.information(self, "Błąd logowania", "Zły login lub hasło")

            print("Zły login lub hasło")
    def registerHandler(self):
        self.register.emit()

        pass