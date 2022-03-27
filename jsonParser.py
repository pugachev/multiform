import requests
import json
from bs4 import BeautifulSoup
from PIL import Image
import io
import re

with open('Journal.json', encoding="utf-8") as f:
    value = json.load(f)
    #print(value["entries"][0]["text"])
    #print(value["entries"][1])
    #print(value["entries"][2]["text"])
    #print(len(value["entries"]))
    
    pattern = '\d{4}-\d{2}-\d{2}'
    
    for index in range(len(value["entries"])):
     if value["entries"][index]["text"] is None:
      print("データなし")
     else:
      print(str(index)+" : "+str(re.match(pattern,value["entries"][index]["creationDate"]).group())+" "+value["entries"][index]["text"])