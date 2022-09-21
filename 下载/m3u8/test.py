import glob
import os

import requests

header = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "vod.gaodun.com",
    "Origin": "https://open.gaodun.com",
    "Referer": "https://open.gaodun.com/",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


def setup():
    url = "https://vod.gaodun.com/13p9Wv580v1a!!fs/SD/1.m3u8"
    response = requests.get(url, headers=header)
    with open("1.m3u8", "wb") as file:
        file.write(response.content)
        file.flush()


def down():
    for index in range(42, 45):

        url = "https://video1-cdn.gaodun.com/pub/13p9Wv580v1a!!fs/SD/"+str(index)+".ts"

        response = requests.get(url)
        with open(str(index) + ".ts", "wb") as file:
            file.write(response.content)
            file.flush()
        print(index)


def merge_to_mp4(dest_file, source_path, delete=False):
    with open(dest_file, 'wb') as fw:
        files = glob.glob(source_path + '/*.ts')
        for file in files:
            with open(file, 'rb') as fr:
                fw.write(fr.read())
                print(f'\r{file} Merged! Total:{len(files)}', end="     ")
            if delete:
                os.remove(file)




# setup()
# down()
merge_to_mp4("test.mp4","/Users/anthony/PycharmProjects/学习python/下载/m3u8")
