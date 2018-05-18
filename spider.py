import re
import requests
import urllib
from google_images_download import google_images_download
import os
import time
import subprocess


def spiders(allpath):

    path = os.path.join(allpath, "additive").replace('\\','/')

    for root, _, files in os.walk(path):

        for each in files:

            imagepath = os.path.join(root, each).replace('\\','/')
            imagename = each
            print(imagepath)

            fnull = open(os.devnull, 'w')
            result0 = subprocess.call('ping www.baidu.com', shell=True, stdout=fnull, stderr=fnull)
            fnull.close()
            while result0:
                print('Waiting for Baidu.')
                time.sleep(60)
                fnull = open(os.devnull, 'w')
                result0 = subprocess.call('ping www.baidu.com', shell=True, stdout=fnull, stderr=fnull)
                fnull.close()

            url = 'https://sp1.baidu.com/70cHazva2gU2pMbgoY3K/n/image?fr=psindex&target=pcSearchImage&needJson=true&id=WU_FILE_0&name='+imagename+'&type=image/jpeg'
            fileopen = open(imagepath, 'rb')
            files = {
                'image': (imagename, fileopen, 'image/jpeg')
            }

            fnull = open(os.devnull, 'w')
            result0 = subprocess.call('ping www.baidu.com', shell=True, stdout=fnull, stderr=fnull)
            fnull.close()
            while result0:
                print('Waiting for Baidu.')
                time.sleep(60)
                fnull = open(os.devnull, 'w')
                result0 = subprocess.call('ping www.baidu.com', shell=True, stdout=fnull, stderr=fnull)
                fnull.close()

            r = requests.post(url, files=files)

            pattern = r'"imageUrl":"(.*?)"}'
            reurl = re.findall(pattern, r.text, re.S)

            reurl[0] = reurl[0].replace('\\', '')

            surl = urllib.parse.unquote(reurl[0])
            imageurl=surl.split('"')[0]

            fnull = open(os.devnull, 'w')
            result1 = subprocess.call('ping images.google.com', shell=True, stdout=fnull, stderr=fnull)
            fnull.close()
            while result1:
                print('Waiting for Google.')
                time.sleep(60)
                fnull = open(os.devnull, 'w')
                result1 = subprocess.call('ping images.google.com', shell=True, stdout=fnull, stderr=fnull)
                fnull.close()

            response = google_images_download.googleimagesdownload()
            arguments = {"similar_images":imageurl,"limit":100, "prefix":"add", "output_directory":"result_"+root.split('\\')[-1]}

            fnull = open(os.devnull, 'w')
            result1 = subprocess.call('ping images.google.com', shell=True, stdout=fnull, stderr=fnull)
            fnull.close()
            while result1:
                print('Waiting for Google.')
                time.sleep(60)
                fnull = open(os.devnull, 'w')
                result1 = subprocess.call('ping images.google.com', shell=True, stdout=fnull, stderr=fnull)
                fnull.close()

            response.download(arguments)
            fileopen.close()
            os.remove(imagepath)
            print("delete imgae:", imagepath)
            if not os.listdir(root):
                os.rmdir(root)
                print("delete empty dir:", root.replace('\\','/'))


if __name__ == '__main__':
    spiders(os.getcwd())