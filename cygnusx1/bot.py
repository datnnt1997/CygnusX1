from cygnusx1.scraper import scrap_google_images
from cygnusx1.downloader import download_image
from cygnusx1.helper import LOGGER, write_json
from tqdm.contrib.concurrent import thread_map
from tqdm import tqdm

import os
import time

def main(args) -> bool:
    keywords = [k.strip() for k in args.keywords.split(",")]
    if len(keywords) == 0:
        return True
    maps = []
    stats = {}
    LOGGER.info(f"\n{'=' * 20}ARGUMENTS{'=' * 20}")
    LOGGER.info(f"Keywords: {keywords}")
    LOGGER.info(f"Workers: {args.workers}")
    LOGGER.info(f"Headless: {args.headless}")
    LOGGER.info(f"Use suggestions: {args.use_suggestions}")
    LOGGER.info(f"Saved Dir: {args.out_dir}")
    LOGGER.info(f"\n{'=' * 23}MAIN{'=' * 22}")
    LOGGER.info("Image scraping ...")

    with tqdm(keywords, desc="Scraping keywords", colour='green') as scrap_bar:
        cached_file = f"./cached_file_{time.strftime('%H%M%S-%Y%m%d')}.json"
        for kw in scrap_bar:
            scrap_bar.set_description(f"Keywords Scraping '{kw}'")
            img_srcs, num_search_results = scrap_google_images(args, kw)
            save_dir = os.path.join(args.out_dir, kw.strip().replace(" ", "_"))
            maps.append([img_srcs, save_dir, kw])
            stats[kw] = {"num_search": num_search_results, "num_scraping": len(img_srcs), "links": img_srcs}
            write_json(cached_file, stats)
    LOGGER.info("Image downloading ...")
    for kw, count in thread_map(download_image, maps,
                                max_workers=args.workers, desc="Keywords Downloading", colour='green'):
        stats[kw]["num_downloaded"] = count
    LOGGER.info(f"\n{'='*21}SUMMARY{'='*21}")
    LOGGER.info(f"Image crawl successfull. Check results at '{args.out_dir}'")
    for k, v in stats.items():
        LOGGER.info(f"Keywords: '{k}'; "
                    f"Searched: {v['num_search']}; "
                    f"Scraped: {v['num_scraping']}; "
                    f"Downloaned: {v['num_downloaded']};")



