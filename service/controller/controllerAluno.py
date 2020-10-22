from service import service


@service.route("/")
def index():
	return "olá mundo"