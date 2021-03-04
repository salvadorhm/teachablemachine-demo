import web
import app
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

class Ml():

    def machineLerning(self,file):
        try:
            # Disable scientific notation for clarity
            np.set_printoptions(suppress=True)

            # Load the model
            model = tensorflow.keras.models.load_model('keras_model.h5')

            # Create the array of the right shape to feed into the keras model
            # The 'length' or number of images you can put into the array is
            # determined by the first position in the shape tuple, in this case 1.
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            # Replace this with the path to your image
            image = Image.open(file)

            #resize the image to a 224x224 with the same strategy as in TM2:
            #resizing the image to be at least 224x224 and then cropping from the center
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.ANTIALIAS)

            #turn the image into a numpy array
            image_array = np.asarray(image)

            # display the resized image
            # image.show()

            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

            # Load the image into the array
            data[0] = normalized_image_array

            # run the inference
            prediction = model.predict(data)

            for i in prediction:
                if i[0] > 0.8:
                    return "mouse"
                elif i[1] > 0.8:
                    return "keyboard"
        except Exception as error:
            return "Error"

    def POST(self):
        try:
            form = web.input(photo={})
            result ={}
            filedir = 'static/jpg' # change this to the directory you want to store the file in.
            if 'photo' in form: # to check if the file-object is created
                filepath = form.photo.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
                filename = filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
                # fout = open( filename,'wb') # creates the file where the uploaded file should be stored
                fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
                fout.write(form.photo.file.read()) # writes the uploaded file to the newly created file.
                fout.close() # closes the file, upload complete.
                result["status"] = 200
            filename = filepath.split('/')[-1]
            analisis = self.machineLerning(filedir +'/'+ filename)
            result["analisis"] = analisis
            return result
        except Exception as error:
            result ={}
            result["status"] = "400"
            result["error"] = error.args[0]
            print("Error 100: {}".format(error.args[0]))
            return result