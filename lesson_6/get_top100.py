import requests
import csv

good = []
with open('top500Domains.csv', 'rt') as f:
    rd = csv.reader(f)
    it = iter(rd)
    cntr = 0
    while cntr < 100:
        _, url, *trash = next(it)
        url = 'https://' + url
        print("try ", url)
        try:
            r = requests.get(url)
            if not r.ok:
                continue
        except:
            continue
        cntr += 1
        print(cntr)
        good.append(url)
print(good)
