# data_processor.py
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType
from utils import get_random_image_paths
from image_utils import read_image_binary
from config import BASE_DIR


def load_and_process_data(spark):
    # Step 1: Get list of random image paths + labels
    sample_files = get_random_image_paths(BASE_DIR, num_samples=5)

    # Step 2: Create DataFrame with image paths and labels
    schema = StructType([
        StructField("image_path", StringType(), True),
        StructField("label", StringType(), True)
    ])

    df = spark.createDataFrame(sample_files, ["image_path", "label"])

    # Step 3: Read image binary data
    df_with_binary = df.withColumn("image_binary", read_image_binary(col("image_path")))

    # Step 4: Select final columns
    final_df = df_with_binary.select("image_binary", col("label").cast("string"))

    return final_df