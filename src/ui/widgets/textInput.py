from PyQt6.QtWidgets import QLineEdit

class TextInput():
    def __init__(self, placeholder_text):
        self.object = QLineEdit()
        self.object.setPlaceholderText(placeholder_text)
        
    def append(self, layout):
        layout.addWidget(self.object)

    def getText(self):
        return self.object.text()