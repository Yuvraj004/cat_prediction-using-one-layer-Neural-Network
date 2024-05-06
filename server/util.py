import json
import pickle
import numpy as np
import copy
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage

from artifacts.lr_utils import load_dataset

image = None
cat_model = None
num_px = 60
def sigmoid(z):
    s = 1/(1+ np.exp((-1)*z))
    return s
def predict(w, b, X):

    
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)

    A =sigmoid( np.dot(w.T,X) + b)

    for i in range(A.shape[1]):

        if A[0][i] > 0.5 :
            Y_prediction[0][i] = 1
        else:
            Y_prediction[0][i] = 0
    
    return Y_prediction

def predict_cat(cat_image):
    # change this to the name of your image file
    my_image = cat_image  or "my-image.jpg"  
    train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
    # We preprocess the image to fit your algorithm.
    fname = "../images/" + my_image
    image = np.array(Image.open(fname).resize((num_px, num_px)))
    plt.imshow(image)
    image = image / 255.
    image = image.reshape((1, num_px * num_px * 3)).T
    my_predicted_image = predict(cat_model["w"], cat_model["b"], image)

    str = "y = " + str(np.squeeze(my_predicted_image)) + ", your algorithm predicts a \"" + classes[int(np.squeeze(my_predicted_image)),].decode("utf-8") +  "\" picture."
    print("y = " + str(np.squeeze(my_predicted_image)) + ", your algorithm predicts a \"" + classes[int(np.squeeze(my_predicted_image)),].decode("utf-8") +  "\" picture.")
    return str


def load_saved_artifacts():
    global cat_model
    global image
    global num_px
    with open('./artifacts/cat_prediction_model.pickle','rb') as f:
        cat_model = pickle.load(f)
    

if __name__=="__main__":
    # load_saved_artifacts()
    # print(get_location_names())
    print("util func")