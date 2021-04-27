from flask import Flask, render_template, send_from_directory
import gevent.pywsgi, pymongo, dotenv
import os, glob, importlib

dotenv.load_dotenv()

app = Flask("Fasmga", template_folder="Sources/HTML")
app.database = pymongo.MongoClient(os.getenv("MongoDBString"))
app.database.db = app.database["Fasmga"]

@app.route("/")
def main():
  return render_template("main.html", login=False)

@app.route("/favicon.ico")
def favicon():
  return send_from_directory(os.path.join(app.root_path, "Sources/Image"),"favicon.ico", mimetype="image/vnd.microsoft.icon")

@app.route("/sources/image/passwordProtect.png")
def password_protect_image():
	return send_from_directory(os.path.join(app.root_path, "Sources/Image"),"password_protected.png")

for filename in [os.path.basename(f)[:-3] for f in glob.glob(os.path.join(os.path.dirname("./Sources/Python/"), "*.py")) if os.path.isfile(f)]:
	filename = filename.removesuffix(".py")
	module = importlib.import_module(f"Sources.Python.{filename}")
	module.setup(app)

if (os.environ.get("FLASK_ENV") == "development"):
	app.run()
else:
	try:
		host = os.getenv("host") or "0.0.0.0"
		port = int(os.getenv("port")) or 5000
		print(f"Running on http://{host}:{port}")
		http_server = gevent.pywsgi.WSGIServer((host, port), app)
		http_server.serve_forever()
	except KeyboardInterrupt:
		print("Stopping server...")
