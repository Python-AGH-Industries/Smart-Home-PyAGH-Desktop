from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from src.ui.widgets.LoginWidget import LoginWidget
from src.ui.widgets.PanelWidget import PanelWidget
from src.ui.widgets.SidePanelWidget import SidePanelWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Home Panel")
        self.setMinimumSize(800, 600)

        self.loginWidget = LoginWidget()
        self.loginWidget.loginSuccessful.connect(self.loginToPanelTransition)

        self.setCentralWidget(self.loginWidget)

    def loginToPanelTransition(self):
        if self.loginWidget is not None:
            self.loginWidget.deleteLater()
            self.loginWidget = None

        self.wrapper = QWidget()

        self.panelWidget = PanelWidget()
        self.sidePanelWidget = SidePanelWidget()
        self.sidePanelWidget.logoutRequest.connect(self.panelToLoginTransition)
        self.sidePanelWidget.setMinimumWidth(100)

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

            self.loginWidget = LoginWidget()
            self.loginWidget.loginSuccessful.connect(self.loginToPanelTransition)

            self.setCentralWidget(self.loginWidget)