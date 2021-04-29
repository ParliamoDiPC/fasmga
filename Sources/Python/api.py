from flask import request

def setup(app):

	@app.route("/api/create", methods=["POST"])
	def api_create():
		print(request.form["token"])
		return "Hello Flask!"
