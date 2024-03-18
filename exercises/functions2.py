import os


def getListofRawFiles(dir_path):
    """
    ## Original function that we have seen in the slides
    """
    dirs = [x[0] for x in os.walk(dir_path)]
    raw_files = []
    for mypath in dirs:
        all_raw_files = [fileName for fileName in os.listdir(mypath) if fileName.endswith(".raw")]
        for raw_file in all_raw_files:
            raw_files.append(os.path.join(mypath, raw_file))
    return raw_files
