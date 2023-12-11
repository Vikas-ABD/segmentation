from flask import Flask, render_template, request
import tensorflow as tf
import cv2
import numpy as np
from model import MultiUNet


app = Flask(__name__)

# Load your object detection model (e.g., saved model or TFLite model)
# Create an instance of the MultiUNet class
multi_unet = MultiUNet(n_classes=2, IMG_H=416, IMG_W=416, IMG_CHANNELS=3)

# Build the model
model = multi_unet.build_model()
model_path=r'C:\Users\VIKAS CHEIIURU\OneDrive\Documents\projects_of_vikas_chelluru\projects\Computer Vision using Deep Learning & Machine Learning\segmentation_using_UNET\LICENCE_PLATE_DETECTION_USING_UNET\model\test_final_200.hdf5'

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.load_weights(model_path)
target_size = (416, 416)

@app.route('/')
def index():
    return render_template('index.html', result_image=None)

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return "No image provided", 400

    image = request.files['image']
    if image.filename == '':
        return "No selected image", 400
    
   # Read the uploaded image and convert it to a numpy array
    image_data = np.frombuffer(image.read(), np.uint8)
    uploaded_image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

    # Resize the uploaded image to the target size
    resized_image = cv2.resize(uploaded_image, target_size) 
   
    resized_images1=[]
   
    resized_images1.append(resized_image)

    # Convert the list of resized images to a NumPy array
    test_img = np.array(resized_images1)

    # Expand the dimensions to (1, x, y, 3) to represent a single color image
    # Predict using the model
    y_pred = model.predict(test_img)
    y_pred_argmax = np.argmax(y_pred, axis=3)[0]

    # Create an RGB version of the predicted mask (assuming class labels)
    y_pred_rgb = np.zeros((y_pred_argmax.shape[0], y_pred_argmax.shape[1], 3), dtype=np.uint8)
    y_pred_rgb[y_pred_argmax == 0] = [0, 0, 0]         # Class 0 (background)
    y_pred_rgb[y_pred_argmax == 1] = [0, 255, 0]       # Class 1 (red)

    # Blend the original image with the segmented mask
    alpha = 0.6  # Adjust the alpha value for blending
    overlay = cv2.addWeighted(test_img[0], alpha, y_pred_rgb, 1 - alpha, 0)
    # Preprocess img (resize, normalize, etc.) as required by your model
    # Run inference with your model to detect objects
    # Post-process the results and annotate the image

    # For simplicity, we assume the result is stored in 'annotated_image'
    annotated_image = overlay # Replace with your actual result

    # Save the annotated image for displaying
    cv2.imwrite('app/static/result.jpg', annotated_image)

    return render_template('index.html', result_image='/static/result.jpg')

if __name__ == '__main__':
    app.run(debug=True)
