from PyQt6.QtWidgets import QWidget, QLabel, QSizePolicy, QVBoxLayout

class SidePanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: red;")
        sidePanelLayout = QVBoxLayout(self)
        label = QLabel("left", self)
        sidePanelLayout.addWidget(label)
        sidePanelLayout.setContentsMargins(0, 0, 0, 0)
        sidePanelLayout.setSpacing(0)