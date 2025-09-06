import logging

from src.settings import LOGGING_LEVEL

LOG_LEVEL = {
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "DEBUG": logging.DEBUG,
    "ERROR": logging.ERROR,
}

console_handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_handler.setFormatter(formatter)

def get_logger(module_name: str) -> logging.Logger:
    lgr = logging.getLogger(module_name)
    lgr.setLevel(LOG_LEVEL[LOGGING_LEVEL])
    lgr.handlers.clear()
    lgr.addHandler(console_handler)
    return lgr
