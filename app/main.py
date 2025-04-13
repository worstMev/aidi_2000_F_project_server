from fastapi import FastAPI,File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import numpy as np
import keras 
import cv2


origins_all = '*';
app = FastAPI();

app.add_middleware(
        CORSMiddleware,
        allow_origins = origins_all,
        allow_credentials = True,
        allow_methods=['*'],
        allow_headers=['*']
        )

@app.get('/')
def root() :
    return 'server works';

@app.post('/upload')
async def upload_image (image : UploadFile):
    print('upload image')
    name_pic = 'image/pic.png'
    blob = await image.read()
    with open(name_pic,'wb') as file:
        file.write(blob)

    #preprocess the image (size)
    data_input = image_resize(img_name=name_pic)

    #load model : everything is on the level of run
    model = keras.saving.load_model('./model/mood_model_i_600.keras')
    #model = keras.saving.load_model('./model/mood_model_i_600_tf_400.keras')
    #model = keras.saving.load_model('./model/mood_model_i_600_no_tl_10e_08.keras')
    #get the prediction

    res = np.round( model.predict(data_input));
    res = str(int(res[0][0]))

    classes = {
            '0' : 'positive vibe',
            '1' : 'negative vibe'
            }
    return f"There's {classes.get(res)} in that picture."



def image_resize(img_name,dimension=(600,600)):
     #load
    image = Image.open(img_name)
    image = np.asarray(image)
    #resize
    resized_img = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
    dim_3d = list(dimension)
    dim_3d.append(3)
    dim_3d = tuple(dim_3d)
    resized_img = np.resize(resized_img, dim_3d)
    data_input = np.asarray([resized_img])
    return data_input

