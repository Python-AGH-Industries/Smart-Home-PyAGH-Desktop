from PyQt6.QtWidgets import QApplication

from src.model.loginController import LoginController
from src.ui.windows.MainWindow import MainWindow

def main():
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()