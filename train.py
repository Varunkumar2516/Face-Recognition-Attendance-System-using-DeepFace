
# FOR Training WE are USIng LBPH algorithm 
#Local Binary Patterns Histograms
# for understadning the algorithm
#https://medium.com/data-science/face-recognition-how-lbph-works-90ec258c3d6b


import cv2
import os
import numpy as np
from tkinter import messagebox
from PIL import Image   # IMPORTANT

def Trainmodel():
    datadir = "DATA"
    path = [os.path.join(datadir, file) for file in os.listdir(datadir)]

    faces = []
    ids = []

    for image_path in path:
        # convert to grayscale
        img = Image.open(image_path).convert('L')
        imageNP = np.array(img, 'uint8')

        # extract ID
        id = int(os.path.split(image_path)[1].split(".")[1])

        faces.append(imageNP)
        ids.append(id)

        cv2.imshow("Training", imageNP)
        cv2.waitKey(1)

    ids = np.array(ids)

    # Train model
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)

    # Save model
    clf.save("Classifier.yml")

    cv2.destroyAllWindows()

    messagebox.showinfo("Success", "Training Complete ✅")