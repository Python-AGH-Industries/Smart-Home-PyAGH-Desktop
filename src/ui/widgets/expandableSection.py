from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve

from src.model.styleLoader import styleLoader


class ExpandableSection(QWidget):
    def __init__(self, title, content, parent = None):
        super().__init__(parent)
        self.setLayout(QVBoxLayout())

        self.expand_button = QPushButton(title)
        self.expand_button.setCheckable(True)
        self.expand_button.setStyleSheet(
            styleLoader.load("./src/resources/styles/expandable_section.qss")
        )

        self.expand_button.clicked.connect(self.toggleContent)

        self.content = QWidget()
        content_layout = QVBoxLayout()
        self.content.setLayout(content_layout)

        content_label = QLabel(content)
        content_label.setWordWrap(True)
        content_layout.addWidget(content_label)

        self.layout().addWidget(self.expand_button)
        self.layout().addWidget(self.content)
        self.content.hide()

        self.animation = QPropertyAnimation(self.content, b"maximumHeight")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.animation.finished.connect(self.onAnimationFinsihed)

    def toggleContent(self):
        if self.expand_button.isChecked():
            self.content.show()
            self.animation.setStartValue(0)
            self.animation.setEndValue(self.content.sizeHint().height())
            self.animation.start()
        else:
            self.animation.setStartValue(self.content.height())
            self.animation.setEndValue(0)
            self.animation.start()

    def onAnimationFinsihed(self):
        if not self.expand_button.isChecked():
            self.content.hide()
