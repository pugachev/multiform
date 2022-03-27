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

csv_file = open("./test_stock.csv", "r", encoding="utf-8", errors="", newline="" )
# csv_file = open("./Journal.csv", "r", encoding="utf-8", errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
for row in f:
    if len(row[2])!=0:
        #画像が複数枚の場合の措置を追加
        tmp = row[2].split(',')
        if len(tmp)>1:
            for tmppic in tmp:
                tgtpic='./tgtphtos/'+tmppic.strip()+'.jpg'
                if os.path.isfile(tgtpic):
                    file = [('image', (tgtpic, open(tgtpic, 'rb'), 'image/jpeg'))]
                else:
                        tgtpic='./tgtphtos/'+tmppic.strip()+'.png'
                        if os.path.isfile(tgtpic):
                            file = [('image', (tgtpic, open(tgtpic, 'rb'), 'image/png'))]

                dtitle=row[0]
                
                headers = { "Content-Type": "multipart/form-data" }
                request_data = {
                    "name":USER,
                    "password":PASS,
                    "title":row[0],
                    "body":row[1],
                    "category":row[3],
                    "headers":headers,
                    "back":"https://blog.ikefukuro40.tech/backend.php",
                    "mml_id":"0"
                }

                url_post = 'https://blog.ikefukuro40.tech/post.php'

                res = session.post(url_post, files=file, data=request_data)

                print("debug0 "+tgtpic.strip())

        else:
                tgtpic='./tgtphtos/'+row[2].strip()+'.jpg'
                # print(tgtpic)
                if os.path.isfile(tgtpic):
                    file = [('image', (tgtpic, open(tgtpic, 'rb'), 'image/jpeg'))]
                    dtitle=row[0]
                    
                    headers = { "Content-Type": "multipart/form-data" }
                    request_data = {
                        "name":USER,
                        "password":PASS,
                        "title":row[0],
                        "body":row[1],
                        "category":row[3],
                        "headers":headers,
                        "back":"https://blog.ikefukuro40.tech/backend.php",
                        "mml_id":"0"
                    }

                    url_post = 'https://blog.ikefukuro40.tech/post.php'

                    res = session.post(url_post, files=file, data=request_data)

                    print("debug0 "+tgtpic.strip())

        # print(res)
        time.sleep(5)
    else:
        print("データ終了です")
        break

print("debug1")
file=''
headers = { "Content-Type": "multipart/form-data" }
request_data = {
    "name":USER,
    "password":PASS,
    "title":'complete',
    "body":'complete',
    "category":'1',
    "headers":headers,
    "back":"https://blog.ikefukuro40.tech/backend.php",
    "mml_id":"0"
}

url_post = 'https://blog.ikefukuro40.tech/post.php'

res = session.post(url_post, files=file, data=request_data)
print("debug2")








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


 
