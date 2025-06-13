from PyQt6.QtWidgets import QWidget, QLabel, QComboBox, QHBoxLayout

class LabelComboBox(QWidget):
    def __init__(self, text, options, parent = None, end_with_stretch = False):
        super().__init__()
        combo_box_layout = QHBoxLayout(self)
        self.setParent(parent)

        description = QLabel(text, self)
        description.setWordWrap(True)

        self.combo_box = QComboBox(self)
        self.combo_box.addItems(options)

        combo_box_layout.addWidget(description)
        combo_box_layout.addWidget(self.combo_box)

        if end_with_stretch:
            combo_box_layout.addStretch(1)

        combo_box_layout.setContentsMargins(0, 0, 0, 0)
        combo_box_layout.setSpacing(0)