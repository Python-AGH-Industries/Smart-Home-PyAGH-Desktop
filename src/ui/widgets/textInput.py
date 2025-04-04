from PyQt6.QtWidgets import QLineEdit

class TextInput():
    def __init__(self,placeholderText):
        self.object = QLineEdit()
        self.object.setPlaceholderText(placeholderText)
    def append(self,layout):
        layout.addWidget(self.object)
    def getText(self):
        return self.object.text()