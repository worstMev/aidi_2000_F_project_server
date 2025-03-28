from fastapi import FastAPI,File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import keras 


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


    #load model : everything is on the level of run
    model = keras.model.load_model('./model/mood_model_i_600.keras')
    #get the prediction
    return "image uploaded"
