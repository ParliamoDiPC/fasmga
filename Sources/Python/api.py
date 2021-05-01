from flask import request
from werkzeug.exceptions import abort
from .utility import newUrlID, ratelimitCheck
import validators

def setup(app):
	Urls = app.database.db["Urls"]
	Tokens = app.database.db["Tokens"]
	BlackList = app.database.db["BlackList"]	

	@app.route("/api/create", methods=["POST"])
	def api_create():
		dbToken = Tokens.find_one({ "Token": request.form["Token"] })
		if not dbToken: return abort(401, "No Token, No access to api!")
		if ratelimitCheck(dbToken) == False: return abort(429, "Ralimit!")
		if not validators.url(str(request.form['Url'])): return abort(400, "Url not valid")
		if request.form["Url"] in BlackList.find_one({ "id": "608d4635fe59353a3418306c" })["BlackList"]: return abort(403, "Url blaklisted")
		urlID = newUrlID()
		docx = Urls.find_one({ "id": urlID })
		while docx:
			urlID = newUrlID()
			docx = Urls.find_one({ "id": urlID })
		Urls.insert_one({ "ID": urlID, "Owner": "API-" + dbToken["Owner"], "Password": request.form["Password"] })

		return f"/{urlID}"
