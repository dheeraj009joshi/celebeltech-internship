# image_utils.py

from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import BinaryType
import pandas as pd


@pandas_udf(BinaryType())
def read_image_binary(paths):
    def read_file(path):
        with open(path, 'rb') as f:
            return bytearray(f.read())
    return paths.apply(read_file)