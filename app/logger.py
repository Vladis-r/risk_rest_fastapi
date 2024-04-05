import logging
import os
import sys


os.makedirs(f'{os.getcwd()}/app/logs', exist_ok=True)

app_logger = logging.getLogger('app_logger')
logging.basicConfig(level=logging.INFO, )
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler(f'{os.getcwd()}/app/logs/app_logger.log')
fh.setFormatter(formatter)

sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(formatter)

app_logger.handlers = [sh, fh]
