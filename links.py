

import urllib.parse
import urllib.request
import re
from bs4 import BeautifulSoup

url = 'https://www.aeaweb.org'

def get_filename_from_page(arg_page):
  soup = BeautifulSoup(arg_page,'html.parser')
  alist = soup.find_all('h2')
  try:
    txt=(alist[0].string).split()
    output_string = 'JEP_'+'{:04d}'.format(int(txt[5]))+'_'
    output_string =output_string+'{:02d}'.format(int(txt[1]))+\
                  '_{:1d}'.format(int(txt[3]))
  except IndexError:
    output_string = 'no journal to dl'
  except AttributeError:
    output_string = 'splitFailed'
  return output_string
  
def read_url(arg_url):
  headers = {'User-Agent': 'cabrito'}
  req = urllib.request.Request(arg_url, None, headers)
  with urllib.request.urlopen(req) as response:
    the_page = response.read()
  return the_page

def get_path_to_files(arg_page):
  soup = BeautifulSoup(arg_page, 'html.parser')
  alist = soup.find_all('a', class_='button')
  linklist = []
  for link in alist:
    linklist.append(url+link.get('href'))
  return linklist

the_page = read_url(url+'/journals/jep/issues')
soup = BeautifulSoup(the_page,'html.parser')
alist=soup.find_all(href=re.compile('issues')) #list with all issues
for link in alist:
  download_page_link = str(url+link.get('href'))
  download_page      = read_url(download_page_link) #particular issue with path and filename
  print (get_filename_from_page(download_page),get_path_to_files(download_page))
print('done')
'''

the_page=read_url(url+'/issues/590')
alist=get_path_to_files(the_page)
print(alist)
'''


