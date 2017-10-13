import requests
from bs4 import BeautifulSoup
import pymongo
import re
import time
from string import punctuation
from .models import rent_fang,ask_rent,business_fang


client = pymongo.MongoClient('localhost',27017)
db1 = client['ganji']
rent_fang = db1['rent_fang']
ask_rent = db1['ask_rent']

def updata_area():
    for i in rent_fang.find():
        if i['address']:
            if i['address'][0] == '经济开发区' or i ['address'][0] == '租房':
                address = '不明'
                rent_fang.update({'_id': i['_id']}, {'$set': {'address': address}})

    #for i in rent_fang.find().limit(30):
        # if i['address']:
        #     address = [i for i in i['address'] if i not in punctuation]
        # else:
        #     address='不明'
        # ask_rent.update({'_id':i['_id']},{'$set':{'address':address}})
        #print(i['address'])

def updata_price():
    for i in rent_fang.find():
        if i['price']:
            price = re.sub("\D","",i['price'])
        else:
            price = None
        rent_fang.update({'_id':i['_id']},{'$set':{'price':price}})
        print(rent_fang.price)

def area_analys(fang):
    area_list=[]
    for item in fang.objects:
        if item.address != []:
            area = item.address[0]
            area_list.append(area)

    area_index = set(area_list)
    area_num = []
    for index in area_index:
        area= area_list.count(index)
        area_num.append(area)
    print(area_num)
    print(area_index)
    return area_num,area_index

def anlyprice(fang,area):
    count = 1
    price = 0
    for i in rent_fang.find():
        if i['address'][0] == area:
            if i['price'] != '':
                price += int(i['price'])
                count += 1

    avg_price =round(price/count)

    return avg_price







#area_list = ['天河','增城','萝岗','从化','海珠','花都','番禺','越秀','荔湾','白云','黄埔']

#price_list = [2805, 1760, 2203, 1007, 3667, 1609, 2460, 3455, 1790, 1750, 1939]

# price_dict = [[area,price] for price,area in zip(price_list,area_list)]
# print(price_dict)

