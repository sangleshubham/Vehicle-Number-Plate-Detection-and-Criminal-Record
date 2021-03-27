import requests
import json
import re
api_key = "36299de6aa88957"
ocr_resp = []



payload = {'isOverlayRequired': 'true',
            'apikey': api_key,
            'language': 'eng',
            'OCREngine':'2',
            }
with open("data/img_out/1.jpg", 'rb') as f:
    r = requests.post('https://api.ocr.space/parse/image',
                        files={"img": f},
                        data=payload,
                        ).content
    resp = json.loads(r)
    print(resp)
    string = ""
    for char in resp["ParsedResults"][0]["ParsedText"]:
        if char.isdigit() or char.isalpha():
            string += char
            print(string)
    if re.match("[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}[0-9]{4}" , string):
        print( string)