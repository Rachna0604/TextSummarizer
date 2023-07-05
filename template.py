import os
#from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/{}/__init__.py".format(project_name),
    "src/{}/components/__init__.py".format(project_name),
    "src/{}/utils/__init__.py".format(project_name),
    "src/{}/utils/common.py".format(project_name),
    "src/{}/logging/__init__.py".format(project_name),
    "src/{}/config/__init__.py".format(project_name),
    "src/{}/config/configuration.py".format(project_name),
    "src/{}/pipeline/__init__.py".format(project_name),
    "src/{}/entity/__init__.py".format(project_name),
    "src/{}/constants/__init__.py".format(project_name),
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py",

]

'''
for filepath in list_of_files:
    filepath = os.path.join(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Created directory: {} for the file {}".format(filedir, filename))


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info("creating empty file: {}".format(filepath))



    else:
        
        logging.info("is already exists: {}".format(filename))
'''

import os
import errno

for filepath in list_of_files:
    filepath = os.path.join(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        try:
            os.makedirs(filedir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        logging.info("Created directory: {} for the file {}".format(filedir, filename))

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info("Creating empty file: {}".format(filepath))
    else:
        logging.info("{} already exists".format(filename))

