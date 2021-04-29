from flask import render_template, request

def setup(app):

	@app.errorhandler(400)
	def error_badRequest_handler(error):
		print(request.headers)
		if not "Cookie" in request.headers: return f"{error}"
		return render_template("error.html", login=False, code="400", error=error)

	@app.errorhandler(405)
	def error_badRequest_handler(error):
		print(request.headers)
		if not "Cookie" in request.headers: return f"{error}"
		return render_template("error.html", login=False, code="405", error=error)