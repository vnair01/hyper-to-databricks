import argparse
import yaml

from extractor import extract_package
from metadata import parse_metadata
from hyper_reader import read_hyper
from transformer import transform
from loader import load_to_table


def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f)


def main(config_path):
    cfg = load_config(config_path)

    twbx_path = cfg["twbx_path"]
    target_table = cfg["target_table"]

    print("🔹 Extracting package...")
    hyper_path, xml_path = extract_package(twbx_path)

    print("🔹 Parsing metadata...")
    caption_map, calc_map = parse_metadata(xml_path)

    print("🔹 Reading Hyper file...")
    df = read_hyper(hyper_path)

    print("🔹 Transforming data...")
    df = transform(df, caption_map, calc_map)

    print("🔹 Loading to Databricks...")
    load_to_table(df, target_table)

    print("✅ Pipeline completed successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    main(args.config)
