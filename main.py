from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 300)

        # Create a QPushButton widget to load the image
        self.load_button = QPushButton("Load Image", self)
        self.load_button.setGeometry(50, 270, 100, 30)  # Set the button position and size


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()