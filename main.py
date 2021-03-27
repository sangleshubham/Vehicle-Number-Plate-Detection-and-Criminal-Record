import crop_imgs
import flask
import vehicle_info
from flask import jsonify

from flask import Flask
app = Flask(__name__)


@app.route('/')
def get_user_data():
    number_plate = crop_imgs.website_method()
    if number_plate == None :
        al_no = crop_imgs.algo_method()
        if al_no == None : 
            return "Number Plate not found"
        else :
            return str(vehicle_info.get_data(al_no))
    else:
        return vehicle_info.get_data(number_plate)

if __name__ == '__main__':
    app.run()





