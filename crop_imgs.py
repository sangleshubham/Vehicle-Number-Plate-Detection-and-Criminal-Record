import pandas as pd
import json
import subprocess
import os
import requests
import json
import re


def website_method():
    # import requests
    from bs4 import BeautifulSoup

    proc=subprocess.Popen('ls ./data/img/', shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]
    output=output.decode('utf-8').split('\n')
    output=list(output)
    print(output)
    for loc in output:
        location = ""
        # proxies=proxies , verify=False ,
        # proxies = {"http": "http://160.119.54.12:8080", "https": "http://160.119.54.12:8080"}
        headers = {'Referer': 'https://google.com/index'}
        with open("./data/img/" + loc , 'rb') as f:
            location = requests.post("https://app.platerecognizer.com/alpr-demo" , files={"upload":f} , allow_redirects=False, headers=headers).headers['Location'] 

        data = requests.get("https://app.platerecognizer.com" + location ).content


        regex = "[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}[0-9]{4}"

        plates = re.findall(regex , str(data))
        if plates == []:
            pass
        else:
            return plates[0]
        # return false if plates == [] else plates[0]

# ./darknet detector test data/obj.data cfg/yolo-obj.cfg backup/yolo-obj_final_vehicle.weights -ext_output -dont_show -out result.json < data/valid2.txt

def algo_method():
    proc=subprocess.Popen('ls ./data/img/', shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]
    output=output.decode('utf-8').split('\n')
    output=list(output)

    with open("img_list.txt" , "w") as f :
        for u_img in output:
            if u_img != "":
                print("data/img/" + u_img)
                f.write("data/img/" + u_img + "\n")


    proc=subprocess.call('./darknet detector test data/obj.data cfg/yolo-obj.cfg backup/yolo-obj_final_vehicle.weights -ext_output -dont_show -out result.json < img_list.txt', shell=True, stdout=subprocess.PIPE, )

    print("process completed")

    #loading results of YOLOv3 Detection
    with open('./result.json') as file:
        data = json.load(file)
    df = pd.DataFrame(data)

    med=[]
    def check(x):
        for y in x:
            if y['name']=="NumberPlate":
                        return True
        return False
    df['plates']=df['objects'].transform(lambda temp:check(temp))

    df=df[df['plates']]



    proc=subprocess.Popen('ls ./data/img/', shell=True, stdout=subprocess.PIPE, )
    output=proc.communicate()[0]
    output=output.decode('utf-8').split('\n')
    output=list(output)

    med=[]
    def check2(x):
        for y in x:
            if y['name']=="NumberPlate":
                        return y
        return False
    df['plate_data']=df['objects'].transform(lambda temp:check2(temp))

    df=df.drop(['frame_id','objects','plates'],axis=1)

    data=df


    def details(x,flag_2):
            co=x['relative_coordinates']
            wid=float(co['width'])/2.0
            hi=float(co['height'])/2.0
            if flag_2=='y2':
                return float(co['center_y'])+hi
            if flag_2=='x2':
                return float(co['center_x'])+wid
            if flag_2=='x1':
                return float(co['center_x'])-wid
            if flag_2=='y1':
                return float(co['center_y'])-hi
    data['x1']=data['plate_data'].transform(lambda f:details(f,'x1'))    
    data['y1']=data['plate_data'].transform(lambda f:details(f,'y1'))  
    data['x2']=data['plate_data'].transform(lambda f:details(f,'x2'))  
    data['y2']=data['plate_data'].transform(lambda f:details(f,'y2'))  


    out_img_list = []

    from PIL import Image
    count=0
    for x,y in data.iterrows():
            img = Image.open(str(y['filename']))
            dim=img.size
            w,h=dim[0],dim[1]
            x1=y['x1']*w
            x2=y['x2']*w
            y1=y['y1']*h
            y2=y['y2']*h
            area=(x1,y1,x2,y2)
            print(count)
            cropped_img = img.crop(area)
            cropped_img=cropped_img.convert('RGB')
            cropped_img.save("./data/img_out/"+str(x)+'.jpg')
            out_img_list.append("./data/img_out/"+str(x)+'.jpg')
            count+=1


    api_key = "36299de6aa88957"
    ocr_resp = []
    for img in out_img_list:
        payload = {'isOverlayRequired': 'true',
                    'apikey': api_key,
                    'language': 'eng',
                    'OCREngine':'2',
                    }
        with open(img, 'rb') as f:
            r = requests.post('https://api.ocr.space/parse/image',
                                files={img: f},
                                data=payload,
                                ).content
            
            resp = json.loads(r)
            string = ""
            for char in resp["ParsedResults"][0]["ParsedText"]:
                if char.isdigit() or char.isalpha():
                    string += char
            if re.match("[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}[0-9]{4}" , string):
                return string
