#storing all cropped images' names to a list
import subprocess
proc=subprocess.Popen('ls data/img_out/', shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
output=output.decode('utf-8').split('\n')
output=list(output)

from PIL import Image
from io import BytesIO
import requests
#image_name will be a list of all file names
#image_number will be the Number Plate content
image_name=[]
image_number=[]
# Replace <Subscription Key> with your valid subscription key for Microsoft Vision API.
subscription_key = "280c7bc04130439ab461e5ed4175c872"
assert subscription_key
vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
ocr_url = vision_base_url + "ocr?en&"
for x in output:
        image_url = x
        # print(x)
        image_data = open("data/img_out/" + image_url, "rb").read()
        
        headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
        params = {'language': 'unk', 'detectOrientation': 'true'}
        data = {'url': image_url}
        response = requests.post(ocr_url, headers=headers, params=params, data = image_data)
        print("Run till here")

        print(response.content)
        response.raise_for_status()

        analysis = response.json()
        line_infos = [region["lines"] for region in analysis["regions"]]
        word_infos = []
        for line in line_infos:
             for word_metadata in line:
                    for word_info in word_metadata["words"]:
                              word_infos.append(word_info)
        label=[]
        for word in word_infos:
              label.append(word["text"])
        image_number.append(label)
        image_name.append(image_url)