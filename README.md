## GSOC Coding Challange For caMicroscope

**tested on**
+ OS : Ubuntu 18.06 (Pop OS)
  
+ Python : 3.6

+ Tensorflow : 2.0.0beta0

+ Opencv : 4.0.2

+ CUDA 10.1

+ cuDNN : 7.6
  
**Inference Time**

> Prediction : ~ 3 - 6 seconds

> Mask Rendering : ~ 5 - 9 seconds

*Tested on Nvidia GTX 1060 6GB*

**installation and setup**

```bash
 pip3 install -r requirements.txt
```

**For GPU User**

```bash
pip3 install -r requirements-gpu.txt
``` 
 then

```bash
chmod +x download_model.sh && ./download_model.sh

python3 app.py
```

Now Open Web Interface at http://localhost:5000 to use web UI.

To Use API use Following Command : 

```bash
curl -X GET\
    -F "image=@/path/to/file.jpg" \
    -F "type=0" \
    http://localhost:5000/predict
```

And It Will return JSON object as following 

```json
{
    "boxes": [
        {
            "box": {
                "xmax": 217,
                "xmin": 121,
                "ymax": 452,
                "ymin": 384
            },
            "box_color": "#0edd6c",
            "class": "dog",
            "mask":[[],[],[]],
            "score": 0.9936468601226807
        },
        {
            "box": {
                "xmax": 102,
                "xmin": 58,
                "ymax": 194,
                "ymin": 125
            },
            "box_color": "#09bdd2",
            "class": "clock",
            "mask":[[],[],[]],
            "score": 0.9722564220428467
        },
        {
            "box": {
                "xmax": 354,
                "xmin": 218,
                "ymax": 443,
                "ymin": 276
            },
            "box_color": "#cb55ed",
            "class": "potted plant",
            "mask":[[],[],[]],
            "score": 0.8766565322875977
        }
    ],
    "filename": "./temp/6.jpg",
    "height": 479,
    "name": "6.jpg",
    "width": 639
}
```

Response will we a JSON String. Return Values Will Be As Following 

+ filename (String):
  +  Path Of the uploaded file on server.

+ height (Integer):
  +  height of the uploaded file.

+ width (Integer): 
  + width of the uploaded file.
  
+ name (String):
  + Name Of the uploaded file.

+ boxes (Array): 
  + Array Containing Detected Objects.
    + box (Dictionary)
      + Dictionary containing co-ordinates of detected object.
    + box_color (String)
      + A unique color assigned to the object class.
    + mask (Array)
      + A 2-dimentional array containing mask for detected object.
    + class (String)
      + Name Of The detected class.
    + score (Floating Point Number)
      + Score of the detection class.

**Note** : Use type=1 in request when you want the JPEG file as BASE64 string in Response