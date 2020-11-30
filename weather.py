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
        weather_str = '<p>位置：' + address +  '</p></n>' + '<p>时间：' + time +  '</p></n>' + '<p>温度：' + temperature +  '</p></n>'  + '<p>天气：' + weather +  '</p></n>' \
        + '<p>风力：' + wind_power + '</p></n>'+ '<p>天气实况：' + weather_conditions +  '</p></n>' + '<p>' + jz_Gls +  '</p></n>'
        return weather_str
    except Exception as e:
        print(e)



if __name__ == '__main__':
    print(weather_main('咸阳'))
# for i in VariationChilds:
#     print(i.childNodes[0].nodeValue)
