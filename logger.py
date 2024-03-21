import logging

app_logger = logging.getLogger('app_logger')
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
