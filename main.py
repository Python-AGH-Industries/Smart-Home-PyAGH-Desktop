from PyQt6.QtWidgets import QApplication
from src.ui.windows.MainWindow import MainWindow

def main():
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__": 
    main()