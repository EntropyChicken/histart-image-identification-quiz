import os
import re


def numeric_key(path):
    filename = os.path.basename(path)
    match = re.search(r"ha(\d+)(?:\.(\d+))?", filename)
    main_num = int(match.group(1))
    sub_num = int(match.group(2)) if match.group(2) else 0
    return (main_num, sub_num)


def load_image_paths(image_range, image_dir=None):
    """Files in images/ whose ha-number falls in image_range, sorted by number."""
    if image_dir is None:
        image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

    paths = [
        entry.path.replace("\\", "/")
        for entry in os.scandir(image_dir)
        if entry.is_file() and numeric_key(entry.path)[0] in image_range
    ]
    paths.sort(key=numeric_key)
    return paths
