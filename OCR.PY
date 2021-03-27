import requests

imgpath = "data/img_out/0.jpg"

with open(imgpath , 'rb') as f:
    print (requests.post("https://app.platerecognizer.com/alpr-demo" , files={"imgpath":f}, ).content )


