from PyQt6.QtWidgets import QPushButton, QWidget, \
    QVBoxLayout, QHBoxLayout, QLabel, QMessageBox, \
    QSizePolicy, QStyle, QStyleOption
from PyQt6.QtCore import Qt, pyqtSignal

from PyQt6.QtGui import QPainter
from src.ui.widgets.labelComboBox import LabelComboBox
from src.ui.widgets.iconButton import IconButton
from src.ui.widgets.textInput import TextInput
from src.model.loginController import LoginController

class Register(QWidget):
    goBack = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.login_widget_layout = QVBoxLayout(self)

        self.login_welcome_label = QLabel("Registration panel", self)
        self.login_welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.login_button_layout = QHBoxLayout()

        login_button = QPushButton("Register", self)
        login_button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        login_button.clicked.connect(self.registerUser)

        self.login_button_layout.addStretch(1)
        self.login_button_layout.addWidget(login_button, stretch = 2)
        self.login_button_layout.addStretch(1)
        self.login_button_layout.setContentsMargins(0, 0, 0, 0)
        self.login_button_layout.setSpacing(0)

        self.login_widget_layout.addWidget(self.login_welcome_label, stretch = 1)

        self.username_field = TextInput("Username")
        self.username_field.append(self.login_widget_layout)

        self.email = TextInput("Your email")
        self.email.append(self.login_widget_layout)

        self.password_field = TextInput("Password")
        self.password_field.append(self.login_widget_layout)

        self.repeat_password_field = TextInput("Repeat password")
        self.repeat_password_field.append(self.login_widget_layout)

        self.user_plan_combo_box = LabelComboBox(
            "Choose your plan",
            ["FREE", "STANDARD", "PREMIUM"]
        )
        self.login_widget_layout.addWidget(self.user_plan_combo_box)

        self.login_widget_layout.addLayout(self.login_button_layout, stretch = 1)
        icon_path = "src/resources/icons/"

        home_button = IconButton(icon_path + "home.png", self)
        home_button.clicked.connect(self.returnToLogin)
        self.login_widget_layout.addWidget(home_button)

        self.setLayout(self.login_widget_layout)

    def registerUser(self):
        if self.password_field.getText() != self.repeat_password_field.getText():
            QMessageBox.warning(
                self,
                "passwords don't match",
                "Your password and repeated password do not match"
            )
            return

        login_controller = LoginController()
        login_controller.register(
            self.username_field.getText(),
            self.email.getText(),
            self.password_field.getText(),
            self.user_plan_combo_box.combo_box.currentIndex() + 1
        )
        self.returnToLogin()

    def returnToLogin(self):
        self.goBack.emit()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)
