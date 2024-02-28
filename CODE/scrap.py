import requests
import time
import urllib
import json
from datetime import datetime


#-----------------------------------------------------------------------------
# Start of scrapping: Start 22-10-2022
# Data source:
# https://www.gti.ssr.upm.es/data/parking-lot-database
# http://cnrpark.it/
# https://www.kaggle.com/datasets/mypapit/klccparking?resource=download
# https://datosabiertos.malaga.eu/dataset/ocupacion-aparcamientos-publicos-municipales/resource/0dcf7abd-26b4-42c8-af19-4992f1ee60c6
#https://datosabiertos.malaga.eu/dataset/ocupacion-aparcamientos-publicos-municipales
#-----------------------------------------------------------------------------

import os

# Initialising Git
os.system("git -C ../ init")
os.system("git -C ../ remote set-url origin git@park.github.com:Zakaria-Dahi/ETL_Parking_Occupency_Data_Bot.git")


for m in range(12): # recover the data during the 12 months of the year
    for l in range(4): # recover the 4 weeks of the month
        for k in range (7): # recover the data during 7 days
            for j in range(24): # recover data during 24 hours.
                for i in range(4): # recover data every 1/4 hour.
                    try: # to avoid the error of the server not returning anything
                        url = 'https://datosabiertos.malaga.eu/recursos/aparcamientos/ocupappublicosmun/ocupappublicosmun.csv'
                        r = requests.get(url,allow_redirects=True)
                        name = "../RESULTS/"+str(datetime.now()) +'.csv';
                        open(name,'wb').write(r.content)
                    except:
                        pass
                    message = "Extraction done at: " + str(datetime.now())
                    print(message)
                    time.sleep(900)
                # Uploading the results to Github every one hour
                os.system("git -C ../ add .")
                commit_name = "git -C ../ commit -m \"Commit done on:" + str(datetime.now()) + "\""
                print(commit_name)
                os.system(commit_name)
                os.system("git -C ../ push origin main")
                message = "Commit done at: " + str(datetime.now())
                print(message)


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

