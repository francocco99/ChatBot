import json
with open('intents.json','r') as f:
    intent=json.load(f)
all_words=[]
tags=[]
xy=[]
print(intent)