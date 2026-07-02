def load_to_databricks(df, table_name):
    df.write.format("delta") \
        .mode("overwrite") \
        .option("overwriteSchema", "true") \
        .option("delta.columnMapping.mode", "name") \
        .option("delta.minReaderVersion", "2") \
        .option("delta.minWriterVersion", "5") \
        .saveAsTable(TARGET_TABLE)
