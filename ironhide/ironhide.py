#! /usr/bin/python
from util import Util
import csv 
import urllib2
import json
import requests
import pandas as pd
import os,sys
from django.utils import timezone
sys.path.append(os.getcwd() + "/../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whynot.settings")
import django
django.setup()
from productentity.models import Productdata,Productfeed

utilObj = Util()
utilObj.printLog("hello")

url_feed = 'https://whynot-karuppaiahal.c9users.io/polls/productfeed/?format=json'
response = urllib2.urlopen(url_feed)
json_data_feed = json.loads(response.read())
print len(json_data_feed["results"])


for i in range(len(json_data_feed["results"])):
    url_csv = json_data_feed["results"][i]["product_feed_url"]
    print url_csv
    response = urllib2.urlopen(url_csv)
    cr = csv.reader(response)
    for row in cr:
        # iteration = 1
        # for item in row:
        #     print str(iteration) + " : " + item
        #     iteration = iteration + 1
        if row[0] == "id":
            continue
        productdata = Productdata()
        productdata.skuid = row[0]
        productdata.title =  row[1]
        productdata.description = row[2]
        productdata.google_product_category = row[3]
        productdata.product_type = row[4]
        productdata.link = row[5]
        productdata.image_link = row[6]
        productdata.condition = row[7]
        productdata.availability = row[8]
        productdata.price = float(row[9])
        if row[10] != "":
            productdata.sale_price = row[10]
        productdata.brand = row[11]
        productdata.gtin = row[12]
        productdata.gender = row[13]
        productdata.color = row[14]
        productdata.size = row[15]
        productdata.model_code = row[16]
        productdata.created_date = timezone.now()
        productdata.updated_date = timezone.now()
        productdata.save()
        
    # df1 = pd.read_csv(url_csv)
    # df2= df1.set_index("id")


