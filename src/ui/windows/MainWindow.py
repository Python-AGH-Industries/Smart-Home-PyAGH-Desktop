from PyQt6.QtWidgets import QMainWindow
from src.ui.widgets.LoginWidget import LoginWidget
from src.ui.widgets.PanelWidget import PanelWidget

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

        self.panelWidget = PanelWidget()
        self.setCentralWidget(self.panelWidget)