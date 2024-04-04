import logging
import os
import sys

# app_logger = logging.getLogger('app_logger')
app_logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler(f'{os.getcwd()}/app/logs/app_logger.log')
# fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
# app_logger.addHandler(fh)

sh = logging.StreamHandler(sys.stdout)
# sh.setLevel(logging.INFO)
sh.setFormatter(formatter)
# app_logger.addHandler(sh)

app_logger.handlers = [sh, fh]
