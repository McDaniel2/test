

'''
OK的 小说的
import requests
from bs4 import BeautifulSoup
targrt = "https://www.biqukan.com/24_24125/"
response = requests.get(targrt) 
html = response.text
soup = BeautifulSoup(html)
divs = soup.find_all('div',class_ = 'listmain')
lianjie = BeautifulSoup(str(divs[0]))
aa = lianjie.find_all('a')
#print(divs[0].text)
with open('zhangjielianjie.txt','w') as file:   
    for b in aa:
        abc = b.text
        efg = b.get('href')
        print(abc,efg)
        file.write("章节:{} 链接:{}\n".format(abc,efg))
'''

"""
腾讯新闻的
import requests
from bs4 import BeautifulSoup
targrt = "http://sports.qq.com/a/20181106/010025.htm"
response = requests.get(targrt) 
html = response.text
soup = BeautifulSoup(html)
divs = soup.find_all('div',class_ = 'qq_article')
pp = BeautifulSoup(str(divs[0]))
aa = pp.find_all('p',class_='text')
""""""print(divs[0].text)""""""
with open('zhangjielianjie.txt','w') as file:   
    for b in aa:
        abc = b.text
        print(abc)
        file.write("{}\n".format(abc))
        """

"""
今日头条
JS import requests
import json
url = 'https://www.toutiao.com/2/wap/search/extra/pc_hot_search/'
wbdata = requests.get(url).text
data = json.loads(wbdata)
news = data['data']['search_words']
for n in news:   
   title = n['q']    
#  img_url = n['image_url']    
 # url = n['media_url']    
  print(title)
  """

'''
#很有问题的，
#{'message': 'error', 'data': [], 'has_more': False}是怎么回事
import requests
import json
url = 'https://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1C5CB8E025900C&cp=5BE2C900909CDE1&_signature=qWXOsQAA8pVnDkhjT2QS.6llzq'
a = requests.get(url)
#data = json.dumps(a)
#news = data['data']
print(a)
#for n in news:    
 # title = n['title']    
  #print(title)
 #  img_url = n['image_url']    
 # url = n['media_url']  
 # 
 '''

'''
糗事百科的
import requests
from bs4 import BeautifulSoup
url = 'https://www.qiushibaike.com/8hr/page/1/'
response = requests.get(url)
req = response.text
soup = BeautifulSoup(req)

writer = soup.find_all('div','author clearfix')
duanzi = BeautifulSoup(str(writer[0]))
duanzi1 = soup.find_all('div','content')

for a in writer:
    a = a.text   
    for b in duanzi1:   
        b = b.text
        print (a.replace('\n',''))
        print (b.replace('\n',''))
        print ('\n')
'''
        
'''
随便一个人的微博 可以的
import requests
import json
from bs4 import BeautifulSoup
cook = {
    "Cookie": "SINAGLOBAL=1180762788830.516.1538900618196; UM_distinctid=1665e9465fe9-0da56a0ffd3eef-75283355-100200-1665e9465ff433; un=1805815201@qq.com; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5EJG8CMcFu8G6FssyG53oq5JpX5KMhUgL.Foec1h2N1K501hz2dJLoI79WCXvlK0nt; TC-V5-G0=5fc1edb622413480f88ccd36a41ee587; ALF=1573037976; SSOLoginState=1541501980; SCF=AqWoPAjkTwIFdfQ9pKH-D9Agvq0ZDg3hHyh2_akFqh-y7h36G0OqTOviOmMLH1OoPcDkiyk_ar6__1HYXJiEXlY.; SUB=_2A2525QRMDeRhGeVI41MW-S7Pwz6IHXVVk3KErDV8PUNbmtAKLUbhkW9NT-bg11Hoc-O1QO6lD1faBRgDeL4OXt6u; SUHB=0laV5EWgIATe2B; Hm_lvt_668f5751b331d2a1eec31f2dc0253443=1541208886,1541302214,1541343796,1541501992; TC-Page-G0=e2379342ceb6c9c8726a496a5565689e; _s_tentry=login.sina.com.cn; Apache=1307090069517.9487.1541501998956; ULV=1541501999017:31:5:3:1307090069517.9487.1541501998956:1541343794839; YF-V5-G0=82f55bdb504a04aef59e3e99f6aad4ca; YF-Page-G0=280e58c5ca896750f16dcc47ceb234ed; wb_view_log_3681790382=1366*7681; UOR=,,ent.ifeng.com; Hm_lpvt_668f5751b331d2a1eec31f2dc0253443=1541582205"
}
targrt = "https://m.weibo.cn/api/container/getIndex?is_all[]=1&is_all[]=1&jumpfrom=weibocom&type=uid&value=2846332925&containerid=1076032846332925"
wbdata = requests.get(targrt,cookies = cook).text
#response.encoding=('uft-8')
data = json.loads(wbdata)
news = data['data']['cards']
for c in news:
    content = c['mblog']
    a = content['text']
    soup = BeautifulSoup(a,"lxml")
    b = soup.text
    print(b)
#print(type(a))

#content = soup.find_all('div',class_ = 'WB_detail')
#lianjie = BeautifulSoup(str(divs[0]))
#aa = lianjie.find_all('a')
'''

