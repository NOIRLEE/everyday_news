import random
from urllib.request import urlopen
from urllib.parse import urlencode,quote,unquote
from xml.dom.minidom import parseString
def weather_main(add):
    try:
        add = quote(add)
        index_url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName=%s'%add
        response1 = urlopen(index_url)  #发送请求
        xml_string = response1.read().decode()
        DOMTree = parseString(xml_string)
        collection = DOMTree.documentElement

        VariationChilds = collection.getElementsByTagName("string")
        address = VariationChilds[1].childNodes[0].nodeValue
        time = VariationChilds[4].childNodes[0].nodeValue
        temperature = VariationChilds[5].childNodes[0].nodeValue
        weather = VariationChilds[6].childNodes[0].nodeValue
        wind_power = VariationChilds[7].childNodes[0].nodeValue
        weather_conditions = VariationChilds[10].childNodes[0].nodeValue
        jz_Gls = VariationChilds[11].childNodes[0].nodeValue
        food_list = ['盖浇饭','麻辣牛肉面','兰州牛肉面','美丽的泡馍','馄饨小笼包','砂锅系列','豪华三合一油泼面系列','荞面饸饹/肉拌搓搓','擀面皮肉夹馍套餐','麻辣米线','香辣土豆片夹馍','养生粥系列','小火锅','麻辣烫','菜夹馍稀饭','西北风（谁抽到这个谁今天必倒霉）','重庆小面','沙县小吃','酸汤水饺/干蘸水饺','绵阳米粉','炸鸡汉堡/KFC/金拱门','烤面筋',]
        ssr = ['一般','高级','稀有','神器','史诗','传说','神话','通天灵宝','创世之神']
        ssr_color = {'一般':'white','高级':'blue','稀有':'purple','神器':'DeepPink','史诗':'gold','传说':'tomato','神话':'brown','通天灵宝':'maroon','创世之神':'red',}
        ssr_c = ssr[random.randint(0,len(ssr))]
        weather_str = '<p style="color:' + ssr_color[ssr_c] +'">今天吃：' + ssr_c + '-->' + food_list[random.randint(0,len(food_list))] +  '</p></n>' + '<p>位置：' + address +  '</p></n>' + '<p>时间：' + time +  '</p></n>' + '<p>温度：' + temperature +  '</p></n>'  + '<p>天气：' + weather +  '</p></n>' \
        + '<p>风力：' + wind_power + '</p></n>'+ '<p>' + weather_conditions +  '</p></n>' + '<p>' + jz_Gls +  '</p></n>'
        return weather_str
    except Exception as e:
        print(e)



if __name__ == '__main__':
    # food_list = ['盖浇饭', '麻辣牛肉面', '兰州牛肉面', '美丽的泡馍', '馄饨小笼包', '砂锅系列', '豪华三合一油泼面系列', '荞面饸饹/肉拌搓搓', '擀面皮肉夹馍套餐', '麻辣米线',
    #              '香辣土豆片夹馍', '养生粥系列', '小火锅', '麻辣烫', '菜夹馍稀饭', '西北风（谁抽到这个谁今天必倒霉）', '重庆小面', '沙县小吃', '酸汤水饺/干蘸水饺', '绵阳米粉',
    #              '炸鸡汉堡/KFC/金拱门', '烤面筋', ]
    print(weather_main('青岛'))
    # a = food_list[random.randint(0, len(food_list))]
    # print(a)
# for i in VariationChilds:
#     print(i.childNodes[0].nodeValue)
