from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout

from src.model.styleLoader import styleLoader
from src.ui.widgets.login import Login
from src.ui.widgets.panel import Panel
from src.ui.widgets.register import Register
from src.ui.widgets.sidePanel import SidePanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Home Panel")
        self.setMinimumSize(1200, 800)

        self.loginWidget = Login()
        self.loginWidget.setStyleSheet(styleLoader.load("./src/resources/styles/login.qss"))

        self.loginWidget.loginSuccessful.connect(self.loginToPanelTransition)
        self.loginWidget.register.connect(self.loginToRegisterTransition)

        self.setCentralWidget(self.loginWidget)

    def loginToPanelTransition(self):
        if self.loginWidget is not None:
            self.loginWidget.deleteLater()
            self.loginWidget = None

        self.wrapper = QWidget()

        self.panelWidget = Panel()
        self.sidePanelWidget = SidePanel()
        self.sidePanelWidget.logoutRequest.connect(self.panelToLoginTransition)
        self.sidePanelWidget.setFixedWidth(100)

        wrapperLayout = QHBoxLayout(self.wrapper)
        wrapperLayout.addWidget(self.sidePanelWidget)
        wrapperLayout.addWidget(self.panelWidget)

        wrapperLayout.setContentsMargins(0, 0, 0, 0)
        wrapperLayout.setSpacing(0)

        self.setCentralWidget(self.wrapper)

    def panelToLoginTransition(self):
        if self.panelWidget is not None:
            self.panelWidget.deleteLater()
            self.panelWidget = None

        if self.sidePanelWidget is not None:
            self.sidePanelWidget.deleteLater()
            self.sidePanelWidget = None

        self.loginWidget = Login()
        self.loginWidget.setStyleSheet(styleLoader.load("./src/resources/styles/login.qss"))

        self.loginWidget.loginSuccessful.connect(self.loginToPanelTransition)
        self.loginWidget.register.connect(self.loginToRegisterTransition)

        self.setCentralWidget(self.loginWidget)

    def loginToRegisterTransition(self):
        if self.loginWidget is not None:
            self.loginWidget.deleteLater()
            self.loginWidget = None

        self.loginWidget = Register()
        self.loginWidget.goBack.connect(self.registrationToLoginTransition)

        self.setCentralWidget(self.loginWidget)
    
    def registrationToLoginTransition(self):
        if self.loginWidget is not None:
            self.loginWidget.deleteLater()
            self.loginWidget = None

        self.loginWidget = Login()
        self.loginWidget.setStyleSheet(styleLoader.load("./src/resources/styles/login.qss"))

        self.loginWidget.loginSuccessful.connect(self.loginToPanelTransition)
        self.loginWidget.register.connect(self.loginToRegisterTransition)

        self.setCentralWidget(self.loginWidget)
