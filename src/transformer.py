from pyspark.sql.functions import col


def transform(df, caption_map, calc_map):

    # Rename columns
    for original, caption in caption_map.items():
        if original in df.columns:
            df = df.withColumnRenamed(original, caption)

    # Apply calculated fields (basic placeholder)
    for col_name, calc in calc_map.items():
        if col_name not in df.columns:
            df = df.withColumn(col_name, col(df.columns[0]))

    return df
