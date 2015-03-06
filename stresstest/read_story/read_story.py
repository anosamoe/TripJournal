# coding: utf-8

import sys
import time
from ghost import Ghost
#from url_creator import url_generator

sys.stdout=open('myifle.txt', 'a')

ghost = Ghost()

urls=['http://127.0.0.1:8000/', 
      'http://127.0.0.1:8000/stories_near_by/', 
      'http://127.0.0.1:8000/pictures_near_by/', 
      'http://127.0.0.1:8000/my_stories/',
      'http://127.0.0.1:8000/edit/',
      'http://127.0.0.1:8000/story/5',
      'http://127.0.0.1:8000/story/6',]


def run_test():
    alltime = 0
    start = time.clock()
    print '-' * 50
    for url in urls:
        page, resources = ghost.open(url)
        print 'status:', page.http_status
        elapsed = time.clock() - start
        print url, ' => ', elapsed
        print ''

run_test()