# Title: Sugamama(Bot)
# Custon Bot for the HAIKYUU in COLOR!! discord server.
# Author: TDXPQ (Aditya Jindal)
# This file contains additional non-discord functions for the Sugamama(Bot)

# Import python libraries.
import random
from pathlib import Path

# Import third party libraries.

# Define functions:
def get_picture_path():      #Function gets random picture from the HAIKYUU in COLOR!! local version of the Google Drive.
    pictures = []

    # Code adapted from leoburgy https://stackoverflow.com/questions/47655205/pathlib-path-glob-and-multiple-file-extension.
    # Code meant to recursivly search a designated folder for files that end with certain extensions.
    BASE_DIR = Path("../Completed page image pool")
    EXTENSIONS = {'.png', '.jpg', '.jpeg'}

    for path in BASE_DIR.glob(r'**/*'):
        if path.suffix in EXTENSIONS:
            pictures.append(path)
    #=====================================================================================================================

    return(pictures[random.randint(0, len(pictures))])


if __name__ == '__main__':
    path = str(get_picture_path())

    for i in range(0, len(path)):
        if path[i] == '\\':
            last_slash = i

    print(path)
    print(path[(last_slash+1):])