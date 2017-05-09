import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
from PIL import Image
import types
import os
import time

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '7278d09a54b742d7899a63d97345dc12',
}

rule = {'disgust':0,'sadness':1,'neutral':2,'happiness':3,'fear':4,'contempt':5,'surprise':6,'anger':7}

params = urllib.parse.urlencode({
})

out=open("result.txt","w+")


conn = http.client.HTTPSConnection('api.cognitive.azure.cn')
for testLabel in os.listdir(r"./tmp"):
    try:
        label = rule[testLabel]
        print(testLabel)
        for filename in os.listdir(r"./tmp/" + testLabel):
            restr = ""
            restr += testLabel + "/" + filename
            restr += "\tLabel\t" + str(rule[testLabel])
            body = open(r"./tmp/" + testLabel + "/" + filename, mode='rb')
            time.sleep(26)
            try:
                time1 = time.time()
                conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
                time2 = time.time()
                response = conn.getresponse()
                time3 = time.time()
                data = response.read()
                jsonRes = json.loads(data.decode())
                lenRes = len(jsonRes)
                restr += "\tTime21\t" + str(time2 - time1)
                restr += "\tTime32\t" + str(time3 - time2)
                i = 1
                restr += "\tResult\t"
                for j in jsonRes:
                    if type(j) == type({}):
                        if 'scores' in j:
                            scores = j['scores']
                            maxRes = max(scores, key=lambda key: scores[key])
                            restr += "\t" + str(rule[maxRes])
                            i += 1
                        else:
                            continue
                    else:
                        continue
                restr += "\n"
                print(restr)
                out.write(restr)
            except Exception as e1:
                print("Error in",e1)
                continue
    except Exception as e2:
        print("Error out",e2)
        continue

conn.close()


