# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 18:34:06 2022

@author: Justin Okorie
"""

import requests
import webbrowser
from bs4 import BeautifulSoup
import urllib3
import random

def dailydosescrapper():
    urllib3.disable_warnings()  
 
    def getdata(url):
        r = requests.get(url, verify=False)
        return r.text
 
    htmldata = getdata("https://www.youtube.com/c/DailyDoseOfInternet/videos")
    soup = BeautifulSoup(htmldata, 'html.parser')
   
    randomlist = str(soup.find_all()).split('/watch?v=')
    videolist = []
 
    for href in randomlist:
        videolist.append('https://www.youtube.com/watch?v=' +href[0:11])
 
    webbrowser.open(random.choice(videolist), new=1)
if __name__ == "__main__":
    dailydosescrapper()
 

