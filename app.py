import web

urls = (
    '/', 'mvc.controllers.machine.index.Index',
    '/ml', 'mvc.apis.ml.Ml',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
