import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

# types = input("Enter question/not answer").strip()
domain = input("Enter domain").strip()
search = input("Enter question")
types=''
view = ''
tag=''
if 'recently' in search:
    view='newest'
elif 'votes' in search:
    view='votes'
if 'questions' in search:
    types='questions'
    tag='sort'
elif 'noanswered' in search:
    types='unanswered'
    tag='tab'
# if types == 'not answer':
#     types = 'unanswered'
url = 'https://stackoverflow.com'+'/'+types+'/tagged' + '/' + domain

# if types == 'questions':


print(url)

values = {tag: view,
             'pageSize': 15
           }

data = urllib.parse.urlencode(values)
print(data)
data = data.encode('utf-8')
print(data)
req = urllib.request.Request(url, data)

# url = 'https://stackoverflow.com/unanswered/tagged/python?tab=newest&pageSize=15'
resp = urllib.request.urlopen(url)
respdata = resp.read()


soup = BeautifulSoup(respdata)
for hr in soup.find_all("h3")[3:9]:
    print(hr.text)

