# Cancer Region of Interest Extraction and Machine Learning

### Abstract / Project Summary:

    Currently caMicroscope provides functionality to upload and view high resolution medical images with simplified web interface. It also provides a separate feature to detect and visualize different objects in images. Currently it uses Tensorflow.js to detect bounding boxes which makes it less flexible to perform tasks such as finding mask segmentations and visualize them. Also tensorflow.js lacks a lot of functionality compared to main tensorflow framework.

---

### Student Details

**Name** : Viraj Patel

**Email** : vptl185@gmail.com

**Slack Username** : Viraj

**Timezone** : IST (india)

---

### Potential Mentors

**Insiyah Hajoori and Ryan Birmingham**

---

### Personal Background

    I'm a Third Year Computer Science Student from Lovely Professional University, Punjab, India. I love data science and deep learning and do them as passion. I have experience in data analytics, predictive modeling and computer vision. 

#### Projects 

| Project | Description | 
|---------|-------------|
| One Shot Learning For Face Recognition | Implememted Siamese Netowrk With Tensorflow to create a face verfification service |
| Blood ROI Extraction and Cell Classification | Neural Network Trained With Tensorflow Object Detection API to extract Region Of Interest and classify blood cells. |
| Handwritten Bengali Grapheme Classifier | Created Image Classification Classification Pipeline with 97% accuracy for kaggle's Bengaliai-cv19 challange. |
| Transfer PI | A Client Server Pair for downloading, uploading and sharing data with CLI |

#### Skills

+ Programming
  + Python
  + JavaScript

+ Frameworks
  + Numpy,Pandas,Matplotlib
  + OpenCV, skimage
  + Tensorflow
  + scikit-learn
  + Flask
  + ReactJS,Router

---

### Project Goals / Major Contributions

+ I intent to upgrade current architecure to predict both bounding boxes and a mask for segmentation. Also i'll try to create light weight object detection and classificstion pipeline, as implementing currently available object detection neural network architectures such as RCNN or YOLO may lead to a large number of weights and very high memory and time consuming runtime inferences.
 
+  Also having such big architectures with very large amount of weights may be prone to overfitting and may require so much time to train on new data. Also to use tensorflow.js we need a architecture as light weight as possible as tensorflow.js uses local runtime and user's computational power and we need to send weights everytime with the web application.

#### Implementation Plan

This plan consists of four steps.

1. Collection Data For Training and creating a proper input format
2. Developing A Object detection and segmentation Pipeline
3. Deploying Pipeline using a REST API
4. Designing a simplified Web Interface for users

#### Deliverables
1. Cancer Region Extractor And Classification Pipeline
2. REST API With Image Classification And ROI Extraction
3. Single Page Web Application (React JS)
4. Documentation And Tests for above implementations.

---

### Project Schedule

| **Community Bonding Period** - *(April 27,2020 - May 18, 2020)*
  1. Community Bonding
  2. Getting familiar with caMicroscope.
  3. Getting familiar with mentors ans caMicroscope team.
  
| **Start Of Development Phase** - *(May 19,2020 - May 29,2020)*
  1. Discussion Of Feature implementation with mentors.
  2. Data Collection and labeling the data.
  3. Deciding Which technologies/frameworks to use.
  4. Designing Web Application UI.

| **Designing and Implementing Architecture** - *(May 29,2020 - June 15,2020)*
  1. Neural Network Architecture Design. 
  2. Data Pipeline Design.
  3. Implementation In Python.
   
| **Phase 1 Submission** - *(June 15,2020 - June 18,2020)*
  1. Phase 1 Evaluation.
  2. Code Review with mentors.

| **Training And Testing Network** - *(June 19,2020 - July 5,2020)*
  1. Data Input Pipeline Creation
  2. Training And Testing Network
  3. Evaluating And Hyperparameter Tuning

| **Deploying Trained Network** - *(July 5,2020 - July 12,2020)*
  1. Freezing Network Inference Graph and Implement the pipeline.
  2. Converting Weights To tensorflow.js config files.
  3. Deploying Network Using Flask for API services.

| **Phase 2 Submission** - *(July 13,2020 - July 16,2020)*
  1. Phase 1 Evaluation.
  2. Code Review with mentors.

| **Developing Web UI** - *(July 16,2020 - July 31,2020)*
  1. Implementing UI.
  2. Coverting Into Single Page Application.
  3. Building Deployable Pages.

| **Testing And Documenting** - *(August 1,2020 - August 9,2020)*
  1. Creating Tests For Application.
  2. Writing User Guides and API Documentation.
  3. Testing The Final Application.

| **Code Submission And Final Evaluation** - *(August 10,2020 - August 17,2020)*
  1. Final Evaluation

---

### Planned GSoC work hours

| Day | Coordinated Universal Time | Indian Standard Time | Total Time |
|-----|----------------------------|----------------------|------------|
| Week Days | 08:30 AM - 12:30 PM| 02:00 PM - 06:00 PM | 4 Hours |
| Week Days | 03:30 PM - 09:30 PM| 09:00 PM - 03:00 AM | 6 Hours |
| Weekends  | 08:30 AM - 08:30 PM| 02:00 PM - 02:00 AM | 12 Hours |

---

###  Planned absence/vacation days

    Since the whole COVID - 19 situation i may have my lectures and examination during summer so my work hours may fluctuate for about 1 - 2 hours. Except for that i have plan for any vacation or absence.

---

###  Skill Set

    Most of the online courses i have done are free, such as Deep Learning From MIT Open Coursewere, Comuter Vision Course From Udacity and  Convolutional Neural Networks for Visual Recognition (cs231n) from Stanford's online courses. I've learned most of the frameworks from documentations.

    I have experience with Both Python and Javascript. I've been using tensorflow as my go to Deep Learning tool. I have developed several neural networks and image processing pipelines with Python, Tensorflow, OpenCV and scikit-image.

    For my code challange i've developed a single page application to upload images and perform mask segmentation. I've used Mask RCNN Implementation by tensorflow,Google. It is trained on MSCOCO dataset and can detect and classify 90 different classes.

    I created a single page application with ReactJS and a API service that uses Flask to deploy the web app. Link to the code challange

    > https://github.com/code-kage/GSOC-code-challange