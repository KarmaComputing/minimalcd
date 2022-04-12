import sys
import os
import logging

PYTHON_LOG_LEVEL = os.getenv('PYTHON_LOG_LEVEL', logging.DEBUG)

logging.basicConfig(level=PYTHON_LOG_LEVEL)

def load():
    paths = [os.getenv('PYTHON_PATH_INJECT')]
    for p in paths:
        logging.info(f"Injecting python path {p}")
        sys.path.insert(0, p)

load()

from minimalcd import application
