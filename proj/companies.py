import json
from urllib.request import urlopen
from urllib.parse import urlencode
from datetime import datetime


def companies(d,m,y):

    d = str(40 + d)
    print(d)
    if m < 10:
        m = '0' + str(m)
    y = str(y)[2:]
    
    ssn = str(d)+str(m)+y
    
    print('SSN: ', ssn)
    data = {'socialnumber': ssn}
    f = urlopen('http://apis.is/company?%s' % urlencode(data))
    data = json.loads(f.read().decode('utf8'))

    return [comp['name'] for comp in data['results'] if comp['active'] == 1]

print(companies(2, 12, 1986))
print(companies(7, 1, 2008))
print(companies(21, 5, 2014))
    
