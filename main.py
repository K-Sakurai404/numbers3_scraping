import json
import pprint
from collections import OrderedDict
import pandas as pd
import streamlit as st
import random

#jsonファイルにanalysisを書き込み
# analysis = {}

# for i in range(1000):
#     key = str(i).zfill(3)
#     analysis[key] = 0

# with open("info.json", "w") as f:
#     json.dump(analysis, f)

#jsonファイルを読み込み
file = open("number3.json", "r")
info = json.load(file)

df = pd.DataFrame()
lists = []
tousen_nums = []
the_number_of = []


for key in info.keys() :
    lists.append([key, info[key]])
    tousen_nums.append(key)
    the_number_of.append(info[key])

#pandasに当選番号の出現回数を当選番号をindex(行)として出力
df = pd.DataFrame(the_number_of, index=tousen_nums, columns=[""])

st.title("ナン◯ーズ3出現回数")
"""
### 第1回〜第2700回分

"""
st.write(
    "出現回数"
)
st.dataframe(df)

st.bar_chart(df)

st.line_chart(df)

st.area_chart(df)
