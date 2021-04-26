def setup(app):

	@app.route("/api/test")
	def api_test():
		print("Hello Flask!")
