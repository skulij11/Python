import csv
from collections import Counter

def count_votes(path):
    with open(path, encoding='utf8') as f:
        reader = csv.DictReader(f)
        lis = []
        for row in reader:
            if row['Hvaða verkefni fannst þér skemmtilegust?'] == '':
                continue
            k = row['Hvaða verkefni fannst þér skemmtilegust?'].split(', ')
            for i in k:
                lis.append(i)
        return dict(Counter(lis))


print(count_votes('Kennslumat - Sheet1.csv'))
