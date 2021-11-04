from typing import List, Tuple
from cygnusx1.helper import get_uuid, valid_image
from tqdm.contrib.concurrent import thread_map

import os
import shutil
import base64
import validators
import requests

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass

def _download_image_from_src(img_src: str, save_dir: str) -> bool:
    try:
        if img_src is None:
            return False
        if validators.url(img_src):
            r = requests.get(img_src, stream=True, timeout=10, verify=False)
            if r.ok:
                ext = r.headers['Content-Type'].split("/")[-1].strip()
                filename = os.path.join(save_dir, f'{get_uuid()}.{ext}')
                with open(filename, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
                    # f.write(r.content)
                valid_image(filename)
            else:
                return False
        else:
            src = img_src.split(";")
            ext = src[0].split("/")[-1].strip()
            base64_content = src[-1].split(",")[-1].strip()
            imgdata = base64.b64decode(base64_content)
            filename = os.path.join(save_dir, f'{get_uuid()}.{ext}')
            with open(filename, 'wb') as f:
                f.write(imgdata)
            valid_image(filename)
        return True
    except Exception as e:
        return False

def download_image(params: Tuple[List[str], str, str]) -> Tuple[str, int]:
    if len(params) != 3:
        return "Failed", 0
    sources, save_dir, keyword = params
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    success_count = 0
    for r in thread_map(_download_image_from_src, sources, [save_dir]*len(sources),
                        max_workers=12, position=0, leave=False):
        if r:
            success_count += 1
        else:
            continue
    return keyword, success_count

