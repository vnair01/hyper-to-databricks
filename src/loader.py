def load_to_databricks(df, table_name):
    df.write.mode("overwrite").saveAsTable(table_name)