'''
微博环球资讯的 可以的
import requests
import json
from bs4 import BeautifulSoup
cook = {
    "Cookie": "HMACCOUNT=82770BA1AA7BA3D5; BAIDUID=72106726825A3CAA53A032A45DB199B9:FG=1; PSTM=1538748708; BIDUPSID=42AE502C99FD55D39CBA6F08E4459A1C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-302%3A; H_PS_PSSID=1457_21085_27377_26350; BDUSS=1JqdVViWkdieVk3Z29DQ0dqanBneTBTTG1wbH5MSGRhdVN1UWNHUWJhNVk2QWxjQUFBQUFBJCQAAAAAAAAAAAEAAACRSv1~U29sYXIwMjIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFhb4ltYW-JbN; HMVT=6bcd52f51e9b3dce32bec4a3997715ac|1541587248|; delPer=0; PSINO=6"
}
targrt = "https://m.weibo.cn/api/container/getIndex?type=uid&value=1656831930&containerid=1076031656831930"
wbdata = requests.get(targrt,cookies = cook).text
#response.encoding=('uft-8')
data = json.loads(wbdata)
news = data['data']['cards']
#print(news)
for c in news:
    content = c['mblog']
    a = content['text']
    soup = BeautifulSoup(a,"lxml")
    b = soup.text
    print(b+'\n')
#print(type(a))
'''

'''
下载图片 
import requests
import urllib.request
from bs4 import BeautifulSoup
url = 'https://www.biquge5200.cc/'
response = requests.get(url).text
soup = BeautifulSoup(response)
img = soup.find_all('div',class_='image')
x = 0
for a in img:
    imm = a.find_all('img')
    for immm in imm:
        b = immm.get('src')
        #c = urllib.request.urlopen(b)       
        #d = c.read()
        print (b)       
        urllib.request.urlretrieve(b,'F:\电影\空0\%s.jpg' % x)
        x += 1
'''
'''
import requests
import json
from bs4 import BeautifulSoup
cook = {
    "Cookie": "_T_WM=f26f4f82bffdadc632afed0445d245b6; ALF=1544258921; WEIBOCN_FROM=1110006030; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5EJG8CMcFu8G6FssyG53oq5JpX5K-hUgL.Foec1h2N1K501hz2dJLoI79WCXvlK0nt; SSOLoginState=1541667155; MLOGIN=1; SCF=AqWoPAjkTwIFdfQ9pKH-D9Agvq0ZDg3hHyh2_akFqh-yEKC20uNyT2kRYtcszOQuCo2UzoNTso8NZ-IhLQfY7OY.; SUB=_2A25254kDDeRhGeVI41MW-S7Pwz6IHXVSKxdLrDV6PUJbktAKLVrfkW1NT-bg11-VMQ9_nk_EsnBFFlUfotEN6WBm; SUHB=0cS3IuJaWoF2_e; Hm_lvt_668f5751b331d2a1eec31f2dc0253443=1541570355,1541570501,1541667167,1541667382; M_WEIBOCN_PARAMS=from%3Dfeed%26luicode%3D10000011%26lfid%3D1076031797679051%26fid%3D1076031742566624%26uicode%3D10000011; Hm_lpvt_668f5751b331d2a1eec31f2dc0253443=1541667835"
}
targrt = "https://m.weibo.cn/api/container/getIndex?type=uid&value=1656831930&containerid=1076031656831930&since_id=4303726577486692"


wbdata = requests.get(targrt,cookies = cook).text
#response.encoding=('uft-8')
data = json.loads(wbdata)
news = data['data']['cards']
#print(news)
for c in news:
    content = c['mblog']
    a = content['text']
    soup = BeautifulSoup(a,"lxml")
    b = soup.text
    print(b+'\n')
#print(type(a))
   '''
