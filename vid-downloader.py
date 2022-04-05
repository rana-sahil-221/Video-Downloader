from pytube import YouTube
from bs4 import BeautifulSoup
import requests
import sys,time

url = input("Enter or Paste the url of the video: ")

if len(url) > 1:
    yt = YouTube(url).streams.filter(file_extension="mp4",progressive=True).order_by('resolution').desc().first()
    #print(yt)
    print("Downloading video.............")
    print(time.sleep(12))
    des = input("Enter or Paste the Absolute path here: ")
    if len(des) > 1:
        yt.download(des)
        print("Downloading may be finished, check in your folder")
    else:
        sys.exit("Please enter the path")
else:
    sys.exit("Please enter a valid url")


