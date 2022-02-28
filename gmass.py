

import requests
import random
import csv
import concurrent.futures
import time
from urllib.parse import urlencode
#opens a csv file of proxies and prints out the ones that work with the url in the extract function

emailist = []

with open('list.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        emailist.append(row[0])

def extract(emails):
    
    emailis = random.choice(emailist)
    #this was for when we took a list into the function, without conc futures.
    payload = {'email': emailis, 'key': '4bbd1f27-626e-4451-9b36-1437f97d8812'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    
    try:
        #change the url to https://httpbin.org/ip that doesnt block anything
        r = requests.post('https://verify.gmass.co/verify?', headers=headers, data=payload, timeout=(5, 15))
        v = (r.json()['Status'])
        vc = (r.json()['Email'], ' | ', r.json()['Status'])
        print(r.json()['Email'], ' | ', v)
        if 'Valid' in v:
            tx = open('valid.txt', 'a+')
            tx.write('\n')
            tx.writelines(vc)
            tx.close()
            time.sleep(20)
    except:
        pass
    return emails

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, emailist)
