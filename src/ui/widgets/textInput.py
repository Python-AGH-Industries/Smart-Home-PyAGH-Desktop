from PyQt6.QtWidgets import QLineEdit

class TextInput():
    def __init__(self,placeholderText):
        super().__init__()

        self.object = QLineEdit()
        self.object.setPlaceholderText(placeholderText)
        self.object.setStyleSheet("""padding: 5px;       
    margin: 5px 100px;  /* vertical | horizontal */

""")
    def append(self,layout):
        layout.addWidget(self.object)
    def getText(self):
        return self.object.text()