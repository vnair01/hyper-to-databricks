from pyspark.sql import SparkSession


def transform_data(hyper_path):
    spark = SparkSession.builder.getOrCreate()

    # Placeholder — customize based on your logic
    df = spark.read.format("parquet").load(hyper_path)

    return df
