import cv2
import tensorflow as tf
import numpy as np
from base64 import b64encode

classes = {1: {'id': 1, 'name': 'person', 'color': (243, 71, 204)},
 2: {'id': 2, 'name': 'bicycle', 'color': (187, 8, 48)},
 3: {'id': 3, 'name': 'car', 'color': (46, 106, 246)},
 4: {'id': 4, 'name': 'motorcycle', 'color': (128, 241, 74)},
 5: {'id': 5, 'name': 'airplane', 'color': (21, 37, 89)},
 6: {'id': 6, 'name': 'bus', 'color': (126, 149, 51)},
 7: {'id': 7, 'name': 'train', 'color': (144, 189, 122)},
 8: {'id': 8, 'name': 'truck', 'color': (199, 213, 141)},
 9: {'id': 9, 'name': 'boat', 'color': (73, 207, 213)},
 10: {'id': 10, 'name': 'traffic light', 'color': (156, 154, 217)},
 11: {'id': 11, 'name': 'fire hydrant', 'color': (31, 91, 45)},
 13: {'id': 13, 'name': 'stop sign', 'color': (184, 18, 49)},
 14: {'id': 14, 'name': 'parking meter', 'color': (244, 150, 83)},
 15: {'id': 15, 'name': 'bench', 'color': (115, 18, 14)},
 16: {'id': 16, 'name': 'bird', 'color': (5, 137, 167)},
 17: {'id': 17, 'name': 'cat', 'color': (147, 36, 234)},
 18: {'id': 18, 'name': 'dog', 'color': (14, 221, 108)},
 19: {'id': 19, 'name': 'horse', 'color': (62, 131, 192)},
 20: {'id': 20, 'name': 'sheep', 'color': (93, 140, 239)},
 21: {'id': 21, 'name': 'cow', 'color': (54, 92, 222)},
 22: {'id': 22, 'name': 'elephant', 'color': (152, 138, 138)},
 23: {'id': 23, 'name': 'bear', 'color': (69, 43, 195)},
 24: {'id': 24, 'name': 'zebra', 'color': (188, 227, 186)},
 25: {'id': 25, 'name': 'giraffe', 'color': (202, 240, 180)},
 27: {'id': 27, 'name': 'backpack', 'color': (163, 153, 116)},
 28: {'id': 28, 'name': 'umbrella', 'color': (65, 34, 124)},
 31: {'id': 31, 'name': 'handbag', 'color': (6, 181, 57)},
 32: {'id': 32, 'name': 'tie', 'color': (94, 126, 146)},
 33: {'id': 33, 'name': 'suitcase', 'color': (136, 220, 122)},
 34: {'id': 34, 'name': 'frisbee', 'color': (31, 159, 40)},
 35: {'id': 35, 'name': 'skis', 'color': (150, 119, 42)},
 36: {'id': 36, 'name': 'snowboard', 'color': (159, 10, 32)},
 37: {'id': 37, 'name': 'sports ball', 'color': (22, 204, 8)},
 38: {'id': 38, 'name': 'kite', 'color': (40, 71, 50)},
 39: {'id': 39, 'name': 'baseball bat', 'color': (233, 117, 71)},
 40: {'id': 40, 'name': 'baseball glove', 'color': (204, 111, 100)},
 41: {'id': 41, 'name': 'skateboard', 'color': (97, 56, 39)},
 42: {'id': 42, 'name': 'surfboard', 'color': (76, 238, 223)},
 43: {'id': 43, 'name': 'tennis racket', 'color': (4, 115, 192)},
 44: {'id': 44, 'name': 'bottle', 'color': (46, 67, 224)},
 46: {'id': 46, 'name': 'wine glass', 'color': (173, 222, 235)},
 47: {'id': 47, 'name': 'cup', 'color': (139, 250, 27)},
 48: {'id': 48, 'name': 'fork', 'color': (102, 148, 78)},
 49: {'id': 49, 'name': 'knife', 'color': (40, 54, 141)},
 50: {'id': 50, 'name': 'spoon', 'color': (246, 152, 216)},
 51: {'id': 51, 'name': 'bowl', 'color': (251, 74, 56)},
 52: {'id': 52, 'name': 'banana', 'color': (60, 115, 26)},
 53: {'id': 53, 'name': 'apple', 'color': (66, 104, 253)},
 54: {'id': 54, 'name': 'sandwich', 'color': (53, 249, 48)},
 55: {'id': 55, 'name': 'orange', 'color': (184, 220, 102)},
 56: {'id': 56, 'name': 'broccoli', 'color': (75, 80, 223)},
 57: {'id': 57, 'name': 'carrot', 'color': (76, 138, 53)},
 58: {'id': 58, 'name': 'hot dog', 'color': (200, 115, 36)},
 59: {'id': 59, 'name': 'pizza', 'color': (38, 135, 37)},
 60: {'id': 60, 'name': 'donut', 'color': (187, 191, 154)},
 61: {'id': 61, 'name': 'cake', 'color': (118, 131, 92)},
 62: {'id': 62, 'name': 'chair', 'color': (187, 219, 161)},
 63: {'id': 63, 'name': 'couch', 'color': (104, 111, 100)},
 64: {'id': 64, 'name': 'potted plant', 'color': (203, 85, 237)},
 65: {'id': 65, 'name': 'bed', 'color': (119, 34, 19)},
 67: {'id': 67, 'name': 'dining table', 'color': (243, 250, 252)},
 70: {'id': 70, 'name': 'toilet', 'color': (243, 153, 133)},
 72: {'id': 72, 'name': 'tv', 'color': (187, 193, 75)},
 73: {'id': 73, 'name': 'laptop', 'color': (231, 214, 152)},
 74: {'id': 74, 'name': 'mouse', 'color': (199, 128, 25)},
 75: {'id': 75, 'name': 'remote', 'color': (212, 17, 164)},
 76: {'id': 76, 'name': 'keyboard', 'color': (109, 18, 90)},
 77: {'id': 77, 'name': 'cell phone', 'color': (151, 185, 225)},
 78: {'id': 78, 'name': 'microwave', 'color': (154, 181, 233)},
 79: {'id': 79, 'name': 'oven', 'color': (8, 185, 171)},
 80: {'id': 80, 'name': 'toaster', 'color': (116, 7, 52)},
 81: {'id': 81, 'name': 'sink', 'color': (204, 242, 167)},
 82: {'id': 82, 'name': 'refrigerator', 'color': (17, 182, 172)},
 84: {'id': 84, 'name': 'book', 'color': (26, 171, 180)},
 85: {'id': 85, 'name': 'clock', 'color': (9, 189, 210)},
 86: {'id': 86, 'name': 'vase', 'color': (169, 154, 252)},
 87: {'id': 87, 'name': 'scissors', 'color': (87, 44, 90)},
 88: {'id': 88, 'name': 'teddy bear', 'color': (251, 106, 120)},
 89: {'id': 89, 'name': 'hair drier', 'color': (98, 67, 144)},
 90: {'id': 90, 'name': 'toothbrush', 'color': (107, 71, 221)}}


