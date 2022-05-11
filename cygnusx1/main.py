from cygnusx1.bot import main
import os
import argparse

def run():
    parser = argparse.ArgumentParser(description='CygnusX1 Bot')
    parser.add_argument('--keywords', default="", type=str, required=True,
                        help='Indicate the keywords/keyphrases you want to search. For multiple keywords, separate '
                             'them with commas.')
    parser.add_argument('--out_dir', default='IMAGES', type=str,
                        help='Path where to save results.')
    parser.add_argument('--workers', default=2, type=int,
                        help='The maximum number of workers used to crawl image.')
    parser.add_argument("--use_suggestions", help="Use google suggestions.", action="store_true")
    parser.add_argument("--headless", help="Hide browser during scraping.", action="store_true")

    args = parser.parse_args()
    if not os.path.exists(args.out_dir):
        os.mkdir(args.out_dir)

    main(args)

if __name__ == "__main__":
    run()
