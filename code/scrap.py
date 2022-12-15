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




# replace by: 336 (for 30 minutes scrapping), 168 (for 30 minutes scrapping)
for i in range(672): # recover data during 7 days every each 1/4 hour. Start 22-10-2022
    url = 'https://datosabiertos.malaga.eu/recursos/aparcamientos/ocupappublicosmun/ocupappublicosmun.csv'
    r = requests.get(url,allow_redirects=True)
    name = 'data('+ str(datetime.now()) +').csv';
    open(name,'wb').write(r.content)
    time.sleep(900)



# This is just another method for scrapping.
"""
for i in range(1):
    url = 'https://datosabiertos.malaga.eu/api/3/action/datastore_search?resource_id=0dcf7abd-26b4-42c8-af19-4992f1ee60c6&limit=100'
    fileobj = urllib.request.urlopen(url)
    json_object = json.dumps(fileobj.read().decode())
    name = 'data('+ str(i) +').json';
    with open(name,"w") as outfile:
        outfile.write(json_object)
"""

