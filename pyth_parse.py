import json
import numpy as np
import matplotlib.pyplot as plt
from dateutil.parser import parse as dateParse


data = json.load(open('rates.json', 'r'))

headers = []

for d in data:
    if d["currency"] in headers:
        pass
    else:
        headers.append(d["currency"])

arranged_data = {} 
l_h = []
plt.figure()

for header in headers:
    arranged_data[header] = list(filter(lambda d: d["currency"] == header, data))
    dates = []
    rates = []
    for d in arranged_data[header]:
        try:
            rates.append(float(d["rate"]))
            dates.append(dateParse(d["date"]))
        except:
            pass 
    print(len(dates) == len(rates))
    h, = plt.plot(dates, rates, label=header) 
    l_h.append(h)

with open('rates_rearranged.json', 'w') as outfile:
    json.dump(arranged_data, outfile)

plt.legend(handles=l_h)
plt.show()
