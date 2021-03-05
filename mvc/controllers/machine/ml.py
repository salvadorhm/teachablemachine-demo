import web
import app

render = web.template.render("mvc/views/machine",base="template")

class Ml():

    def GET(self):
        return render.ml()