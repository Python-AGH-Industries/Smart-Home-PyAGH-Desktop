from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

class IconButton(QPushButton):
    def __init__(self, path = "", parent = None):
        super().__init__(parent)
        self.setFixedSize(80, 80)
        self.setIcon(QIcon(path))
        self.setIconSize(QSize(70, 70))