'''
JS翻页的 成语的
import requests
import json
from bs4 import BeautifulSoup
y = 0
x = 0
for i in range(6):
    a = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6848&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=%E6%88%90%E8%AF%AD&sort_key=&sort_type=1&stat0=&stat1=&stat2=5%E5%AD%97&stat3=&'
    b = 'pn='+ str(x)
    c = '&rn=25&_=154173195406' + str(y)
    url = a+b+c
    wbdata = requests.get(url).text
    data = json.loads(wbdata)
    news = data['data']
    for n in news:    
        name = n['disp_data']
        for n in name:
            name1 = n['ename']
            soup = BeautifulSoup(name1)  
            mz = soup.text
            print(mz)   
    print('\n') 
    print(x,y)
    x = x+25
    y = y+1
    '''
'''
链家 查找更进一步
import requests
from bs4 import BeautifulSoup
targrt = "https://bj.lianjia.com/zufang/"
response = requests.get(targrt) 
html = response.text
soup = BeautifulSoup(html)
divs = soup.find_all('div',class_ = 'info-panel')
for x in divs:
    z = x.find_all('h2')
    b = x.find_all('div',class_='price')
    f = BeautifulSoup(str(z[0]))
    g = f.find_all('a')
    for a in g:
        title = a.text#get('title')
        lianjie = a.get('href')
        print(title+'\n',lianjie )
    for d in b:
        pr = d.text  
        print(pr+'\n')
'''
            
'''
拉钩网 post请求 
import requests
import json
from bs4 import BeautifulSoup
data = {"first": "true",
        "pn": "1",
        "kd": "爬虫"
}
HEADERS = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput='
}

targrt = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
response = requests.post(targrt,headers=HEADERS,data = data) 
aa = response.text
aaa = json.loads(aa)
data = aaa['content']['positionResult']['result']
for ct in data:
    nm = ct['companyFullName']
    pm = ct['positionName']
    salary = ct['salary']  
    print ("公司：{}\n位置:{}\n薪水:{}\n".format(nm,pm,salary))
'''
'''
存excel的
import requests
import xlsxwriter
from bs4 import BeautifulSoup
url = "https://bj.lianjia.com/zufang/"
def get_text():
    resonse = requests.get(url).text
    soup = BeautifulSoup(resonse,'lxml')
    title0 = []
    lianjie0 = []
    divs = soup.find_all('div',class_ = 'info-panel')
    for x in divs:
        z = x.find_all('h2')
        b = x.find_all('div',class_='price')
        f = BeautifulSoup(str(z[0]),'lxml')
        g = f.find_all('a')
        for a in g:
            title = a.text#get('title')
            lianjie = a.get('href')
            title0.append(title)
            lianjie0.append(lianjie)
            workbook11 = xlsxwriter.Workbook('测试的表.xlsx')    # 创建一个名为‘Demo1.xlsx’的工作表
            worksheet12 = workbook11.add_worksheet('100')
            i = 1
            j = 1            
            for aaa in title0:                 
                worksheet12.write(i,2,aaa) 
                i = i+1      
            for bbb in lianjie0: 
                worksheet12.write(j,6,bbb)                                       
                j = j+1
            workbook11.close() 
if __name__ == '__main__':
    get_text()
'''
    


