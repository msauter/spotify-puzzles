import sys
import itertools
from datetime import date


def padYear(year):
    if year < 2000:
        year += 2000
    return str(year)

def padMD(md):
    if md < 10:
        return '0'+str(md)
    return str(md)

# returns int list of [y,m,d]
def bestDate(input):
    partsStr = input.split('/')
    pts= sorted(map(int, partsStr))
    if not isUnsigned(pts):
        return input
        
    for a in itertools.permutations(pts, 3):
            b = list(a)
            if dateCheck(b):
                return b
                
    return input

def isUnsigned(arr):
    if arr[0] < 0 or arr[1] < 0 or arr[2] < 0:
        return False
    return True

def sanitizeDate(arr):
    arr[0] = arr[0] + 2000 if arr[0] < 1000 else arr[0]

def dateCheck(arr):
    sanitizeDate(arr)
    try:
        date(arr[0], arr[1], arr[2])
    except ValueError:
        return False
    return True


def formatDate(arr):
    if isinstance(arr, str):
        return arr+' is illegal'
    return '-'.join([padYear(arr[0]), padMD(arr[1]), padMD(arr[2])])


if __name__ == '__main__':
    for line in sys.stdin:
        print formatDate(bestDate(line.strip()))
