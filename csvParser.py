import csv
import re

# 読み込み
outdata = []
pattern = '\d{4}-\d{2}-\d{2}'
with open('Journal.csv', encoding="utf-8") as f:
    csv_reader = csv.DictReader (f)
    line_count = 0
    for row in csv_reader :
        if line_count ==0:
            print("データなし")
        else:
            #print(str(re.match(pattern,row["date"]).group())+" : "+row["text"])
            d = []
            d.append(str(re.match(pattern,row["date"]).group())+" : "+row["text"])
            outdata.append(d)
        line_count += 1

# 書き込み
with open('csvout.csv', 'w', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(outdata)