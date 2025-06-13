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

    current_user = None

    def __init__(self):
        super().__init__()
        self.login_widget_layout = QVBoxLayout(self)

        self.login_welcom_label = QLabel("Welcome to your Smart Home Panel!", self)
        self.login_welcom_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        login_button = QPushButton("Login", self)
        login_button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        login_button.clicked.connect(self.loginHandler)

        register_button = QPushButton("Register", self)
        register_button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        register_button.clicked.connect(self.registerHandler)

        self.login_widget_layout.addWidget(self.login_welcom_label, stretch = 1)
        self.username_field = TextInput("Username")
        self.username_field.append(self.login_widget_layout)
        self.password_field = TextInput("Password")
        self.password_field.append(self.login_widget_layout)

        self.login_widget_layout.addWidget(login_button)
        self.login_widget_layout.addWidget(register_button)
        self.login_widget_layout.addStretch(1)

        self.login_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.login_widget_layout.setSpacing(0)
        self.setLayout(self.login_widget_layout)

    def loginHandler(self):
        global current_user
        login_controller = LoginController()

        username = self.username_field.getText()
        password = self.password_field.getText()

        if login_controller.login(
            username,
            password
        ):
            Login.current_user = User(username)
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
        return cls.current_user
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)
