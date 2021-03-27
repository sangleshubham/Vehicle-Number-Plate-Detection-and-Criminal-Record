# GET /v1/search/MH20BX4334 HTTP/1.1
# Host: jankari-api.loconav.com
# Connection: close
# jwt: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoVG9rZW4iOiJRVW1nV01VaGpOM1pFd191cEI5RSIsImxvZ2luSWQiOiIrOTE4NzY1Njc4ODc2IiwiaWF0IjoxNjE0NDMwMTcwLCJleHAiOjE2MTQ1MTY1NzB9.SWQbLrq8ewNoLSpju-Fl5cv5wIwQWiRPvwpIjxNvAFw
# User-Agent: Mozilla/5.0 (Linux; Android 10; Custom Phone_2 Build/QQ1D.200105.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.186 Mobile Safari/537.36
# loco nav
# 



#We have to generate AUTH token every time

import requests
import sys

def get_data(v_number):
    key = open("key" , 'r') 
    key = key.readline().strip()
    url = "https://jankari-api.loconav.com/v1/search/" + v_number
    headers = {'jwt': key}
    req = requests.get(url, headers=headers)
    print(req.content.decode("utf8"))
    if req.content.decode("utf8") == "Access Denied":
        print("inside if")
        data = requests.post("https://jankari-api.loconav.com/v1/login" , json={"authenticationToken":"r1qQvW6MDpMa4mFECokE"}).json()
        with open ("key",'w') as f:
            print(data['jwt'])
            f.write(data['jwt'])
    else : 
        return req.content.decode("utf8")