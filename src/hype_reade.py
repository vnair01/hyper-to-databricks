from tableauhyperapi import HyperProcess, Connection, Telemetry, TableName
from pyspark.sql import SparkSession


def read_hyper(hyper_path):
    spark = SparkSession.builder.getOrCreate()

    rows = []
    columns = []

    with HyperProcess(Telemetry.DO_NOT_SEND_USAGE_DATA_TO_TABLEAU) as hyper:
        with Connection(endpoint=hyper.endpoint, database=hyper_path) as conn:
            catalog = conn.catalog

            schemas = catalog.get_schema_names()
            table = None

            for schema in schemas:
                tables = catalog.get_table_names(schema)
                if tables:
                    table = tables[0]
                    break

            if table is None:
                raise Exception("No table found in Hyper file")

            columns = [c.name for c in catalog.get_table_definition(table).columns]

            with conn.execute_query(f"SELECT * FROM {table}") as result:
                for row in result:
                    rows.append(tuple(row))

    return spark.createDataFrame(rows, columns)
