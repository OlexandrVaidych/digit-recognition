import numpy as np
from PIL import Image
import tensorflow as tf


class DigitRecognizer:
    def __init__(self):
        self.model = tf.keras.models.load_model("digit_model.h5")

    def preprocess_image(self, image):
        # Convert the QPixmap to a QImage
        qimage = image.toImage()

        # Convert the QImage to a PIL Image
        pil_image = Image.fromqimage(qimage)

        # Convert the image to grayscale
        grayscale_image = pil_image.convert("L")

        # Resize the image to the desired input shape of the model
        resized_image = grayscale_image.resize((28, 28))

        # Convert the image to a NumPy array
        image_array = np.array(resized_image)

        # Normalize the pixel values between 0 and 1
        normalized_image = image_array / 255.0

        return normalized_image


    def digit_recognize(self, image):
        # Convert the preprocessed image to a format suitable for the model
        preprocessed_image = self.preprocess_image(image)

        # Assuming the model expects input of shape (batch_size, height, width, channels)
        input_image = preprocessed_image[np.newaxis, :, :, np.newaxis]

        # Perform digit recognition using the loaded model
        predicted_labels = self.model.predict(input_image)
        predicted_digit = np.argmax(predicted_labels)

        return str(predicted_digit)
