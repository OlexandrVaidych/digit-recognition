from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel

from DigitRecognizer import DigitRecognizer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 300)

        # Create a QLabel widget to display the image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(50, 50, 300, 200)  # Set the label position and size

        # Create a QPushButton widget to load the image
        self.load_button = QPushButton("Load Image", self)
        self.load_button.setGeometry(50, 270, 100, 30)  # Set the button position and size
        self.load_button.clicked.connect(self.load_image)

        # Create a QPushButton widget for digit recognition
        self.recognize_button = QPushButton("Digit Recognition", self)
        self.recognize_button.setGeometry(200, 270, 150, 30)  # Set the button position and size
        self.recognize_button.clicked.connect(self.perform_digit_recognition)

        self.loaded_image = None

    def load_image(self):
        # Open a file dialog to select an image file
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            file_path = file_dialog.selectedFiles()[0]

            # Load and set the image
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)
            self.loaded_image = pixmap

    def perform_digit_recognition(self):
        if self.loaded_image is not None:
            # Perform digit recognition on the loaded image
            digit_recognizer = DigitRecognizer()
            recognized_digit = digit_recognizer.digit_recognize(self.loaded_image)

            print(f"Recognized digit: {recognized_digit}")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()