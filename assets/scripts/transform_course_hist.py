# 1. Use beutifulsoup to 
# 2. Confirm loaded correctly
# 3. define def to find the table
# what does it return the table as? 

import pandas as pd
from bs4 as BeautifulSoup as bs

def getTables(htmlDoc):
	with open(htmlDoc) as fp:
		soup = bs(fp)
	return soup.findAll('table')
	
course_hist = getTables('course_history.html')

print(course_hist)

	