"""
@author: Amaljith c
"""
import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image, ImageOps
st.write("""
          # Malware Classification
          """
          )
upload_file = st.sidebar.file_uploader("Upload Malware greyScale Images")
Generate_pred=st.sidebar.button("Predict")
model=tf.keras.models.load_model('mal.h5')
def import_n_pred(image_data, model):
    image_data = np.asarray(image_data)
    #print(image_data.shape)
    img64=cv2.resize(image_data,(64,64))
    #print(img64.shape)
    ar=np.asarray([img64])
    #print(ar.shape)
    pred=model.predict(ar)
    size = (64,64)
    #image = ImageOps.fit(image_data, size)
    #image = ImageOps.grayscale(image)
    #img = np.asarray(image)
    #reshape=img[np.newaxis,...]
    #print(reshape)
    #pred = model.predict(reshape)
    return pred
if Generate_pred:
    image=Image.open(upload_file).convert("RGB")
    # print(image[...,:3].shape)
    # image=cv2.imread(image,cv2.IMREAD_COLOR)
    with st.expander('malware Image', expanded = True):
        st.image(image, width=350)#, use_column_width=True
    pred=import_n_pred(image, model)
    labels = ['1Ramnit','2Lollipop','3Kelihos_ver3','8Obfuscator','9Gatak','Adialer.C','Agent.FYI','Allaple.A','Allaple.L','Alueron.gen!J','Autorun.K','C2LOP.P',
              'C2LOP.gen!g','Dialplatform.B','Dontovo.A','Fakerean','Instantaccess','Lolyda.AA1','Lolyda.AA2','Lolyda.AA3','Lolyda.AT','Malex.gen!J','Obfuscator.AD',
              'Rbot!gen','Skintrim.N','Swizzor.gen!E','Swizzor.gen!I','VB.AT','Wintrim.BX','Yuner.A']
    st.title("Prediction:{0}".format(labels[np.argmax(pred)]))
