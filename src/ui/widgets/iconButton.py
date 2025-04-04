from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

class IconButton(QPushButton):
    def __init__(self, path = "", parent = None, fixedSize = 80):
        super().__init__(parent)
        self.setFixedSize(QSize(fixedSize, fixedSize))
        self.setIcon(QIcon(path))
        
        offset = fixedSize / 6

        self.setIconSize(QSize(int(fixedSize - offset), int(fixedSize - offset)))