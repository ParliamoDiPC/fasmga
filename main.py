from flask import Flask, render_template
import gevent.pywsgi, pymongo
import os, glob, importlib

app = Flask("Fasmga", template_folder='Sources/HTML')
app.database = pymongo.MongoClient(os.getenv("MongoDBString"))
app.database.db = app.database["Fasmga"]

@app.route('/')
def main():
  return render_template("index.html")

for filename in [os.path.basename(f)[:-3] for f in glob.glob(os.path.join(os.path.dirname("./Sources/Python/"), "*.py")) if os.path.isfile(f)]:
    filename = filename.removesuffix(".py")
    module = importlib.import_module(f"Sources.Python.{filename}")
    module.setup(app)

if (os.environ.get("FLASK_ENV") == "development"):
    app.run()
else:
    http_server = gevent.pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
