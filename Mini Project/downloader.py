# downloader.py

import os
import numpy as np
from PIL import Image

from get_mnist import get_mnist  # We'll save the shared function below

OUTPUT_DIR = 'flat files/mnist_png'


def save_samples(images, labels, output_dir, prefix=""):
    """Convert image bytes to PNG and save by label"""
    for idx, (img, label) in enumerate(zip(images, labels)):
        img_array = img.astype(np.uint8)  # Ensure uint8 format
        img_pil = Image.fromarray(img_array)
        label_dir = os.path.join(output_dir, str(label))
        os.makedirs(label_dir, exist_ok=True)
        img_pil.save(os.path.join(label_dir, f"{prefix}_{idx}.png"))

def convert_local_mnist_to_png(num_samples=500):
    """Use local MNIST files or download them, then convert to PNG samples"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Downloading and parsing MNIST dataset...")
    train_images, train_labels, test_images, test_labels = get_mnist()

    print(f"Saving {num_samples} sample training images...")
    save_samples(train_images[:num_samples], train_labels[:num_samples], OUTPUT_DIR, "train")

    print(f"Saving {num_samples} sample test images...")
    save_samples(test_images[:num_samples], test_labels[:num_samples], OUTPUT_DIR, "test")

    print("MNIST PNG dataset generated at:", OUTPUT_DIR)