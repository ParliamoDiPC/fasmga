from flask import render_template, request

def setup(app):

	#region 4xx: Client Error

	@app.errorhandler(400)
	def error_badRequest_handler(error):
		if not "Cookie" in request.headers: return f"{error}"
		return render_template("error.html", login=False, code="400", error=error)

	@app.errorhandler(401)
	def error_unauthorized_handler(error):
		if not "Cookie" in request.headers: return f"{error}"
		return render_template("error.html", login=False, code="401", error=error)

	@app.errorhandler(403)
	def error_Forbidden_handler(error):
		if not "Cookie" in request.headers: return f"{error}"
		return render_template("error.html", login=False, code="403", error=error)

	@app.errorhandler(405)
	def error_methodNotAllowed_handler(error):
		if not "Cookie" in request.headers: return f"{error}"
		return render_template("error.html", login=False, code="405", error=error)

	@app.errorhandler(429)
	def error_tooManyRequests_handler(error):
		if not "Cookie" in request.headers: return f"{error}"
		return render_template("error.html", login=False, code="429", error=error)

	#endregion