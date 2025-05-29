from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt

from src.model.styleLoader import styleLoader
from src.ui.widgets.expandableSection import ExpandableSection


class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Help")
        self.setMinimumSize(600, 400)
        
        # Create main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.setStyleSheet(
            styleLoader.load("./src/resources/styles/sidePanel.qss")
        )

        # Create scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # Create content widget
        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_widget.setLayout(content_layout)
        
        # Add help sections
        sections = [
            ("Generating Reports", """
            To generate a report:
            1. Go to the Reports section
            2. Select the date range
            3. Choose the type of report
            4. Click 'Generate Report'
            5. The report will be saved in your documents folder
            """),
            
            ("Changing Password", """
            To change your password:
            1. Click on your profile icon
            2. Select 'Settings'
            3. Choose 'Change Password'
            4. Enter your current password
            5. Enter and confirm your new password
            6. Click 'Save Changes'
            """),
            
            ("Managing Sensors", """
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
        
        # Add sections to layout
        for title, content in sections:
            section = ExpandableSection(title, content)
            content_layout.addWidget(section)
        
        # Add stretch to push content to the top
        content_layout.addStretch()
        
        # Set the scroll area's widget
        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)
