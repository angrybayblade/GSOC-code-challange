rm -rf checkpoints
wget http://download.tensorflow.org/models/object_detection/mask_rcnn_inception_v2_coco_2018_01_28.tar.gz
tar xvf mask_rcnn_inception_v2_coco_2018_01_28.tar.gz
mv mask_rcnn_inception_v2_coco_2018_01_28 checkpoints
echo "Delete The Tar file if you don\'t need it"