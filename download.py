from ast import keyword
from cgitb import text
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os
import time
import sys

key = "cf68902e98ed9d2343e01e9b3b39c370"
secret = "0b5b29e55c70c3b7"
wait_time = 1

keyword = sys.argv[1]
savedir = "./" + keyword

flickr = FlickrAPI(key, secret, format="parsed-json")
result = flickr.photos.search(
    text=keyword,
    per_page=400,
    media="photos",
    sort="relevance",
    safe_serch=1,
    extras="url_q, license",
)

photos = result["photos"]


for i, photo in enumerate(photos["photo"]):
    url_q = photo["url_q"]
    filepath = savedir + "/" + photo["id"] + ".jpg"
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
