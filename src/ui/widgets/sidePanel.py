from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStyle, QStyleOption
from PyQt6.QtCore import Qt, pyqtSignal
from src.ui.widgets.iconButton import IconButton
from PyQt6.QtGui import QPainter

class SidePanel(QWidget):
    logoutRequest = pyqtSignal()
    showHomeRequest = pyqtSignal()
    showSettingsRequest = pyqtSignal()
    showHelpRequest = pyqtSignal()
    showAboutRequest = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        side_panel_layout = QVBoxLayout(self)
        
        icon_path = "src/resources/icons/"

        home_button = IconButton(icon_path + "home.png", self)
        help_button = IconButton(icon_path + "question_mark.png", self)
        about_button = IconButton(icon_path + "info.png", self)
        settings_button = IconButton(icon_path + "gear.png", self)
        logout_button = IconButton(icon_path + "logout.png", self)

        home_button.clicked.connect(self.showHomeRequest.emit)
        settings_button.clicked.connect(self.showSettingsRequest.emit)
        logout_button.clicked.connect(self.logoutRequest.emit)
        help_button.clicked.connect(self.showHelpRequest.emit)
        about_button.clicked.connect(self.showAboutRequest.emit)

        side_panel_layout.addWidget(home_button)
        side_panel_layout.addWidget(help_button)
        side_panel_layout.addWidget(about_button)
        side_panel_layout.addStretch(1)
        side_panel_layout.addWidget(settings_button)
        side_panel_layout.addWidget(logout_button)

        side_panel_layout.setAlignment(
            home_button,
            Qt.AlignmentFlag.AlignHCenter
        )

        side_panel_layout.setAlignment(
            help_button,
            Qt.AlignmentFlag.AlignHCenter
        )

        side_panel_layout.setAlignment(
            about_button,
            Qt.AlignmentFlag.AlignHCenter
        )

        side_panel_layout.setAlignment(
            settings_button,
            Qt.AlignmentFlag.AlignHCenter
        )

        side_panel_layout.setAlignment(
            logout_button,
            Qt.AlignmentFlag.AlignHCenter
        )

        side_panel_layout.setSpacing(10)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)