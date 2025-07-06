# main.py

import os
from downloader import convert_local_mnist_to_png

from spark_utils import create_spark_session
from data_processor import load_and_process_data
from config import BASE_DIR, DELTA_TABLE_NAME


def main():
    # Step 1: Download MNIST if needed


    if not os.path.exists(BASE_DIR) or not os.listdir(BASE_DIR):
        print(f"{BASE_DIR} is empty or doesn't exist. Generating MNIST PNG dataset...")
        convert_local_mnist_to_png(num_samples=500)  # adjust as needed
    else:
        print("Using existing MNIST PNG data.")

    # Step 2: Create Spark session
    spark = create_spark_session()

    # Step 3: Load and process data
    final_df = load_and_process_data(spark)

    # Step 4: Write to Delta Table
    print("Writing to managed Delta table...")
    final_df.write.format("delta").mode("overwrite").saveAsTable(DELTA_TABLE_NAME)

    print("✅ Managed Delta Table created successfully.")
    spark.sql(f"DESCRIBE TABLE {DELTA_TABLE_NAME}").show(truncate=False)
    spark.stop()



if __name__ == "__main__":
    main()