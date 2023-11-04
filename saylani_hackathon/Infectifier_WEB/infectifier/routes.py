from infectifier.forms import UserInput
from infectifier import app
from flask import render_template
from infectifier.predict import make_prediction
import secrets,os
from PIL import Image


def saveImage(imageFile):
    randomHax = secrets.token_hex(6)
    _,fileExtention = os.path.splitext(imageFile.filename)
    fileName = randomHax + fileExtention
    filePath = os.path.join(app.root_path,'static','prediction_images',fileName)
    temp_path = f'prediction_images/{fileName}'
    image = Image.open(imageFile)
    image.save(filePath)
    return filePath,temp_path

@app.route('/',methods=['GET','POST'])
def home():
    form = UserInput()
    result = None
    image = None
    show = False
    if form.imageFile.data:
        path,image = saveImage(form.imageFile.data)
        result = make_prediction(path)
        show = True
    return render_template('index.html', title='Infectifier', form=form, image=image, result=result, show=show)