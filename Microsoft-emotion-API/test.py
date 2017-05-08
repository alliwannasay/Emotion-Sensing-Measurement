import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
from PIL import Image
import types
headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '7278d09a54b742d7899a63d97345dc12',
}

params = urllib.parse.urlencode({
})

body = open('./tmp/anger/7.jpg', mode='rb')
# body = "{ \"url\": \"http://feeling.com.mx/img/2011/12/Adele-Set-Fire-To-The-Rain.jpg\"}"

try:
    conn = http.client.HTTPSConnection('api.cognitive.azure.cn')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body , headers)
    response = conn.getresponse()
    data = response.read()
    # print(data)
    jsonRes = json.loads(data.decode())
    lenRes = len(jsonRes)
    for j in jsonRes:
        scores = j['scores']
        maxRes = max(scores, key=lambda key: scores[key])
        print(maxRes)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

