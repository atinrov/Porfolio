# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 17:05:11 2022
@author: agustin
"""

#Import packages and libraries
import requests
from bs4 import BeautifulSoup #For web scraping
import pandas as pd

#variables
URL="https://www.lidl.es/es/no-te-compliques-bio-en-lidl/c3803"

#constants
products=[] #List to store name of the product
prices=[] #List to store price of the product
df=pd.DataFrame()

#### #main code ####

#Get results as iterable element
page   =  requests.get(URL)
parser = BeautifulSoup(page.content,"html.parser")
JobIter = parser.find_all("div", class_="c-4 product product-grid-box-tile__left")
#print(JobIter[0].find("a", class_="go-to-pdp")["href"])
print(JobIter[0].find("span", class_="price-height"))

#for iter in JobIter:
#    iter.find("a", class_="go-to-pdp")["href"]
    