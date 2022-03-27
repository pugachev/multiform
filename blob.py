#ライブラリのインポート
import glob
list = glob.glob('./tgtphtos/*')
for file in list:
    print(file)