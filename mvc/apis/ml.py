import web
import app


class Ml():

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

            return result
        except Exception as error:
            result ={}
            result["status"] = "400"
            result["error"] = error.args[0]
            print("Error 100: {}".format(error.args[0]))
            return result