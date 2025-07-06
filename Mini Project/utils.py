# utils.py

import os
import glob
import random


def get_random_image_paths(base_dir, num_samples=5):
    all_paths = []

    for label in range(10):
        label_dir = os.path.join(base_dir, str(label))
        if not os.path.isdir(label_dir):
            continue
        image_files = glob.glob(os.path.join(label_dir, "*.png"))
        selected = random.sample(image_files, min(num_samples, len(image_files)))
        all_paths.extend([(path, label) for path in selected])

    return all_paths