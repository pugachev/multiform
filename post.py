import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import glob
import os
import csv

# メールアドレスとパスワードの指定
USER = "mtake"
PASS = "Manabu2010"
OPTION="python"
preUUID=''

# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "name":USER,
    "password":PASS,
    "option":OPTION,
    "back":"https://blog.ikefukuro40.tech/post.php",
    "mml_id":"0"
}

# action
url_login = "https://blog.ikefukuro40.tech/login.php"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

# csv_file = open("./test_stock.csv", "r", encoding="utf-8", errors="", newline="" )
csv_file = open("./Journal.csv", "r", encoding="utf-8", errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
for row in f:

    if row[2]!=preUUID:
        preUUID=row[2]
    
        # tgtpic='./tgtphtos/'+row[2]
        if len(row[45])!=0:
            #画像が複数枚の場合の措置を追加
            tmp = row[45].split(',')
            if len(tmp)>1:
                for tmppic in tmp:
                    tgtpic='./photos/'+tmppic.strip()+'.jpeg'
                    if os.path.isfile(tgtpic):
                        file = [('image', (tgtpic, open(tgtpic, 'rb'), 'image/jpeg'))]
                    else:
                            tgtpic='./photos/'+tmppic.strip()+'.png'
                            if os.path.isfile(tgtpic):
                                file = [('image', (tgtpic, open(tgtpic, 'rb'), 'image/png'))]

                    dtitle=row[0]
                    
                    headers = { "Content-Type": "multipart/form-data" }
                    request_data = {
                        "name":USER,
                        "password":PASS,
                        "title":dtitle[0:10],
                        "body":row[1],
                        "category":row[3],
                        "headers":headers,
                        "back":"https://blog.ikefukuro40.tech/backend.php",
                        "mml_id":"0"
                    }

                    url_post = 'https://blog.ikefukuro40.tech/post.php'

                    res = session.post(url_post, files=file, data=request_data)

            else:
                    tgtpic='./photos/'+row[45].strip()+'.jpeg'
                    if os.path.isfile(tgtpic):
                        file = [('image', (tgtpic, open(tgtpic, 'rb'), 'image/jpeg'))]
                        dtitle=row[0]
                        
                        headers = { "Content-Type": "multipart/form-data" }
                        request_data = {
                            "name":USER,
                            "password":PASS,
                            "title":dtitle[0:10],
                            "body":row[1],
                            "category":row[3],
                            "headers":headers,
                            "back":"https://blog.ikefukuro40.tech/backend.php",
                            "mml_id":"0"
                        }

                        url_post = 'https://blog.ikefukuro40.tech/post.php'

                        res = session.post(url_post, files=file, data=request_data)

            # print(res)
            time.sleep(5)







# list = glob.glob('./tgtphtos/*')
# for tgtfile in list:
#     # file = [('image', ('takada.jpg', open('takada.jpg', 'rb'), 'image/jpeg'))]
#     print(os.path.split(tgtfile)[1])
#     file = [('image', (tgtfile, open(tgtfile, 'rb'), 'image/jpeg'))]

#     headers = { "Content-Type": "multipart/form-data" }
#     request_data = {
#         "name":USER,
#         "password":PASS,
#         "title":"連続美人さん",
#         "body":"美人さんを連続POSTしています",
#         "category":"1",
#         "headers":headers,
#         "back":"https://blog.ikefukuro40.tech/backend.php",
#         "mml_id":"0"
#     }

#     url_post = 'https://blog.ikefukuro40.tech/post.php'

#     res = session.post(url_post, files=file, data=request_data)
#     print(res)
#     time.sleep(5)


 
