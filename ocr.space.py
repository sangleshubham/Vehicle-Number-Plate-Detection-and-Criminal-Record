import requests
import re


# url = "https://ocr.space/Scripts/OCR/jquery-ocr-starter.js"

# data = requests.get(url).content

# data = str(data)
# print(data)

# key = re.findall("apikey'.*'" , data)
# print(key)
# key = key[0][11:-1]

# key = "5a64d478-9c89-43d8-88e3-c65de9999580"

# url_ocr = "https://api8.ocr.space/parse/image"

# file = open("data/img_out/0.jpg", 'rb')
# headers = {'apikey': key }
# payload = {'url':'https://america.cgtn.com/wp-content/uploads/2018/11/DIGITAL-LICENSE-PLATES-digi.00_02_40_14.Still003-770x433.jpg' , 'language':'eng' , 'isOverlayRequired':'true' , "FileType":".Auto" , 'IsCreateSearchablePDF':'false', 'isSearchablePdfHideTextLayer':'true' , 'detectOrientation':'false' , 'isTable':'false' , 'scale':'false' , 'OCREngine':'2' , 'detectCheckbox':'false' , 'checkboxTemplate':'0'}
# proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
# session = requests.session()
# print(requests.post(url='https://api8.ocr.space/parse/image' , headers=headers , files=payload , proxies=proxies, verify=False).content) 


api_key = "36299de6aa88957"

ocr_resp = []
payload = {'isOverlayRequired': 'true',
            'apikey': api_key,
            'language': 'eng',
            'OCREngine':'2',
            }
filename = "data/img_out/1.jpg"
with open(filename, 'rb') as f:
    r = requests.post('https://api.ocr.space/parse/image',
                        files={filename: f},
                        data=payload,
                        )

ocr_resp.append(r.content.decode())

print(ocr_resp)

# import json


# resp = '{"ParsedResults":[{"TextOverlay":{"Lines":[{"LineText":"HRZECFSR68","Words":[{"WordText":"HRZECFSR68","Left":-1.0,"Top":5.0,"Height":43.0,"Width":67.0}],"MaxHeight":43.0,"MinTop":5.0}],"HasOverlay":true,"Message":"Total lines: 1"},"TextOrientation":"0","FileParseExitCode":1,"ParsedText":"HRZECFSR68","ErrorMessage":"","ErrorDetails":""}],"OCRExitCode":1,"IsErroredOnProcessing":false,"ProcessingTimeInMilliseconds":"328"}'
# resp = json.loads(resp)


# # for resp in ocr_resp:
# print(resp["ParsedResults"][0]["ParsedText"])
