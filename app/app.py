from bottle import Bottle, run, template

ftp_server = Bottle()

@ftp_server.route("/")
def return_main_page():
    return template("main.html")

@ftp_server.route("/update")
def return_update():
    jsonify(get_server_list())

def get_server_list():
    return "{}"

if __name__ == "__main__":
    run(ftp_server, reloader=True)
