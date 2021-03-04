import web
import app

render = web.template.render("mvc/views/machine",base="template")

class Index():

    def GET(self):
        return render.index()

    def POST(self):
        try:
            form = web.input()

            print(form)
        #     filedir = '../../static/jpg/' # change this to the directory you want to store the file in.
        #     if 'photo' in form: # to check if the file-object is created
        #         filepath=form.photo.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
        #         filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
        #         fout = open(filedir +'/'+ filename,'w') # creates the file where the uploaded file should be stored
        #         fout.write(form.photo.file.read()) # writes the uploaded file to the newly created file.
        #         fout.close() # closes the file, upload complete.
        #     return "cool"
        except Exception as error:
            print("Error 100: {}".format(error.args[0]))
            return "MMM algo salio mal"