def get_pred(tensor,model):
    output_dict = model(tensor)
    output_dict.pop("num_detections")
    for i in output_dict.keys():
        output_dict[i] = output_dict[i].numpy()
    return output_dict

def get_image(path):
    image = cv2.imread(path)
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis,...]
    return input_tensor,image

def get_boxes(out,x,y,type_):
    boxes = []
    clss = []
    for box,cls,mask,score in zip(*[out[i][0] for i in sorted(out.keys())]):
        if score > 0.75:
            box = {
                "mask":None,
                "class":classes[cls]['name'],
                "score":float(score),
                "box":{
                    "ymin":int(box[0]*y),
                    "xmin":int(box[1]*x),
                    "ymax":int(box[2]*y),
                    "xmax":int(box[3]*x)
                },
                "box_color":'#%02x%02x%02x' % classes[cls]['color']
            }
            h = box['box']['ymax'] - box['box']['ymin']
            w = box['box']['xmax'] - box['box']['xmin']
            mask = cv2.resize(mask,(w,h),interpolation = cv2.INTER_NEAREST)
            if type_:
                x_,y_ = np.where(mask > 0.15)
                cords = [[int(i[0]),int(i[1])] for i in zip(x_,y_)]
                rect = []
                for y_,x_ in cords:
                    rect.append(f"""<rect y={y_} x={x_} height="1px" width="1px" fill={box['box_color']} opacity="0.5" ></rect>""")
                svg = f"""<svg height="{h}px" width="{w}px"> {"".join(rect)} </svg>"""
                box['mask'] = svg
            else:
                box['mask'] = mask.astype(float).tolist()
            boxes.append(box)                     
            clss.append(int(cls))
    clss = [
            {
                "name":classes[i]['name'],
                "color":'#%02x%02x%02x' % classes[i]['color'],
                "render":True
            } 
            for i in set(clss)
        ]
    return [i for i in boxes if i['score'] > 0.75],clss

