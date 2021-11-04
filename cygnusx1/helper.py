from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import hashlib
import time
import uuid
import os
import json
import imghdr
import shutil
import logging
import random as rand

logging.getLogger("WDM").setLevel(logging.ERROR)

def init_logger(log_file=None, log_file_level=logging.NOTSET):
    log_format = logging.Formatter("%(message)s")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.handlers = [console_handler]

    if log_file and log_file != '':
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_file_level)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
    return logger

def get_browser(headless=False) -> webdriver:
    options = webdriver.ChromeOptions()
    options.headless = headless
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    return driver

def highlight(browser: webdriver, element):
    browser.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                           "background: yellow; border: 4px solid red; opacity: 0.5")

def get_md5() -> str:
    return hashlib.md5(str(time.time() + rand.randint(0, 10000)).encode('utf-8')).hexdigest()

def get_uuid() -> str:
    return str(uuid.uuid4().hex)

def valid_image(file_path: str) -> None:
    raw_name, ext = os.path.splitext(file_path)
    img_type = imghdr.what(file_path)
    if f".{img_type}" != ext:
        new_file_path = f"{raw_name}.{img_type}"
        shutil.move(file_path, new_file_path)

def write_json(file_path: str, data: dict):
    with open(file_path, 'w') as fw:
        json.dump(data, fw)


LOGGER = init_logger()
