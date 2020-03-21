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
    "boxes":[
        {
            "class":"Car",
            "score":0.9998185038566589,
            "xmax":604,
            "xmin":488,
            "ymax":336,
            "ymin":255
        },
        {
            "class":"Tree",
            "score":0.962854266166687,
            "xmax":284,
            "xmin":178,
            "ymax":408,
            "ymin":339
        },
        {
            "class":"Bird",
            "score":0.9942442774772644,
            "xmax":236,
            "xmin":48,
            "ymax":74,
            "ymin":2
        },
        {
            "class":"Ship",
            "score":0.9564193487167358,
            "xmax":86,
            "xmin":4,
            "ymax":191,
            "ymin":136
        }
    ],
    "filename":"./temp/BloodImage_00001.jpg",
    "height":480,
    "width":640,
    "name":"BloodImage_00001.jpg"
}
```

**Note** : Use type=1 in request when you want the JPEG file as BASE64 string in Response