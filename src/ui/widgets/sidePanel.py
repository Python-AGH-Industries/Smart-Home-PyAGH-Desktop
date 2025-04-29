from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStyle, QStyleOption
from PyQt6.QtCore import Qt, pyqtSignal
from src.ui.widgets.iconButton import IconButton
from PyQt6.QtGui import QPainter

class SidePanel(QWidget):
    logoutRequest = pyqtSignal()
    showHomeRequest = pyqtSignal()
    showSettingsRequest = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        sidePanelLayout = QVBoxLayout(self)
        
        iconPath = "src/resources/icons/"

        homeButton = IconButton(iconPath + "home.png", self)
        helpButton = IconButton(iconPath + "question_mark.png", self)
        aboutButton = IconButton(iconPath + "info.png", self)
        settingsButton = IconButton(iconPath + "gear.png", self)
        logoutButton = IconButton(iconPath + "logout.png", self)

        homeButton.clicked.connect(self.showHomeRequest.emit)
        settingsButton.clicked.connect(self.showSettingsRequest.emit)
        logoutButton.clicked.connect(self.logoutRequest.emit)

        sidePanelLayout.addWidget(homeButton)
        sidePanelLayout.addWidget(helpButton)
        sidePanelLayout.addWidget(aboutButton)
        sidePanelLayout.addStretch(1)
        sidePanelLayout.addWidget(settingsButton)
        sidePanelLayout.addWidget(logoutButton)

        sidePanelLayout.setAlignment(
            homeButton,
            Qt.AlignmentFlag.AlignHCenter
        )

        sidePanelLayout.setAlignment(
            helpButton,
            Qt.AlignmentFlag.AlignHCenter
        )

        sidePanelLayout.setAlignment(
            aboutButton,
            Qt.AlignmentFlag.AlignHCenter
        )

        sidePanelLayout.setAlignment(
            settingsButton,
            Qt.AlignmentFlag.AlignHCenter
        )

        sidePanelLayout.setAlignment(
            logoutButton,
            Qt.AlignmentFlag.AlignHCenter
        )

        sidePanelLayout.setSpacing(10)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)