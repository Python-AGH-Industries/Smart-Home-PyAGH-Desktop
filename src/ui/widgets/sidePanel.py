from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from src.ui.widgets.iconButton import IconButton

class SidePanel(QWidget):
    logoutRequest = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(100, 100, 100);")
        sidePanelLayout = QVBoxLayout(self)
        
        iconPath = "src/resources/icons/"

        homeButton = IconButton(iconPath + "home.png", self)
        helpButton = IconButton(iconPath + "question_mark.png", self)
        aboutButton = IconButton(iconPath + "info.png", self)
        logoutButton = IconButton(iconPath + "logout.png", self)

        logoutButton.clicked.connect(self.logoutHandler)

        sidePanelLayout.addWidget(homeButton)
        sidePanelLayout.addWidget(helpButton)
        sidePanelLayout.addWidget(aboutButton)
        sidePanelLayout.addStretch(1)
        sidePanelLayout.addWidget(logoutButton)

        sidePanelLayout.setAlignment(homeButton, Qt.AlignmentFlag.AlignHCenter)
        sidePanelLayout.setAlignment(helpButton, Qt.AlignmentFlag.AlignHCenter)
        sidePanelLayout.setAlignment(aboutButton, Qt.AlignmentFlag.AlignHCenter)
        sidePanelLayout.setAlignment(logoutButton, Qt.AlignmentFlag.AlignHCenter)

        sidePanelLayout.setSpacing(10)

    def logoutHandler(self):
        self.logoutRequest.emit()