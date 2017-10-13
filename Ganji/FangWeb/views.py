from django.shortcuts import render
from .models import rent_fang,ask_rent,second_fang,business_fang,price_pre
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .data_analys import area_analys,gen_data,piechart,analysdiv
from .updatadb import anlyprice
import json

def strchange(fang):
    if fang == 'second_fang':
        return second_fang
    if fang == 'rent_fang':
        return rent_fang
    if fang == 'business_fang':
        return business_fang

def predict(request):
    new_price_data=[]
    new_total_data=[]
    second_price=[]
    second_total=[]
    rent_price=[]
    rent_total =[]
    for item in price_pre.objects:
        if item['fang'] == 'new_fang':
            new_price_data.append(item['price'])
            new_total_data.append(item['total'])
        if item['fang'] == 'second':
            second_price.append(item['price'])
            second_total.append(item['total'])
        if item['fang'] == 'rent':
            rent_price.append(item['price'])
            rent_total.append(item['total'])
    context={
        'new_price':new_price_data,
        'new_total':new_total_data,
        'second_price':second_price,
        'second_total':second_total,
        'rent_price':rent_price,
        'rent_total':rent_total,
    }
    return render(request,'predict/predict.html',context)


def index(request):
    try:
        fang_type = request.GET.get("fang")
        if fang_type == None:
            fang_type = 'rent_fang'
    except:
        fang_type = 'rent_fang'

    limit = 15
    fang_limit = strchange(fang_type).objects.limit(15)
    paginator = Paginator(fang_limit,limit)
    # page = request.Get.get('page')
    try:
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except :
        page = 1
    try:
        fangs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        fangs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        fangs = paginator.page(paginator.num_pages)

    context={
        'rent_fang':fangs,
        'count':strchange(fang_type).objects.count(),
    }
    return render(request, 'base/lists.html', context)

def chartpage(request):
    try:
        fang = request.GET.get("fang")
        if fang == None:
            fang = 'rent_fang'
    except:
        fang = 'rent_fang'
    #转化成数据库
    fang_ = strchange(fang)
    # #地区列表
    # area_list = area_analys(fang_)[1]

    data = area_analys(fang_)
    #地区列表
    area_index = list(data[1])
    #地区数量
    post_time = data[0]
    # 价格列表
    price_list = [anlyprice(fang_, area_) for area_ in area_index]
    print(price_list)
    #生成series数据
    # area_data = gen_data(area_index,post_time)
    List = [data for data in gen_data(area_index, post_time)]

    piedata=piechart(area_index,post_time)
    #分布
    div_data = analysdiv(strchange(fang))
    div_cate = div_data[0]
    series_data=[]
    for item in div_data[1]:
        series_data.append(item)
    context={
        'List':json.dumps(List),
        'PieData':piedata,
        'PriceList':price_list,
        'AreaList':area_index,
        'Spyder_cata':div_cate,
        'Spyder_data':series_data,

    }
    return render(request, 'base/chartpage.html', context)

def second(request):
    limit = 15
    fang_limit = ask_rent.objects.limit(15)
    paginator = Paginator(fang_limit,limit)

    # page = request.Get.get('page')
    # try:
    #     fangs = paginator.page(page)
    # except PageNotAnInteger:
    #      #If page is not an integer, deliver first page.
    #     fangs = paginator.page(1)
    # except EmptyPage:
    #     #If page is out of range (e.g. 9999), deliver last page of results.
    #     fangs = paginator.page(paginator.num_pages)

    context={
        'ask_rent':fang_limit,
        'count':ask_rent.objects.count()

    }
    return render(request, 'second/secondlist.html', context)