from PyQt6.QtWidgets import QPushButton, QWidget, \
    QVBoxLayout, QLabel, QSizePolicy, QMessageBox, \
    QStyle, QStyleOption
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPainter

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

        self.loginWelcomeLabel = QLabel("Welcome to your Smart Home Panel!", self)
        self.loginWelcomeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

        self.loginWidgetLayout.addWidget(self.loginWelcomeLabel, stretch = 1)
        self.usernameField = TextInput("Username")
        self.usernameField.append(self.loginWidgetLayout)
        self.passwordField = TextInput("Password")
        self.passwordField.append(self.loginWidgetLayout)

        self.loginWidgetLayout.addWidget(loginButton)
        self.loginWidgetLayout.addWidget(registerButton)
        self.loginWidgetLayout.addStretch(1)

        self.loginWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.loginWidgetLayout.setSpacing(0)
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
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)
