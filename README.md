<h1 align="center">🕳️CygnusX1</h1>

Code by **Trong-Dat Ngo**.

## Overviews

🕳️CygnusX1 is a multithreaded tool 🛠️, used to search and download images from popular search engines 🔎. It is straightforward to set up and run! 

## Key features

-  🥰 No knowledge is required to get up and to run.
- 🚀 Download image using customizable number of threads.
- ⛏️Crawl all possible images (search results and recommendations).

## Installation

This repository is tested on Python 3.6+ and PyTorch selenium 3.141.0+, as well as it works fine on macOS, Windows, Linux.

You should setup and run 🕳️CygnusX1 in a [virtual environment](https://docs.python.org/3/library/venv.html). If you're 
unfamiliar with Python virtual environments, check out the user guide [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

First, create a virtual environment with the version of Python you're going to use and activate it. (Can be omitted if you want to set up directly on the OS environment) 
```sh
source venv/bin/activate
```
### Pip Insstallation
Install 🕳️CygnusX1 by pip:
```sh
pip install CygnusX1
```

### Manual Installation
Download 🕳️CygnusX1 from Github:
```sh
git clone https://github.com/dat821168/CygnusX1.git
```
Finally install dependencies in `requirements.txt`:
```sh
pip install -r requirements.txt
```

## Run
Use cygnusx1 command line:
```bash
cygnusx1  --keywords "keyword 1, keyword 2" --workers 8 --use_suggestions --headless
```

Use `run.py` to start the script:
```bash
python run.py  --keywords "keyword 1, keyword 2" --workers 8 --use_suggestions --headless
```

Argument details:

- `--keywords`: Indicate the keywords/keyphrases you want to search. For multiple keywords, separate them with commas.
- `--out_dir`: Path where to save results. Default = './IMAGES'.
- `--workers`: The maximum number of workers used to crawl image. Default = 2.
- `--use_suggestions`: Crawl search engine suggestions/recommendations. Default = False.
- `--headless`: Hide browser during scraping. Default = False.

### Future Releases

- [x] <strike>Suppor [Google search engine</strike>](https://www.google.com/).
- [ ] Support [Bing search engine](https://www.bing.com/).
- [ ] Support [Baidu search engine](https://www.baidu.com/).


## References
- [<b>Google Images Download</b>](https://github.com/hardikvasa/google-images-download.git)
- [<b>Image Downloader</b>](https://github.com/sczhengyabin/Image-Downloader.git)
