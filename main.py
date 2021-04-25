import flask, gevent.pywsgi
import os, glob, importlib
#import flask, pymongo, validators, string, random, os, glob, importlib

app = flask.Flask("Fasmga")

@app.route("/testm")
def testm():
	print("this is a test!")


if (os.environ.get("FLASK_ENV") == "development"):
	app.run()
else:
	http_server = gevent.pywsgi.WSGIServer(('0.0.0.0', 5000), app)
	http_server.serve_forever()
	
for filename in [os.path.basename(f)[:-3] for f in glob.glob(os.path.join(os.path.dirname("./Sources/Python/"), "*.py")) if os.path.isfile(f)]:
	filename = filename.removesuffix(".py")
	module = importlib.import_module(f"Sources.Python.{filename}")
	module.setup(app)
