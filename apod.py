#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import httplib2
import time
from BeautifulSoup import BeautifulSoup, SoupStrainer

def search_link(link_da_scansionare):#searches for link
    http = httplib2.Http()
    try:
        status, response = http.request(link_da_scansionare)
        print ("Parsing links...")
        for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
            if link.has_key('href'):
                link_a_immagine = 'https://apod.nasa.gov/apod/'+ (link['href'])
                searchFor_pics(link_a_immagine)
    except:
            print("Connection reset by peer in search_link")

        #if link.has_key('href'):

def searchFor_pics(link_da_scansionare): #downloads the pic if he finds it
    http = httplib2.Http()
    try:
        status, response = http.request(link_da_scansionare)
        for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
            if link.has_key('href'):
                link_file=link['href']
                estensione=link_file[-3:]
                if (estensione=='jpg') or (estensione=='gif'):
                    link_file='https://apod.nasa.gov/apod/' + link['href']
                    print("Downloading: " + link_file)
                    download_link(link_file)
                    print("")
    except:
        print("Connection reset by peer in searchFor_pics")
    #status, response = http.request('https://apod.nasa.gov/apod/ap170511.html')


def process_filename(link_da_processare):
    nome_file=link_da_processare[38:]
    data_file=link_da_processare[33:37]
    filename=data_file+'_'+nome_file
    return filename


def download_link(link_to_download):
    testfile = urllib.URLopener()
    try:
        testfile.retrieve(link_to_download, process_filename(link_to_download))
    except:
        print("Cannot download from link. Skipping.")

##################################################
#####       MAIN                            ######
##################################################
search_link('https://apod.nasa.gov/apod/archivepix.html')

