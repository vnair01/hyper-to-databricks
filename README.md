# Hyper to Databricks Loader

This project extracts data from Tableau `.tdsx/.twbx` files and loads it into a Databricks table using PySpark.

## Features

* Extract `.hyper` files from Tableau packages
* Parse metadata (captions, calculated fields)
* Convert data to Spark DataFrame
* Load into Databricks table

## Project Structure

* `src/` → Core logic
* `config/` → Configurations
* `tests/` → Test files

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python src/main.py --config config/config.yaml
```

## Configuration

Edit `config/config.yaml`:

```yaml
twbx_path: /path/to/file.tdsx
target_table: database.schema.table
```

## Future Improvements

* Add logging
* Add unit tests
* Add Airflow/Databricks job support
