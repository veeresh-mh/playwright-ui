import logging

def get_logger():
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("output.log")
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger