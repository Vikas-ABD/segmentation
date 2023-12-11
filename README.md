# License Plate Segmentation Using UNET in tensorflow

<div align="center">
<<<<<<< HEAD
    <img src="./app/static/Screenshot 2023-09-21 221428.png"/>
=======
  <img src="./app/static/Screenshot 2023-09-21 221428.png"/>
>>>>>>> d7db7ff57c0b8cf8237675ce64da398d6f547a84
</div>


<!-- The source code for [this](https://dev.to/andreygermanov/a-practical-introduction-to-object-detection-with-yolov8-neural-network-3n8c) article. -->

This is a web interface to [UNET Objection Segmentation Model](https://pyimagesearch.com/2022/02/21/u-net-image-segmentation-in-keras/) 
implemented on [Python](https://www.python.org) that uses a model to detect License Plate on images.

## Install

* Clone this repository: `git clone https://github.com/Vikas-ABD/Projects.git`
* Go to this folder Computer Vision using Deep Learning & Machine Learning/segmentation_using_UNET/LICENCE_PLATE_DETECTION_USING_UNET in Projects repository.
* Install dependencies by running `pip3 install -r requirements.txt`

## Run

Execute:

```
python app\flaskapp.py.py

```

It will start a webserver on http://localhost:5000. Use any web browser to open the web interface.

Using the interface you can upload the image to the object detector and see segmentation of all objects(License-plate) detected on it.
