import glob
import os
import requests


# url = "https://europe.olemovienews.com/hls2timeofffmp4/20220918/cihJvCAq/mp4/cihJvCAq.mp4/index-v1-a1.m3u8"
# response = requests.get(url)
# with open("1.m3u8", "wb") as file:
#     file.write(response.content)
#     file.flush()
# "https://europe.olemovienews.com/hls2timeofffmp4/20220918/cihJvCAq/mp4/cihJvCAq.mp4/seg-1-v1-a1.m4s"

# 1-241

def down_first():
    for index in range(1, 3):
        url = "https://europe.olemovienews.com/hls2timeofffmp4/20220918/cihJvCAq/mp4/cihJvCAq.mp4/init-v1-a1.mp4"
        response = requests.get(url)
        with open("init-v1-a1.mp4", "wb") as file:
            file.write(response.content)
            file.flush()
        print(index)

def down():
    for index in range(1, 3):
        url = "https://europe.olemovienews.com/hls2timeofffmp4/20220918/cihJvCAq/mp4/cihJvCAq.mp4/"
        url2 = url + "seg-" + str(index) + "-v1-a1.m4s"
        response = requests.get(url2)
        with open("seg-" + str(index) + "-v1-a1.m4s", "wb") as file:
            file.write(response.content)
            file.flush()
        print(index)


def merge_to_mp4(dest_file, source_path, delete=False):
    with open(dest_file, 'wb') as fw:
        files = glob.glob(source_path + '/*.m4s')
        for file in files:
            with open(file, 'rb') as fr:
                fw.write(fr.read())
                print(f'\r{file} Merged! Total:{len(files)}', end="     ")
            if delete:
                os.remove(file)


down_first()
down()

# merge_to_mp4("test.mp4", "/Users/anthony/PycharmProjects/学习python/下载")

# merge()
