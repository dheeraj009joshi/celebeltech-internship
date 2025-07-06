# get_mnist.py

import gzip
import numpy as np
import os
import struct
from urllib.request import urlretrieve

def load_data(src, num_samples):
    print("Downloading " + src)
    gzfname, h = urlretrieve(src, "./delete.me")
    print("Done.")
    try:
        with gzip.open(gzfname) as gz:
            n = struct.unpack("I", gz.read(4))
            if n[0] != 0x3080000:
                raise Exception("Invalid file: unexpected magic number.")
            n = struct.unpack(">I", gz.read(4))[0]
            if n != num_samples:
                raise Exception(
                    "Invalid file: expected {0} entries.".format(num_samples)
                )
            crow = struct.unpack(">I", gz.read(4))[0]
            ccol = struct.unpack(">I", gz.read(4))[0]
            if crow != 28 or ccol != 28:
                raise Exception(
                    "Invalid file: expected 28 rows/cols per image."
                )
            # Read raw byte data (no normalization)
            res = np.frombuffer(
                gz.read(num_samples * crow * ccol), dtype=np.uint8
            )
    finally:
        os.remove(gzfname)
    return res.reshape((num_samples, crow, ccol))  # No division by 256.0

def load_labels(src, num_samples):
    print("Downloading " + src)
    gzfname, h = urlretrieve(src, "./delete.me")
    print("Done.")
    try:
        with gzip.open(gzfname) as gz:
            n = struct.unpack("I", gz.read(4))
            if n[0] != 0x1080000:
                raise Exception("Invalid file: unexpected magic number.")
            n = struct.unpack(">I", gz.read(4))
            if n[0] != num_samples:
                raise Exception(
                    "Invalid file: expected {0} rows.".format(num_samples)
                )
            res = np.frombuffer(gz.read(num_samples), dtype=np.uint8)
    finally:
        os.remove(gzfname)
    return res.reshape((num_samples))


def try_download(data_source, label_source, num_samples):
    data = load_data(data_source, num_samples)
    labels = load_labels(label_source, num_samples)
    return data, labels


def get_mnist():
    server = 'https://raw.githubusercontent.com/fgnt/mnist/master'
    url_train_image = f'{server}/train-images-idx3-ubyte.gz'
    url_train_labels = f'{server}/train-labels-idx1-ubyte.gz'
    num_train_samples = 60000

    print("Downloading train data")
    train_features, train_labels = try_download(url_train_image, url_train_labels, num_train_samples)

    url_test_image = f'{server}/t10k-images-idx3-ubyte.gz'
    url_test_labels = f'{server}/t10k-labels-idx1-ubyte.gz'
    num_test_samples = 10000

    print("Downloading test data")
    test_features, test_labels = try_download(url_test_image, url_test_labels, num_test_samples)

    return train_features, train_labels, test_features, test_labels