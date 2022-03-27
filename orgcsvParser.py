import pandas as pd
csv_input = pd.read_csv(filepath_or_buffer="Journal.csv",  encoding="utf-8", sep=",")
# インプットの項目数（行数 * カラム数）を返却します。
print(csv_input.size)
# 指定したカラムだけ抽出したDataFrameオブジェクトを返却します。
print(csv_input[["date", "text"]]) 