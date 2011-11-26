import sys
import itertools
from datetime import date

def year_convert(y):
    if y < 1000:
        year = 2000 + y
    else:
        year = y
    return year
    
def sanitize(unformated_date):
    date_list = unformated_date.split('/')
    date_list = [x.strip() for x in date_list]
    date_list = map(int, date_list)
    return date_list
    
def date_to_output(unformated_date):
    date_list = sanitize(unformated_date)
    sorted_date_list = sorted(date_list)
    if len(sorted_date_list) == 3:
        for a in itertools.permutations(sorted_date_list, 3):
    	    b = list(a)
    	    b[0] = year_convert(b[0])
    	    try:
    	        dt = date(b[0], b[1], b[2])
    	    except ValueError:
    	        continue
    	    return str(dt)
    return unformated_date.strip() + " is illegal"
    
if __name__ == '__main__':
    for unformated_date in sys.stdin:
        print date_to_output(unformated_date)