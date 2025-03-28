from PyQt6.QtWidgets import QWidget, QLabel, QSizePolicy, QVBoxLayout

class PublicDataWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: blue;")
        publicDataLayout = QVBoxLayout(self)
        label = QLabel("right", self)
        publicDataLayout.addWidget(label)
        publicDataLayout.setContentsMargins(0, 0, 0, 0)
        publicDataLayout.setSpacing(0)