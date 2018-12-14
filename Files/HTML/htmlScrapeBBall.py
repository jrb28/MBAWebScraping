# -*- coding: utf-8 -*-
"""
Created on Thu May 26 21:29:00 2016

@author: james.bradley
"""
"""
Based on this web site: http://stackoverflow.com/questions/11709079/parsing-html-using-python
"""

from bs4 import BeautifulSoup  # Parsing HTML
import requests  # Internet information requests
import re        # Regular Expressions (Regex) package

htmlPath = 'https://www.basketball-reference.com/players/w/walljo01/gamelog-advanced/2017/'
htmlDoc = requests.get(htmlPath).content

""" parse html """
htmlParsed = BeautifulSoup(htmlDoc, 'lxml')
""" get data from one game: object games will be of the ResultType data type """
games = htmlParsed.find_all('tr', attrs={'id' : 'pgl_advanced.424'})  # Finds one row of data
""" The next statement uses Regex to find all rows of data """
#games = htmlParsed.find_all('tr', attrs={'id' : re.compile('^pgl_advanced.')})  

print('Number of games found:',len(games))
print('Game stats are in data type:',type(games),'\n')
all_games = []  # set up an empty list in which to store the data 
for game in games:
    new_game = []   #create empty list to store the data from the next game
    for field in game.find_all('td'):
        new_game.append(field.text)   # append next data point to the current game list
        
    all_games.append(new_game)        # append current game data list to overall list
    
print('\nHere\'s the Data')
print(all_games)