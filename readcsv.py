import csv

csv_file = open("Journal.csv", "r", encoding="utf-8", errors="", newline="" )

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
#print(header)
preUUID=''
for row in f:
    #rowはList
    #row[0]で必要な項目を取得することができる
    #uuidが同じ値が2つ連続する仕様なので、2つ目を取るとする
    #ある値と次の値を比較する 今回分を前回分としてとっておくpreValueとしましょうかね
    if row[2]==preUUID:
        print("")
    else:
        print(row[2])
        preUUID=row[2]