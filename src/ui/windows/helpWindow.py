from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QStyleOption, QStyle
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter

from src.model.styleLoader import style_loader
from src.ui.widgets.expandableSection import ExpandableSection


class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Help")
        self.setMinimumSize(600, 400)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        # Create main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.setStyleSheet(
            style_loader.load("./src/resources/styles/help_window.qss")
        )

        # allow for scrolling
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_widget.setLayout(content_layout)
        
        # Help Sections
        sections = [
            ("Generating Reports", """
            To generate a report:
            1. Go to main page
            2. Select sensor you want to generate report form
            3. From bar above graph choose type of report
            4. Save the report file
            5. The report will be saved in selected folder
            """),
            
            ("Changing Password", """
            To change your password:
            1. Click on the settings icon
            2. Enter current password
            3. Enter new password
            4. Save changes
            5. Confirm the change
            """),
            
            ("Change sensor displayed", """
            To manage your sensors:
            1. Go to the Sensors section
            2. To rename a sensor:
               - Click on the sensor
               - Click the edit icon
               - Enter new name
               - Click 'Save'
            3. To add a new sensor:
               - Click 'Add Sensor'
               - Follow the setup wizard
            """),
            
            ("Viewing Statistics", """
            To view statistics:
            1. Go to the Dashboard
            2. Select the time period
            3. Choose the type of statistics
            4. View the graphs and data
            5. Export if needed
            """),
            
            ("System Settings", """
            To access system settings:
            1. Click on the gear icon
            2. Choose from available options:
               - Display settings
               - Notification preferences
               - System preferences
               - Backup settings
            """)
        ]
        
        # generate sections of help
        for title, content in sections:
            section = ExpandableSection(title, content)
            content_layout.addWidget(section)
        
        content_layout.addStretch()

        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

        super().paintEvent(event)
