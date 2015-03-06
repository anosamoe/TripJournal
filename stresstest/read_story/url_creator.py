server = 'http://127.0.0.1:8000'
static_urls=['/',
      '/stories_near_by/', 
      '/pictures_near_by/', 
      '/my_stories/',
      '/edit/',]

story_prefix='/story/'

story_count = 200 #TODO: fetch the number of stories

def url_generator ():
	for link in static_urls:
		print server+link
		
	for id in xrange(1,story_count):
		print server+story_prefix+str(id)

if __name__ == '__main__':
	url_generator()