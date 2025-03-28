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

        wrapperLayout = QHBoxLayout(self.wrapper)
        wrapperLayout.addWidget(self.sidePanelWidget, stretch = 1)
        wrapperLayout.addWidget(self.panelWidget, stretch = 9)

        wrapperLayout.setContentsMargins(0, 0, 0, 0)
        wrapperLayout.setSpacing(0)

        self.setCentralWidget(self.wrapper)