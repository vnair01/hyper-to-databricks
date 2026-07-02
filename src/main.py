
import argparse
import yaml
from extractor import extract_hyper
from transformer import transform_data
from loader import load_to_databricks


def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def main(config_path):
    config = load_config(config_path)

    hyper_path = extract_hyper(config["twbx_path"])
    df = transform_data(hyper_path)
    load_to_databricks(df, config["target_table"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    main(args.config)
