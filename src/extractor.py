import zipfile
import tempfile
import os


def extract_hyper(twbx_path):
    temp_dir = tempfile.mkdtemp()

    with zipfile.ZipFile(twbx_path, 'r') as z:
        hyper_files = [f for f in z.namelist() if f.endswith('.hyper')]

        if not hyper_files:
            raise Exception("No .hyper file found")

        hyper_file = hyper_files[0]
        z.extract(hyper_file, temp_dir)

        return os.path.join(temp_dir, hyper_file)
