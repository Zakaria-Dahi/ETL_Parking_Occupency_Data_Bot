import requests
import time
import urllib
import json
from datetime import datetime


#-----------------------------------------------------------------------------
# Data source:
# https://www.gti.ssr.upm.es/data/parking-lot-database
# http://cnrpark.it/
# https://www.kaggle.com/datasets/mypapit/klccparking?resource=download
# https://datosabiertos.malaga.eu/dataset/ocupacion-aparcamientos-publicos-municipales/resource/0dcf7abd-26b4-42c8-af19-4992f1ee60c6
#https://datosabiertos.malaga.eu/dataset/ocupacion-aparcamientos-publicos-municipales
#-----------------------------------------------------------------------------

import os

# Initialising Git
os.system("git init")
os.system("git remote set-url origin git@github.com:Zakaria-Dahi/ETL_Parking_Occupency_Data_Bot.git")

for l in range(12): # recover the data during the 12 months of the year
    for k in range(4): # recover the 4 weeks of the month
        for j in range (7): # recover the data during 7 days
            for i in range(1): # recover data during 24 hours every 1/4 hour. Start 22-10-2022
                url = 'https://datosabiertos.malaga.eu/recursos/aparcamientos/ocupappublicosmun/ocupappublicosmun.csv'
                r = requests.get(url,allow_redirects=True)
                name = "results/"+str(datetime.now()) +'.csv';
                open(name,'wb').write(r.content)
                time.sleep(10)
            # Uploading the results to Github
            os.system("git add .")
            commit_name = "git commit -m \"Commit done on:" + str(datetime.now()) + "\""
            print(commit_name)
            os.system(commit_name)
            os.system("git push origin main")


# This is just an alternative method for scrapping using the open API.
"""
for i in range(1):
    url = 'https://datosabiertos.malaga.eu/api/3/action/datastore_search?resource_id=0dcf7abd-26b4-42c8-af19-4992f1ee60c6&limit=100'
    fileobj = urllib.request.urlopen(url)
    json_object = json.dumps(fileobj.read().decode())
    name = 'data('+ str(i) +').json';
    with open(name,"w") as outfile:
        outfile.write(json_object)
"""

