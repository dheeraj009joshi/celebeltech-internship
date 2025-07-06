from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

builder = SparkSession.builder \
    .appName("Delta Test") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:3.0.0")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

df = spark.createDataFrame([(1, "apple"), (2, "banana")], ["id", "fruit"])
df.write.format("delta").mode("overwrite").save("/tmp/delta-test")
df = spark.read.format("delta").load("/tmp/delta-test")
df.show()