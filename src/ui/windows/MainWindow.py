from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QStackedLayout
from PyQt6.QtCore import Qt

from src.model.loginController import LoginController
from src.model.styleLoader import style_loader
from src.ui.widgets.login import Login
from src.ui.widgets.panel import Panel
from src.ui.windows.settingsPanel import SettingsPanel
from src.ui.widgets.register import Register
from src.ui.widgets.sidePanel import SidePanel
from src.ui.windows.helpWindow import HelpWindow
from src.ui.windows.aboutWindow import AboutWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Home Panel")
        self.setMinimumSize(1200, 800)

        self.loginWidget = Login()
        self.loginWidget.setStyleSheet(
            style_loader.load("./src/resources/styles/login.qss")
        )

        self.loginWidget.loginSuccessful.connect(self.login_to_panel_transition)
        self.loginWidget.register.connect(self.login_to_register_transition)

        self.setCentralWidget(self.loginWidget)

    def login_to_panel_transition(self):
        if self.loginWidget is not None:
            self.loginWidget.deleteLater()
            self.loginWidget = None

        self.wrapper = QWidget()
        self.contentWrapper = QWidget()

        self.contentLayout = QStackedLayout(self.contentWrapper)

        # List of panels displayed
        self.panelWidget = Panel()
        self.settingsWidget = SettingsPanel()
        self.aboutWidget = AboutWindow()
        self.helpWidget = HelpWindow()

        self.contentLayout.addWidget(self.panelWidget)
        self.contentLayout.addWidget(self.settingsWidget)
        self.contentLayout.addWidget(self.helpWidget)
        self.contentLayout.addWidget(self.aboutWidget)

        self.sidePanelWidget = SidePanel()
        self.sidePanelWidget.logoutRequest.connect(self.panel_to_login_transition)
        self.sidePanelWidget.setFixedWidth(100)

        self.sidePanelWidget.showHomeRequest.connect(
            lambda: self.contentLayout.setCurrentIndex(0)
        )
        self.sidePanelWidget.showSettingsRequest.connect(
            lambda: self.contentLayout.setCurrentIndex(1)
        )
        self.sidePanelWidget.showHelpRequest.connect(
            lambda: self.contentLayout.setCurrentIndex(2)
        )
        self.sidePanelWidget.showAboutRequest.connect(
            lambda: self.contentLayout.setCurrentIndex(3)
        )

        self.panelWidget.setStyleSheet(
            style_loader.load("./src/resources/styles/panel.qss")
        )

        self.panelWidget.publicDataWidget.setStyleSheet(
            style_loader.load("./src/resources/styles/publicSubPanel.qss")
        )

        self.settingsWidget.setStyleSheet(
            style_loader.load("./src/resources/styles/panel.qss")
        )

        self.sidePanelWidget.setStyleSheet(
            style_loader.load("./src/resources/styles/sidePanel.qss")
        )

        self.settingsWidget.themeComboBox.comboBox.currentTextChanged.connect(
            self.style_toggle
        )

        wrapperLayout = QHBoxLayout(self.wrapper)
        wrapperLayout.addWidget(self.sidePanelWidget)
        wrapperLayout.addWidget(self.contentWrapper)

        wrapperLayout.setContentsMargins(0, 0, 0, 0)
        wrapperLayout.setSpacing(0)

        self.setCentralWidget(self.wrapper)

    def panel_to_login_transition(self):
        if self.panelWidget is not None:
            self.panelWidget.deleteLater()
            self.panelWidget = None

        if self.sidePanelWidget is not None:
            self.sidePanelWidget.deleteLater()
            self.sidePanelWidget = None

        self.loginController = LoginController()
        self.loginController.logout()
        self.loginWidget = Login()
        self.loginWidget.setStyleSheet(
            style_loader.load("./src/resources/styles/login.qss")
        )

        self.loginWidget.loginSuccessful.connect(self.login_to_panel_transition)
        self.loginWidget.register.connect(self.login_to_register_transition)

        self.setCentralWidget(self.loginWidget)

    def login_to_register_transition(self):
        if self.loginWidget is not None:
            self.loginWidget.deleteLater()
            self.loginWidget = None

        self.loginWidget = Register()
        self.loginWidget.goBack.connect(self.registration_to_login_transition)
        self.loginWidget.setStyleSheet(
            style_loader.load("./src/resources/styles/register.qss")
        )

        self.setCentralWidget(self.loginWidget)
    
    def registration_to_login_transition(self):
        if self.loginWidget is not None:
            self.loginWidget.deleteLater()
            self.loginWidget = None

        self.loginWidget = Login()
        self.loginWidget.setStyleSheet(
            style_loader.load("./src/resources/styles/login.qss")
        )

        self.loginWidget.loginSuccessful.connect(self.login_to_panel_transition)
        self.loginWidget.register.connect(self.login_to_register_transition)

        self.setCentralWidget(self.loginWidget)

    def style_toggle(self):
        new_text = self.settingsWidget.themeComboBox.comboBox.currentText()
        if new_text == "light":
            self.panelWidget.setStyleSheet(
                style_loader.load("./src/resources/styles/light_panel.qss")
            )

            self.panelWidget.publicDataWidget.setStyleSheet(
                style_loader.load("./src/resources/styles/light_publicSubPanel.qss")
            )

            self.settingsWidget.setStyleSheet(
                style_loader.load("./src/resources/styles/light_panel.qss")
            )

            self.sidePanelWidget.setStyleSheet(
                style_loader.load("./src/resources/styles/light_sidePanel.qss")
            )
        else:
            self.panelWidget.setStyleSheet(
                style_loader.load("./src/resources/styles/panel.qss")
            )

            self.panelWidget.publicDataWidget.setStyleSheet(
                style_loader.load("./src/resources/styles/publicSubPanel.qss")
            )

            self.settingsWidget.setStyleSheet(
                style_loader.load("./src/resources/styles/panel.qss")
            )

            self.sidePanelWidget.setStyleSheet(
                style_loader.load("./src/resources/styles/sidePanel.qss")
            )
