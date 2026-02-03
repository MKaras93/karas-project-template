import logging
from settings import settings

settings.configure_logging()
logger = logging.getLogger(__name__)

# REPLACE CODE BELOW WITH YOUR APPLICATION LOGIC


def sum_numbers(a, b):
    return a + b


logger.info(f"Current settings type: {settings.settings_type}")
logger.info(f"Sum of 3 and 5 is {sum_numbers(3, 5)}")
