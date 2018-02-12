# import redis
#
# conn = redis.Redis()
# conn.keys("*")
# conn.set('secret', 'ni!')
# conn.set('carats',24)
# conn.set('fever',101.5)
#
# conn.get('carats')
# conn.getset('secret','lkjfdasjlkfalk-fd')
# conn.get('secret')
#
# conn.delete('secret')

import urllib.request as ur
import requests

url = "https://developer.yahoo.com/weather/documentation.html#2487956";
conn = ur.urlopen(url)
# print(conn)
resp = requests.get(url)
print(resp)
print(resp.text)

data = conn.read()
# print(data)
# print(conn.status)
data = conn.getheaders()
for key,value in data:
    print(key, value)
print( [int(value) for key,value in data if key=="Content-Length"] )



