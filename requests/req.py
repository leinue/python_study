import requests
r = ''
r = requests.get(url='http://ivydom.com')
print(r.status_code)
r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})
print(r.url)
print(r.text)
