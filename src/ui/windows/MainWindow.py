from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QStackedLayout

from src.model.loginController import LoginController
from src.model.styleLoader import styleLoader
from src.ui.widgets.login import Login
from src.ui.widgets.panel import Panel
from src.ui.widgets.settingsPanel import SettingsPanel
from src.ui.widgets.register import Register
from src.ui.widgets.sidePanel import SidePanel
from src.ui.windows.helpWindow import HelpWindow
from src.ui.windows.aboutWindow import AboutWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Home Panel")
        self.setMinimumSize(1200, 800)

        self.login_widget = Login()
        self.login_widget.setStyleSheet(
            styleLoader.load("./src/resources/styles/login.qss")
        )

        self.login_widget.loginSuccessful.connect(self.loginToPanelTransition)
        self.login_widget.register.connect(self.loginToRegisterTransition)

        self.setCentralWidget(self.login_widget)

    def loginToPanelTransition(self):
        if self.login_widget is not None:
            self.login_widget.deleteLater()
            self.login_widget = None

        self.wrapper = QWidget()
        self.content_wrapper = QWidget()

        self.content_layout = QStackedLayout(self.content_wrapper)

        # List of panels displayed
        self.panel_widget = Panel()
        self.settings_widget = SettingsPanel()
        self.about_widget = AboutWindow()
        self.help_widget = HelpWindow()

        self.content_layout.addWidget(self.panel_widget)
        self.content_layout.addWidget(self.settings_widget)
        self.content_layout.addWidget(self.help_widget)
        self.content_layout.addWidget(self.about_widget)

        self.side_panel_widget = SidePanel()
        self.side_panel_widget.logoutRequest.connect(self.panelToLoginTransition)
        self.side_panel_widget.setFixedWidth(100)

        self.side_panel_widget.showHomeRequest.connect(
            lambda: self.content_layout.setCurrentIndex(0)
        )
        self.side_panel_widget.showSettingsRequest.connect(
            lambda: self.content_layout.setCurrentIndex(1)
        )
        self.side_panel_widget.showHelpRequest.connect(
            lambda: self.content_layout.setCurrentIndex(2)
        )
        self.side_panel_widget.showAboutRequest.connect(
            lambda: self.content_layout.setCurrentIndex(3)
        )

        self.panel_widget.setStyleSheet(
            styleLoader.load("./src/resources/styles/panel.qss")
        )

        self.panel_widget.public_data_widget.setStyleSheet(
            styleLoader.load("./src/resources/styles/publicSubPanel.qss")
        )

        self.settings_widget.setStyleSheet(
            styleLoader.load("./src/resources/styles/panel.qss")
        )

        self.side_panel_widget.setStyleSheet(
            styleLoader.load("./src/resources/styles/sidePanel.qss")
        )

        self.settings_widget.theme_combo_box.combo_box.currentTextChanged.connect(
            self.styleToggle
        )

        wrapper_layout = QHBoxLayout(self.wrapper)
        wrapper_layout.addWidget(self.side_panel_widget)
        wrapper_layout.addWidget(self.content_wrapper)

        wrapper_layout.setContentsMargins(0, 0, 0, 0)
        wrapper_layout.setSpacing(0)

        self.setCentralWidget(self.wrapper)

    def panelToLoginTransition(self):
        if self.panel_widget is not None:
            self.panel_widget.deleteLater()
            self.panel_widget = None

        if self.side_panel_widget is not None:
            self.side_panel_widget.deleteLater()
            self.side_panel_widget = None

        self.login_controller = LoginController()
        self.login_controller.logout()
        self.login_widget = Login()
        self.login_widget.setStyleSheet(
            styleLoader.load("./src/resources/styles/login.qss")
        )

        self.login_widget.loginSuccessful.connect(self.loginToPanelTransition)
        self.login_widget.register.connect(self.loginToRegisterTransition)

        self.setCentralWidget(self.login_widget)

    def loginToRegisterTransition(self):
        if self.login_widget is not None:
            self.login_widget.deleteLater()
            self.login_widget = None

        self.login_widget = Register()
        self.login_widget.goBack.connect(self.registrationToLoginTransition)
        self.login_widget.setStyleSheet(
            styleLoader.load("./src/resources/styles/register.qss")
        )

        self.setCentralWidget(self.login_widget)
    
    def registrationToLoginTransition(self):
        if self.login_widget is not None:
            self.login_widget.deleteLater()
            self.login_widget = None

        self.login_widget = Login()
        self.login_widget.setStyleSheet(
            styleLoader.load("./src/resources/styles/login.qss")
        )

        self.login_widget.loginSuccessful.connect(self.loginToPanelTransition)
        self.login_widget.register.connect(self.loginToRegisterTransition)

        self.setCentralWidget(self.login_widget)

    def styleToggle(self):
        new_text = self.settings_widget.theme_combo_box.combo_box.currentText()
        if new_text == "light":
            self.panel_widget.setStyleSheet(
                styleLoader.load("./src/resources/styles/light_panel.qss")
            )

            self.panel_widget.public_data_widget.setStyleSheet(
                styleLoader.load("./src/resources/styles/light_publicSubPanel.qss")
            )

            self.settings_widget.setStyleSheet(
                styleLoader.load("./src/resources/styles/light_panel.qss")
            )

            self.side_panel_widget.setStyleSheet(
                styleLoader.load("./src/resources/styles/light_sidePanel.qss")
            )
        else:
            self.panel_widget.setStyleSheet(
                styleLoader.load("./src/resources/styles/panel.qss")
            )

            self.panel_widget.public_data_widget.setStyleSheet(
                styleLoader.load("./src/resources/styles/publicSubPanel.qss")
            )

            self.settings_widget.setStyleSheet(
                styleLoader.load("./src/resources/styles/panel.qss")
            )

            self.side_panel_widget.setStyleSheet(
                styleLoader.load("./src/resources/styles/sidePanel.qss")
            )
