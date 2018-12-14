# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 12:16:21 2018

@author: jrbrad
"""

from bs4 import BeautifulSoup

htmlPath = './CourseSchedule.htm'
f = open(htmlPath)
htmlDoc = f.read()
f.close()

# parse html 
htmlParsed = BeautifulSoup(htmlDoc,"lxml")

results1 = htmlParsed.find_all('table', attrs={'class' : 'Course'})
#print(results1)

for result1 in results1:
    results2a = result1.find('tr', attrs = {'class' : 'Name'})
    courseName = results2a.text
    results2b = result1.find_all('tr', attrs = {'class' : 'Session'})
    for result2 in results2b:
        results3a = result2.find_all('td', attrs = {'class' : 'Num'})
        results3b = result2.find_all('td', attrs = {'class' : 'Time'})
        results3c = result2.find_all('td', attrs = {'class' : 'Days'})
        
        for i in range(len(results3a)):
            print(courseName,': ', results3a[i].text, results3b[i].text, results3c[i].text)