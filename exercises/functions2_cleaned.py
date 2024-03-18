import os
import glob


def find_raw_files(directory: str) -> list:
    return glob.glob(os.path.join(directory, '**', '*.raw'),  recursive=True)
