import os

from ...exercises.functions2 import getListofRawFiles
from ...exercises.functions2_cleaned import find_raw_files

test_folder = os.path.join(os.path.dirname(__file__), '..', 'resources', 'raw')
expectation = ['4.raw', '1.raw', '2.raw', '3.raw']


def test_old_version():
    result = getListofRawFiles(test_folder)
    result = [os.path.basename(f) for f in result]
    assert_right_files_found(result)


def test_new_version():
    result = find_raw_files(test_folder)
    result = [os.path.basename(f) for f in result]
    assert_right_files_found(result)


def assert_right_files_found(result: list) -> None:
    assert len(result) == len(expectation)
    for entry in expectation:
        assert entry in result
