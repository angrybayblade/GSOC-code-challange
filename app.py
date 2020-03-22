from flask import Flask,request,send_from_directory,jsonify,render_template
from flask_cors import CORS
from base64 import b64encode
from utils import *

import tensorflow as tf
import cv2


sign = tf.saved_model.load(f"./checkpoints/saved_model")
model = sign.signatures['serving_default']

app = Flask(__name__,template_folder="./templates",static_folder="./templates/static/")
CORS(app)

mime ={"js":"javascript","css":"css"}

@app.route("/static/<string:file_type>/<string:file>",methods=['GET'])
def static_(file_type,file):
    return send_from_directory(f"./templates/static/{file_type}/",file,mimetype=f"text/{mime[file_type]}")

@app.route("/",methods=['GET'])
def index():
    return render_template("index.html",)

@app.route("/predict",methods=['POST','GET'])
def predict():
    image = request.files['image']
    name = image.filename
    image.save(f"./temp/{name}")
    type_ = int(request.form['type'])

    tensor,image = get_image(f"./temp/{name}")
    y,x,c = image.shape
    predictions = get_pred(tensor,model)
    boxes,classes = get_boxes(predictions,x,y,type_)

    if type_:
        image_data = None
        with open(f"./temp/{name}","rb") as image_rb:
            image_data = b64encode(image_rb.read())
        image_data = f"data:image/jpg;base64, {str(image_data,'utf-8')}"

        for i in boxes:
            i['render'] = True
        return jsonify({
                "boxes":boxes,
                "filename":f"./temp/{name}",
                "height":y,
                "width":x,
                "image":image_data,
                "name":name,
                "classes":classes
            })

    return jsonify({
                "boxes":boxes,
                "filename":f"./temp/{name}",
                "height":y,
                "width":x,
                "name":name
            })
    
@app.route("/test",methods=['GET','POST'])
def test():
    print (request.files)
    return "Hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0")