import web

urls = (
    '/upload', 'mvc.controllers.machine.index.Index',
    '/', 'mvc.controllers.machine.upload.Upload',
    '/ml', 'mvc.controllers.machine.ml.Ml',
    '/api', 'mvc.apis.ml.Ml',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
