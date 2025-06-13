from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QStyleOption, QStyle
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices, QPainter

from src.model.styleLoader import style_loader


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setMinimumSize(400, 300)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        # Create main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.setStyleSheet(
            style_loader.load("./src/resources/styles/about.qss")
        )

        # Project title
        title_label = QLabel("Smart Home PyAGH")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # Description
        description = """
        Smart Home PyAGH is a comprehensive smart home management system developed as part of the AGH UST Python course.
        The project consists of three main components:
        - Desktop application (GUI)
        - Backend server
        - Firmware for nRF7002DK board
        
        This system allows users to monitor and control various aspects of their smart home environment, including:
        • Temperature monitoring
        • Humidity tracking
        • Pressure measurements
        • Light intensity monitoring
        
        The application provides real-time data visualization, customizable reports, and user-friendly interface for managing your smart home environment.
        """
        desc_label = QLabel(description)
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("margin: 20px;")
        main_layout.addWidget(desc_label)

        # Authors
        authors_label = QLabel("Authors:")
        authors_label.setStyleSheet("font-weight: bold; margin: 20px 20px 5px 20px;")
        main_layout.addWidget(authors_label)

        authors = "• Beniamin Buzun\n• Adrian Suliga"
        authors_text = QLabel(authors)
        authors_text.setStyleSheet("margin: 0 20px;")
        main_layout.addWidget(authors_text)

        # GitHub link
        github_button = QPushButton("GitHub Repository")
        github_button.setStyleSheet("""
            QPushButton {
                background-color: #2ea44f;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                margin: 20px;
            }
            QPushButton:hover {
                background-color: #2c974b;
            }
        """)
        github_button.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/Python-AGH-Industries")))
        main_layout.addWidget(github_button)

        # Add stretch to push everything to the top
        main_layout.addStretch()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)
