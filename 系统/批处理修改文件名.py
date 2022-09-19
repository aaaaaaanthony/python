import os

count = 1

url = "/Users/anthony/PycharmProjects/学习python/"
for key in range(21):
    key = key+1
    print(key)
    os.rename(url + str(key), url + str(key) + ".mp4")
