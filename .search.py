import sys
import os
n = len(sys.argv)
search_term = ''
command = 'google-chrome '
for i in range (1,n):
	if(i<n-1):
		search_term = search_term + sys.argv[i] + "%20"
	else:
		search_term = search_term + sys.argv[i]
url = "https://www.google.com.tr/search?q={}".format(search_term)   
command = command + url
os.system(command + ' >/dev/null 2>/dev/null 3>/dev/null &')
