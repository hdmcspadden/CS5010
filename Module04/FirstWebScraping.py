# -*- coding: utf-8 -*-
"""
Actiity: Homework 3: Python and Web Scraper
Name: H. Diana McSpadden
UI: hdm5s
"""
# Import Libraries I will need
import requests # import requests library
from bs4 import BeautifulSoup # import BeautifulSoup library
import csv 
import datetime

# For intial run I used three news sites rates: Center (or not left or right leaning)
# Source: https://www.seafordlibrary.org/fakenews.html
        
#%%
# set the date and time the scraping occured
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#%%
filename = 'newsarticles.csv' # set the filename of the CSV to save article info to

#%%

def writeArticlesToCSV(art_list, filename):
    """ writeArticlesToCSV(art_list, filename): write contents of article list (site, headline, storyURL, scrapedate, cat) to csv file (filename)"""
   
    try:
        with open(filename, 'a', newline='') as f: 
            w = csv.DictWriter(f,['site','headline','storyURL','scrapedate','cat']) 
            for item in art_list: 
                w.writerow(item)
    except IOError as err:
        print("An IO Error has been raised: " + str(err))
    except PermissionError as err:
        print("The file may be open or I don't have rights to write to it: " + str(err))
    except Exception as err:
        print("A General Exception has been raised: " + str(err))
            
#%%
def retrieveLoopableSoupFind(url, parentTag, searchAttrs):
    """retrieveLoopableSoupFind(url, parentTag, searchAttrs): return a soup tag by beautifulSoup filter attribute"""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html5lib')
        return soup.find(parentTag, attrs = searchAttrs) 
    except Exception as err:
        print("A General Exception has been raised: " + str(err))

def retrieveLoopableSoupFindAll(url, parentTag, searchAttrs):
    """retrieveLoopableSoupAll(url, parentTag, searchAttrs): return an iterable collection of soup tags by beautifulSoup filter attribute"""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html5lib')
        return soup.findAll(parentTag, attrs = searchAttrs) 
    except Exception as err:
        print("A General Exception has been raised: " + str(err))   
    

#%%
# ABC NEWS
# retrieve the news stories abcnews.go.com identified as their TOP NEWS and store the site headline, URL, and scrape date time
try:
    articlesTable = retrieveLoopableSoupFind('https://abcnews.go.com/', 'article', {'id': 'trio-headline-view'})
    
    topArticles = []  # a list to store quotes 
    
    for art in articlesTable.findAll('li'):
        toparticle = {}
        toparticle['site'] = "abc"
        toparticle['headline'] = art.h1.a.contents[0]
        toparticle['storyURL'] = art.h1.a['href']
        toparticle['scrapedate'] = today
        toparticle['cat'] = "lightblue"
        topArticles.append(toparticle)
    
    writeArticlesToCSV(topArticles, filename)
except Exception as err:
        print("A General Exception during ABC News retrieval has been raised: " + str(err))

#%%

#NBC NEWS
# retrieve the news stories npr.org's news page identified as their TOP NEWS and store the site headline, URL, and scrape date time
try:
    articlesTable = retrieveLoopableSoupFindAll('https://www.npr.org/sections/news/', 'h2', {'class': 'title'})
    
    topArticles = []  # reinitialize list to store quotes  
    
    for artNPR in articlesTable:
        toparticle = {}
        toparticle['site'] = "npr"
        toparticle['headline'] = artNPR.a.contents[0]
        toparticle['storyURL'] = artNPR.a['href']
        toparticle['scrapedate'] = today
        toparticle['cat'] = "center"
        topArticles.append(toparticle)
    
    writeArticlesToCSV(topArticles, filename)
except Exception as err:
        print("A General Exception during NPR News retrieval has been raised: " + str(err))
        
#%%        
#CBS NEWS
# retrieve the news stories cbsnews.com identified as their TOP NEWS and store the site headline, URL, and scrape date time
try:
    articlesTable = retrieveLoopableSoupFindAll('https://www.cbsnews.com/', 'article', {'class': 'item'})
    
    topArticles = []  # reinitialize list to store quotes 
    
    for artCBS in articlesTable:
        toparticle = {}
        toparticle['site'] = "cbs"   
        toparticle['headline'] = artCBS.find('div', attrs = {'class': 'item__title-wrapper'}).find('h4', attrs = {'class': 'item__hed'}).contents                                    
        toparticle['storyURL'] = artCBS.a['href']
        toparticle['scrapedate'] = today
        toparticle['cat'] = "lightblue"
        topArticles.append(toparticle)
    
    writeArticlesToCSV(topArticles, filename)
except Exception as err:
        print("A General Exception during CBS News retrieval has been raised: " + str(err))

#%%
#AP NEWS
# retrieve the news stories apnews.com identified as their TOP NEWS and store the site headline, URL, and scrape date time
try:
    articlesTable = retrieveLoopableSoupFindAll('https://apnews.com/', 'a', {'data-key': 'related-story-link'})
    
    topArticles = []  # reinitialize list to store quotes 
    
    for artAP in articlesTable:
        toparticle = {}
        toparticle['site'] = "ap"   
        toparticle['headline'] = artAP.find('div', attrs = {'data-key': 'related-story-headline'}).contents                                    
        toparticle['storyURL'] = 'https://apnews.com/' + artAP['href']
        toparticle['scrapedate'] = today
        toparticle['cat'] = "center"
        topArticles.append(toparticle)
    
    writeArticlesToCSV(topArticles, filename)
except Exception as err:
        print("A General Exception during AP News retrieval has been raised: " + str(err))
#%%
#Fox News
try:
    mainTable = retrieveLoopableSoupFind('https://www.foxnews.com/', 'div', {'class': 'main main-secondary'})
    
    topArticles = []  # reinitialize list to store quotes 
    
    for artFox in mainTable.findAll('h2', attrs = {'class' : 'title'}):
        toparticle = {}
        toparticle['site'] = "fox"   
        toparticle['headline'] = artFox.a.contents                                    
        toparticle['storyURL'] = artFox.a['href']
        toparticle['scrapedate'] = today
        toparticle['cat'] = "lightred"
        topArticles.append(toparticle)
    
    writeArticlesToCSV(topArticles, filename)
except Exception as err:
        print("A General Exception during Fox News retrieval has been raised: " + str(err))
#%%
#Reason
try:
    mainTable = retrieveLoopableSoupFind('https://reason.com/', 'div', {'class': 'home-page-list-area--list col-md-8'})
    
    topArticles = []  # reinitialize list to store quotes 
    
    for artR in mainTable.findAll('h4'):
        toparticle = {}
        toparticle['site'] = "reason"   
        toparticle['headline'] = artR.a.contents                                    
        toparticle['storyURL'] = artR.a['href']
        toparticle['scrapedate'] = today
        toparticle['cat'] = "lightred"
        topArticles.append(toparticle)
    
    writeArticlesToCSV(topArticles, filename)
except Exception as err:
        print("A General Exception during Reason News retrieval has been raised: " + str(err))