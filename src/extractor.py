import zipfile
import tempfile
import os


def extract_package(twbx_path):
    temp_dir = tempfile.mkdtemp()

    with zipfile.ZipFile(twbx_path, 'r') as z:
        files = z.namelist()

        hyper_file = [f for f in files if f.endswith(".hyper")][0]
        xml_file = [f for f in files if f.endswith((".twb", ".tds"))][0]

        z.extract(hyper_file, temp_dir)
        z.extract(xml_file, temp_dir)

        return (
            os.path.join(temp_dir, hyper_file),
            os.path.join(temp_dir, xml_file)
        )
