from typing import List, Tuple
from tqdm import tqdm
from tqdm.contrib.concurrent import thread_map
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from cygnusx1.config import (GOOGLE_SUGGEST_CLASS, GOOGLE_THUBNAILS_XPATH,
                             GOOGLE_IMAGE_FULLSIZE_XPATH, GOOGLE_IMAGE_LOADING_BAR_XPATH)
from cygnusx1.helper import get_browser, highlight, LOGGER

import time


def _get_google_suggests(root_url: str, headless: bool = False) -> List[str]:
    urls = set()
    try:
        browser = get_browser(headless)
        browser.get(root_url)
        suggestions = browser.find_elements_by_class_name(GOOGLE_SUGGEST_CLASS)
        urls.update([s.get_attribute("href") for idx, s in enumerate(suggestions)
                     if s.get_attribute("href") is not None])
        browser.quit()
    except Exception as e:
        # LOGGER.info(f"Failed to get google suggest.")
        pass
    return list(urls)

def _scrap_google_page_image_urls(page_url: str, thread_id: int, headless: bool = False) -> Tuple[List[str], int]:
    thread_name = f"BROWSER_{thread_id}"
    image_srcs = set()
    browser = get_browser(headless)
    wait = WebDriverWait(browser, 10)
    num_of_search_results = 0
    try:
        browser.get(page_url)
        time.sleep(1)
        last_height = browser.execute_script("return document.body.scrollHeight")
        reached_page_end = False
        while not reached_page_end:
            browser.execute_script(f"window.scrollTo(0, {last_height});")
            time.sleep(1)
            new_height = browser.execute_script("return document.body.scrollHeight")
            if last_height == new_height:
                reached_page_end = True
            else:
                last_height = new_height
            try:
                browser.find_element_by_class_name("mye4qd").click()
            except:
                continue
        thubnails = browser.find_elements(By.XPATH, GOOGLE_THUBNAILS_XPATH)
        num_of_search_results += len(thubnails)
        for thubnail in tqdm(thubnails, leave=False, desc=f"{thread_name}"):
            try:
                highlight(browser, thubnail)
                thubnail.click()
                loading_bar = browser.find_element(By.XPATH, GOOGLE_IMAGE_LOADING_BAR_XPATH)
                # wait.until(WaitLoad(loading_bar))
                if "display" in (str(loading_bar.get_attribute('style'))):
                    wait.until(lambda _: 'display: none' in str(loading_bar.get_attribute('style')))
                imgs = browser.find_elements(By.XPATH, GOOGLE_IMAGE_FULLSIZE_XPATH)
                for img in imgs:
                    highlight(browser, img)
                    src = img.get_attribute('src')
                    image_srcs.add(src)
            except Exception as e:
                 # LOGGER.info(f"Failed to get google image.")
                 continue
    except Exception as e:
        # LOGGER.info(f"Failed to get google page image.")
        pass
    finally:
        browser.quit()
    return list(image_srcs), num_of_search_results

def scrap_google_images(args, keywork: str) -> Tuple[List[str], int]:
    img_srcs = set()
    root_url = "https://www.google.com/search?q=" + keywork.strip() + "&source=lnms&tbm=isch&safe=off"
    page_urls = [root_url]
    num_results = 0
    if args.use_suggestions:
        page_urls.extend(_get_google_suggests(root_url, args.headless))
    for links, num_search_results in thread_map(_scrap_google_page_image_urls,
                                                page_urls,
                                                range(len(page_urls)),
                                                [args.headless]*len(page_urls),
                                                max_workers=args.workers, desc="Page Image Scraping",
                                                leave=False, colour='blue'):
        img_srcs.update(links)
        num_results += num_search_results
    return list(img_srcs), num_results
