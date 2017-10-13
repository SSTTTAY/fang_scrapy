from .models import rent_fang,ask_rent,price_pre




def area_analys(fang):
    # num_data = len(ask_rent.objects)
    # print(num_data)

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
    # print(area_num)
    # print(area_index)
    return area_num,area_index

def gen_data(area_index,post_time):
    lenth = 0
    if lenth <= len(area_index):
        for area,time in zip(area_index,post_time):
            data={
            'name':area,
            'data':[time],
            }
            yield data
            lenth += 1

def piechart(area_index,post_time):
    data=[[area,num] for area,num in zip(area_index,post_time)]
    return data

def anlyprice(fang,area):
    count = 1
    price = 0
    for i in fang.find():
        if i['address'][0] == 'area':
            if i['price'] != None:
                price+=int(i['price'])
                count+=1
    avg_price = price/count
    return avg_price

def analysdiv(fang):
    # num_data = len(ask_rent.objects)
    # print(num_data)

    div_list=[]
    for item in fang.objects:
        if item.info != []:
            area = item.info[0]
            div_list.append(area)

    area_index = set(div_list)
    area_num = []

    for index in area_index:
        area= div_list.count(index)
        area_num.append(area)
    # print(area_num)
    # print(area_index)
    return area_num,area_index

analysdiv(rent_fang)




