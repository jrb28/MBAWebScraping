# -*- coding: utf-8 -*-
"""
Created on Thu May 26 21:29:00 2016

@author: james.bradley
"""

from bs4 import BeautifulSoup

htmlPath = './CourseSchedule.htm'
f = open(htmlPath)
htmlDoc = f.read()
f.close()

# parse html 
htmlParsed = BeautifulSoup(htmlDoc,"lxml")

results = htmlParsed.find_all('td', attrs={'class' : 'Num'})
print(results)
print('Type of results: ', type(results))
print('results: ', len(results))
print('      Full Tag                      Tag Width   Class')
for result in results:
    print(result, ',', result.text, ',', result['width'], ',', result['class'])