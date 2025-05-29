from PyQt6.QtWidgets import QPushButton, QWidget, \
    QVBoxLayout, QHBoxLayout, QLabel, QMessageBox, \
    QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal

from src.ui.widgets.labelComboBox import LabelComboBox
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
        loginButton.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        loginButton.clicked.connect(self.registerUser)

        self.loginButtonLayout.addStretch(1)
        self.loginButtonLayout.addWidget(loginButton, stretch = 2)
        self.loginButtonLayout.addStretch(1)
        self.loginButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.loginButtonLayout.setSpacing(0)

        self.loginWidgetLayout.addWidget(self.loginWelcomeLabel, stretch = 1)

        self.usernameField = TextInput("Username")
        self.usernameField.append(self.loginWidgetLayout)

        self.email = TextInput("Your email")
        self.email.append(self.loginWidgetLayout)

        self.passwordField = TextInput("Password")
        self.passwordField.append(self.loginWidgetLayout)

        self.repeatPasswordField = TextInput("Repeat password")
        self.repeatPasswordField.append(self.loginWidgetLayout)

        self.userPlanComboBox = LabelComboBox(
            "Choose your plan",
            ["FREE", "STANDARD", "PREMIUM"]
        )
        self.loginWidgetLayout.addWidget(self.userPlanComboBox)

        self.loginWidgetLayout.addLayout(self.loginButtonLayout, stretch = 1)
        iconPath = "src/resources/icons/"

        homeButton = IconButton(iconPath + "home.png", self)
        homeButton.clicked.connect(self.returnToLogin)
        self.loginWidgetLayout.addWidget(homeButton)

        self.setLayout(self.loginWidgetLayout)

    def registerUser(self):
        if self.passwordField.getText() != self.repeatPasswordField.getText():
            QMessageBox.warning(
                self,
                "Passwords don't match",
                "Your password and repeated password do not match"
            )
            return

        loginController = LoginController()
        loginController.register(
            self.usernameField.getText(),
            self.email.getText(),
            self.passwordField.getText(),
            self.userPlanComboBox.comboBox.currentIndex() + 1
        )
        self.returnToLogin()

    def returnToLogin(self):
        self.goBack.emit()
