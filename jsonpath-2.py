import jsonpath
import json
import urllib.request

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
req = urllib.request.Request(url)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')
#print(html)

json_obj = json.loads(html)
#print(json_obj)

city_list = jsonpath.jsonpath(json_obj,'$..name')
print(city_list)
with open('city.json','w') as f:
    content = json.dump(city_list,f,ensure_ascii=False)
    #f.write(content)
    f.close()