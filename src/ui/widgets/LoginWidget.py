from PyQt6.QtWidgets import QPushButton, QWidget, \
                            QVBoxLayout, QHBoxLayout, QLabel, \
                            QSizePolicy, QLineEdit
from PyQt6.QtCore import Qt, pyqtSignal

from src.model.LoginController import LoginController
from src.ui.widgets.TextInput import TextInput


class LoginWidget(QWidget):
    loginSuccessful = pyqtSignal()

    def __init__(self):
        super().__init__()


        self.loginWidgetLayout = QVBoxLayout(self)

        self.loginWelcomeLabel = QLabel("Welcome to you Smart Home Panel", self)
        self.loginWelcomeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)


            

        self.loginButtonLayout = QHBoxLayout()

        loginButton = QPushButton("Login", self)
        loginButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        loginButton.clicked.connect(self.loginHandler)

        self.loginButtonLayout.addStretch(1)
        self.loginButtonLayout.addWidget(loginButton, stretch = 5)
        self.loginButtonLayout.addStretch(1)

        self.loginButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.loginButtonLayout.setSpacing(0)

        self.loginWidgetLayout.addWidget(self.loginWelcomeLabel, stretch = 2)
        self.usernameField = TextInput("Username")
        self.usernameField.append(self.loginWidgetLayout)
        self.passwordField = TextInput("Password")
        self.passwordField.append(self.loginWidgetLayout)

        self.loginWidgetLayout.addLayout(self.loginButtonLayout, stretch = 1)
        self.loginWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.loginWidgetLayout.setSpacing(0)


        self.setLayout(self.loginWidgetLayout)







    def loginHandler(self):

        loginController = LoginController()

        if loginController.login(self.usernameField.getText(),self.passwordField.getText()):
            print("logowanie pomyślne")
            self.loginSuccessful.emit()

        else:
            print("Zły login lub hasło")
