import os
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from app.MainWindow import MainWindow
from app.resources import resource_path


if __name__ == "__main__":
    app = QApplication(sys.argv)
    icon_path = resource_path("icons", "icon.ico")
    app.setWindowIcon(QIcon(icon_path))
    window = MainWindow(app)
    window.show()
    sys.exit(app.exec())
    