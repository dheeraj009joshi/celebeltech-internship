# spark_utils.py

from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

def create_spark_session():
    spark_ = SparkSession.builder \
        .appName("MNISTDeltaTable") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.jars.packages", "io.delta:delta-core_2.12:3.0.0") \
        
    spark=configure_spark_with_delta_pip(spark_).getOrCreate()

    return spark