'''
微博cn 多少页都OK的
import requests
from bs4 import BeautifulSoup
url1 = 'https://weibo.cn/newsvideo?page='
for i in range(1,5):    
    url2 = i
    url = url1 + str(url2)
    cook = {"Cookie": "_T_WM=f26f4f82bffdadc632afed0445d245b6; ALF=1544926547; SCF=AqWoPAjkTwIFdfQ9pKH-D9Agvq0ZDg3hHyh2_akFqh-yYspTSZERtjRh-Vd3gKMtRYZ4sbfc9Swm5ZvSfGr3KvE.; SUB=_2A2526lj5DeRhGeVI41MW-S7Pwz6IHXVSFXixrDV6PUJbktAKLVfskW1NT-bg13AqYymTrt7AO6lAoh58rAcfmZjv; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5EJG8CMcFu8G6FssyG53oq5JpX5K-hUgL.Foec1h2N1K501hz2dJLoI79WCXvlK0nt; SUHB=0LcCl1RTnZwQru; SSOLoginState=1542334633; Hm_lvt_668f5751b331d2a1eec31f2dc0253443=1542334643,1542335134,1542335145; Hm_lpvt_668f5751b331d2a1eec31f2dc0253443=1542337032"}
    response = requests.get(url,cookies = cook).text
    soup = BeautifulSoup(response)
    divs = soup.find_all('div',class_='c')   
    divs = BeautifulSoup(str(divs),'lxml')
    spc = divs.find_all('span',class_='ctt')
    for a in spc:
        aa = a.text
        print (aa)
        print('\n')
    i = i+1
'''
'''
500页微博
import requests
from bs4 import BeautifulSoup
url1 = 'https://weibo.cn/crinews?page='
j = 1
proxy = {'HTTP': '61.135.217.7:80' }
with open('henduode.txt','w',encoding='utf-8') as file:  
    for i in range(1,501):    
        url2 = i
        url = url1 + str(url2)
        cook = {"Cookie": "_T_WM=f26f4f82bffdadc632afed0445d245b6; ALF=1545032081; SCF=AqWoPAjkTwIFdfQ9pKH-D9Agvq0ZDg3hHyh2_akFqh-yfdDVazHtYtCw9alOZ0uUSkQ19aerzGUK3-ltHd8f3hc.; SUB=_2A25267TtDeRhGeVI41MW-S7Pwz6IHXVSF9ylrDV6PUJbktANLRD2kW1NT-bg14hW06YUwpS06JloKzqAKR48eV-G; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5EJG8CMcFu8G6FssyG53oq5JpX5K-hUgL.Foec1h2N1K501hz2dJLoI79WCXvlK0nt; SUHB=0QSp49jAn5Jg_a; SSOLoginState=1542440125; Hm_lvt_668f5751b331d2a1eec31f2dc0253443=1542334643,1542335134,1542335145,1542440136; Hm_lpvt_668f5751b331d2a1eec31f2dc0253443=1542440136"}
        response = requests.get(url,cookies = cook,proxies = proxy).text
        soup = BeautifulSoup(response)
        divs = soup.find_all('div',class_='c')   
        divs = BeautifulSoup(str(divs),'lxml')
        spc = divs.find_all('span',class_='ctt')
        for a in spc:
            aa = a.text
            print (j,aa)
            print('\n')            
            file.write("{} {}\n".format(j,aa))
            j = j+1
    i = i+1             
'''
'''
setproxyhandler = ProxyHandler({"HTTPS":"101.132.122.230"})
seopener = build_opener(setproxyhandler)
install_opener(setproxyhandler)
'''
'''
天气的
import requests
from bs4 import BeautifulSoup

def parseurl(url):
    #headers = {}
    response = requests.get(url)
    response = response.content.decode('utf-8')
    soup = BeautifulSoup(response,'lxml')  
    # print (response)
    out = soup.find('div',class_='conMidtab')
    table = out.find_all('div',class_='conMidtab2')
    for trall in table:
        trss = trall.find_all('tr')[2:]
        for index,trs in enumerate(trss):
            cityss = trs.find_all('td')
            citytd = cityss[0]
            if index == 0:
                citytd = cityss[1]
            city = list(citytd.stripped_strings)[0]#list(citytd.strings)[1]   #  #citytd.text返回一个换行和城市文本
            tempsstd = cityss[-5]
            temp = list(tempsstd.stripped_strings)[0]
            print ('城市：{}，最高气温：{}'.format(city,temp))

def main():
    urls = [
        "http://www.weather.com.cn/textFC/hb.shtml",
        "http://www.weather.com.cn/textFC/db.shtml",
        "http://www.weather.com.cn/textFC/hd.shtml",
        "http://www.weather.com.cn/textFC/hz.shtml",
        "http://www.weather.com.cn/textFC/gat.shtml"

        ]
    for url in urls:
        parseurl(url)

if __name__ == '__main__':
    main()

'''