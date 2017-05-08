import json
import types
import operator
fp = open('result.json')
try:
     str = fp.read()
     jsonRes = json.loads(str)
     lenRes = len(jsonRes)
     for j in jsonRes:
          scores = j['scores']
          # disgust = scores['disgust']
          # sadness = scores['sadness']
          # neutral = scores['neutral']
          # happiness = scores['happiness']
          # fear = scores['fear']
          # contempt = scores['contempt']
          # surprise = scores['surprise']
          # anger = scores['anger']
          maxRes = max(scores, key=lambda key: scores[key])
          print(maxRes)
finally:
     fp.close()