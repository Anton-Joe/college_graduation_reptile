#coding:utf-8

# 爬虫基本框架
# def getHTMLText(url):
#     try:
#         r = requests.get(url)
#         r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
#         r.encoding = r.apparent_encoding
#         return r.headers
#     except:
#         return "产生异常"
#
#
# if __name__ == "__main__":
#     url = "https://www.baidu.com"
#     print(getHTMLText(url))
#
#     r = requests.post('http://httpbin.org/post', 'ABC')
#     print(r.text)

# 测试爬取JD商品页面
# import requests
# r = requests.get('https://item.jd.com/100009082500.html')
# print(r.status_code)
# print(r.encoding)
# print(r.text[:1000])

# 爬取亚马逊的商品信息，亚马逊不允许user-agent==爬虫的程序访问，需要修改user-agent参数
# import requests
# kv = {'user-agent': 'Mozilla/5.0'}
# r = requests.get('https://www.amazon.cn/dp/B0793HNPFR?ref_=Oct_RecCard_dsk_asin3&pf_rd_r=H2PE0Y96SPGYBNT5QEJN&pf_rd_p=d7526bc5-3640-48d5-8d6b-448fefacc51e&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-4', headers=kv)
# print(r.status_code)
# r.encoding = r.apparent_encoding
# print(r.text)
# print(r.request.headers)

# 测试百度关键词提交
# import requests
# kv = {'wd': 'Python'}
# r = requests.get('http://www.baidu.com/s', params=kv)
# print(r.status_code)
# print(r.request.url)
# print(len(r.text))

# 保存图片
# import requests
# path = '/Users/yejingxuan/Desktop/test.jpeg'
# imgUrl = 'http://photocdn.sohu.com/20150613/mp18715484_1434167464942_6.jpeg'
# r = requests.get(imgUrl)
# print(r.status_code)
# with open(path, 'wb') as file:
#     file.write(r.content)
#     file.close()
#     print("保存成功！")

# ip地址归属地查询
# import requests
# url = 'http://m.ip138.com/ip.asp?'
# # r = requests.get(url + '202.204.80.112')
# kv = {'ip': '202.204.80.112'}
# r = requests.get(url, params=kv)
# print(r.status_code)
# print(r.text)


# 使用BeautifulSoup解析Html文档
# import requests
# from bs4 import BeautifulSoup
# r = requests.get('http://python123.io/ws/demo.html')
# demo = r.text
# soup = BeautifulSoup(demo, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# # 只能返回第一个a标签
# print(soup.a.attrs)
# print(soup.a.string)
# print(soup.p.string)
# print(soup.head.contents)
# print(soup.body.contents)
# print(soup.body.contents[1])
# print("-")
# for child in soup.body.children:
#     print(child)
# print(soup.title.parent)
# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)
# print(soup.p)
# print(soup.p.next_sibling.next_sibling)
# print(soup.prettify())

# 查找所有a标签，遍历
# import requests
# from bs4 import BeautifulSoup
# r = requests.get('http://python123.io/ws/demo.html')
# demo = r.text
# soup = BeautifulSoup(demo, 'html.parser')
# for link in soup.find_all('a'):
#     print(link.attrs['href'])
# print(soup.find_all('a'))
# print(soup.find_all(['a', 'b']))

# 实例：中国大学排名定向爬虫
# import requests
# from bs4 import BeautifulSoup
# import bs4
# r = requests.get('http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html')
# r.encoding = r.apparent_encoding
# demo = r.text
# soup = BeautifulSoup(demo, 'html.parser')
# uinfo = []
#
# for tr in soup.tbody.children:
#     if isinstance(tr, bs4.element.Tag):
#         tds = tr('td')
#         uinfo.append([tds[0].string, tds[1].string, tds[2].string])
#
# for univ in uinfo:
#     print(univ[0], univ[1], univ[2])

# 字符串匹配库
# import re
# ls = re.findall(r'^[1-9]\d{5}', 'BIT100081 TSU100084')
# print(ls)
# print(re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084'))
# pat = re.compile(r'[1-9]\d{5}')
# rst = pat.search('Bit 100081')
# print(rst.group(0))
# print(rst.re)

# 实验：循环爬取淘宝商品信息
# import re
# import requests
# from bs4 import BeautifulSoup
#
#
# def getHTMLText(url):
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         print("Error：获取HTML失败")
#
#
# def parsePage(ilt, html):
#     try:
#         plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
#         tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
#         for i in range(len(plt)):
#             price = eval(plt[i].split(':')[1])
#             title = eval(tlt[i].split(':')[1])
#             ilt.append([price, title])
#     except:
#         print("error:parsePage")
#
#
# if __name__ == "__main__":
#     goods = '书包'
#     depth = 2
#     itemList = []
#     start_url = 'https://taobao.com/search?q=' + goods
#     for i in range(depth):
#         try:
#             url = start_url + '&s=' + str(44 * i)
#             html = getHTMLText(url)
#             parsePage(itemList, html)
#         except:
#             continue

