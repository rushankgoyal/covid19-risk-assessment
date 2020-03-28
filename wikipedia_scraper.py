import numpy as np
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_tests(country):
  html = urlopen("https://en.wikipedia.org/wiki/COVID-19_testing")
  content = BeautifulSoup(html, 'html.parser')

  table = content.find_all('table')
  table = table[1]
  rows = table.find_all('tr')
  rows = rows[1:(len(rows)-1)]

  list_tests = ''
  country_list = []

  for row in rows:
    cells = row.find_all('th')
    for cell in cells:
      country_list.append(cell.text.rstrip().lstrip())
  country_list[country_list.index('United States (unofficial tracking)')] = 'United States'

  for row in rows:
    cells = row.find_all('td')
    list_tests += str(cells[0])
  list_tests = list_tests.replace('<td>','').replace('</td>','').replace(',','').replace('\n',' ').split(' ')
  
  return (list_tests[country_list.index('United States')] if 'United States' in country_list else 0)
