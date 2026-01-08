import cv2
import numpy as np

def preprocess_image(path, size=2):
    # Read image in grayscale
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Resize to size x size (2x2 for FRQI simplicity)
    img = cv2.resize(img, (size, size))

    # Normalize pixel values to [0,1]
    img = img / 255.0

    return img

if __name__ == "__main__":
    image = preprocess_image("data/sample.png")
    print("Preprocessed Image:\n", image)
