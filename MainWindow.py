from PyQt6.QtWidgets import QMainWindow
from LoginWidget import LoginWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Home Panel")
        self.setMinimumSize(800, 600)

        loginWidget = LoginWidget()

        self.setCentralWidget(loginWidget)

