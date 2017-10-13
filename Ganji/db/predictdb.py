import pymongo

client = pymongo.MongoClient('localhost',27017)
db1 = client['ganji']
predictdb = db1['price_pre']

def put_into_data(fang,price,total):
    data = {'fang':fang,'price':price,'total':total}
    predictdb.insert_one(data)

price = [1.64,1.62,1.69,1.68,1.66]
total = [15300,8031,1332,6796,4442]

second_price = [2.8,2.84,2.88,2.93,3.05]
second_total = [23136,9905,8196,8157,7315]


# for p,t in zip(price,total):
#     put_into_data('new_fang',p,t)

for p,t in zip(second_price,second_total):
    put_into_data('second',p,t)