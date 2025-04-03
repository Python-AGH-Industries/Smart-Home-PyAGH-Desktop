from PyQt6.QtWidgets import QApplication
from src.ui.windows.MainWindow import MainWindow

def main():
    app = QApplication([])
    qss = "./style.qss"
    with open(qss, "r") as fh:
        app.setStyleSheet(fh.read())
    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__": 
    main()