# test
import requests
import json
import pymysql
import time

def fetchCmts(hotel, page):
    url = "https://m.ctrip.com/restapi/soa2/16765/gethotelcomment?&_fxpcqlniredt=09031074110034723384"
    headers = {
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://m.ctrip.com',
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    formData = {
        'groupTypeBitMap': '2',
        'hotelId': str(hotel),
        'pageIndex': str(page),
        'pageSize': '10',
        'travelType': '-1',
    }
    r = requests.post(url, data=formData, headers=headers)
    r.raise_for_status()
    r.encoding = "utf-8"
    return r.text


def parseJsonAndLoadIntoDB(HTML, hotelID2):
    data = eval(json.dumps(HTML['othersCommentList'], ensure_ascii=False))
    for one in data:
        contentID = one['id']
        checkInDate = one['checkInDate']
        postDate = one['postDate']
        userLevel = one['commenterGrade']
        userGiveScore = one['ratingPoint']
        userGiveScoreDesc = one['ratingPointDesc']
        travelType = one['travelType']
        content = one['content']
        userCommentUsefulCount = one['userCommentUsefulCount']
        if 'feedbackList' in one:
            feedBackContent = one['feedbackList'][0]['content']
        else:
            feedBackContent = ""
        if 'hasHotelFeedBack' in one:
            hasHotelFeedback = one['hasHotelFeedback']
        else:
            hasHotelFeedback = 0
        isUserFeedBackFeedBack = one['isCanFeedback']
        imgCount = len(one['imageList'])

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='565648923z1',
                                     db='ctrip',
                                     charset='utf8mb4')
        cur = connection.cursor()
        sql = """ 
        Insert into hotelContent values ('{ID}','{level}','{giveScore}','{giveScoreDesc}',
        '{travelType}','{content}','{usefulCount}','{feedBackContent}','{hasHotelFeedback}',
        '{isUserFeedBackFeedBack}','{imgCount}','{contentID}','{checkinDate}','{postDate}')
        """.format(ID=hotelID2, level=userLevel, giveScore=userGiveScore, giveScoreDesc=userGiveScoreDesc, travelType=travelType, content=content, usefulCount=userCommentUsefulCount,\
                   feedBackContent=feedBackContent, hasHotelFeedback=hasHotelFeedback, isUserFeedBackFeedBack=isUserFeedBackFeedBack, imgCount=imgCount, contentID=contentID, checkinDate=checkInDate, postDate=postDate)
        print(sql)
        try:
            cur.execute(sql)
        except:
            print("失败！!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

            continue
        connection.commit()
        connection.close()


def getHotelIDAndContentCount():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='565648923z1',
                                 db='ctrip',
                                 charset='utf8mb4')
    cur = connection.cursor()
    sql = "select hotelID,commentCount from hotellist where hotellevel in ('经济型', '国家旅游局评定为二星级' ) and hotelID not in ( select DISTINCT hotelID from  hotelContent)"
    cur.execute(sql)
    hotelID = cur.fetchall()

    connection.close()
    return hotelID

if __name__ == "__main__":
    while 1:
        try:
            hotelID = getHotelIDAndContentCount()
            for (id, contentCount) in hotelID:
                if contentCount > 5 :
                    count = int(contentCount / 5)
                    # if count >=1000:
                    #     count = 1000
                elif contentCount == 0:
                    print("content==0 ; hotelID={id}".format(id=id))
                    continue
                else:
                    count = 1
                for i in range(0, count):
                    time.sleep(0.5)
                    print("{time} : hotel:{hotelID} is still running, index={index},count={count}, contentCount={contentCount}".format(time=time.time() , index=i, count=count, contentCount=contentCount, hotelID=id))
                    try:
                        htmlText = fetchCmts(id, i+1)
                        jsonDict = json.loads(htmlText)
                        if len(jsonDict['othersCommentList']) != 0:
                            parseJsonAndLoadIntoDB(jsonDict, id)
                        else:
                            break
                    except:
                        print('i am here')
                        break
        except:
            print("eeeoee")
            time.sleep(5)




# a = json.loads(fetchCmts('15331400', 1))
# b = eval(json.dumps(a['othersCommentList'], ensure_ascii=False))
# print(type(b))


# print(b[1]['commenterGrade']) # 用户等级
# print(b[1]['ratingPoint']) # 顾客打分
# print(b[1]['ratingPointDesc']) # 顾客打分描述
# print(b[1]['travelType']) # 顾客旅行方式
# print(b[1]['userCommentCount']) # 顾客点评数量
# print(b[1]['content'])
# print(b[1]['userCommentUsefulCount']) # 被点有用点评
# print(b[1]['feedbackList'][0]['content']) # 酒店回复
# print(b[1]['hasHotelFeedback']) # 店家是否回复
# print(b[1]['isCanFeedback']) # 顾客针对店家是否回复
# print(len(b[1]['imageList'])) # 图片个数