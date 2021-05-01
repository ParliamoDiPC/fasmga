import random, string, json
global ratelimit
ratelimit = {}
Authorizated = json.load(open("Sources/Json/Authorizated.json", "r"))


def newUrlID(): return "".join(random.choice(string.ascii_lowercase) for i in range(8))

def ratelimitCheck(dbToken):
	for auth in Authorizated:	
		ratelimit[auth] = -1
		
	if not dbToken["Owner"] in ratelimit:
		ratelimit[dbToken["Owner"]] = 1
		return True
	else:
		if ratelimit[dbToken["Owner"]] < 20:
			if ratelimit[dbToken["Owner"]] == -1: return True
			ratelimit[dbToken["Owner"]] += 1
			return True
		elif ratelimit[dbToken["Owner"]] == -1: return True
		else: return False