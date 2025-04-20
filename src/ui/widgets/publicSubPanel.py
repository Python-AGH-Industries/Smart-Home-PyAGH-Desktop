from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class PublicSubPanel(QWidget):
    def __init__(self):
        super().__init__()
        
        publicDataLayout = QVBoxLayout(self)
        publicDataLayout.setContentsMargins(0, 0, 0, 0)
        publicDataLayout.setSpacing(0)
        
        label = QLabel("panel under construction", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)  
        
        publicDataLayout.addWidget(label)