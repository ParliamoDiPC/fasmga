def setup(app):

	@app.route("/testa")
	def testa():
		print("Hello Flask!")

