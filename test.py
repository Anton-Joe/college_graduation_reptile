import requests
import re
import pymysql
import time


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error:页面获取阶段失败,url地址：' + url)


def parseHTML(hotelFirstList, html):
   try:
       JSONData = re.search(r'hotelPositionJSON.*', html).group(0)
       # print(JSONData)
       idList = re.findall(r'\"id\"\:\".*?\"', JSONData)
       hotelNameList = re.findall(r'\"name\"\:\".*?\"', JSONData)
       urlList = re.findall(r'\"url\"\:\".*?\"', JSONData)
       scoreList = re.findall(r'\"score\"\:\".*?\"', JSONData)
       userRecommendList = re.findall(r'\"dpscore\"\:\".*?\"', JSONData)
       userCommentCountList = re.findall(r'\"dpcount\"\:\".*?\"', JSONData)
       hotelLevelList = re.findall(r'\"stardesc\"\:\".*?\"', JSONData)

       for i in range(len(hotelNameList)):
           id = eval(idList[i].split(':')[1])
           hotelName = eval(hotelNameList[i].split(':')[1])
           url = 'https://hotels.ctrip.com/' + eval(urlList[i].split(':')[1])
           score = eval(scoreList[i].split(':')[1])
           userRecommend = eval(userRecommendList[i].split(':')[1])
           userComment = eval(userCommentCountList[i].split(':')[1])
           hotelLevel = eval(hotelLevelList[i].split(':')[1])
           hotelFirstList.append([id, hotelName, url, score, userRecommend, userComment, hotelLevel])
   except:
       print('error:解析网页出错')


def loadIntoDB(cityCName):
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='565648923z1',
                             db='ctrip',
                             charset='utf8mb4')
    cur = connection.cursor()
    for i in hotelFirstList:
        hotelID = i[0]
        hotelNmae = i[1]
        hotelURL = i[2]
        hotelScore = i[3]
        userRecommendRate = i[4]
        commentCount = i[5]
        hotelLevel = i[6]
        sql = "Insert into hotelList values('{ID}','{Name}','{URL}','{Score}','{re}','{count}','{city}', '{hotelLevel}');"\
            .format(ID=hotelID, Name=hotelNmae, URL=hotelURL, Score=hotelScore, re=userRecommendRate, count=commentCount, city=cityCName, hotelLevel=hotelLevel)
        print(sql)
        # cur.execute(sql)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    hotelFirstList = []
    cityCName = ['深圳', '重庆']
    cityEName = ['shenzhen30', 'chongqing4']
    url = 'https://hotels.ctrip.com/hotel/beijing1/p'
    for index, value in enumerate(cityCName):
        url = 'https://hotels.ctrip.com/hotel/' + str(cityEName[index]) + '/p'
        print(url)
        for i in range(1, 51):
            time.sleep(5)
            HTML = getHTMLText(url + str(i))
            print(HTML)
            parseHTML(hotelFirstList, HTML)
            loadIntoDB(value)
            hotelFirstList = []




