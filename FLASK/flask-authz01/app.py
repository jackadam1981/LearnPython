import casbin
from middleware import Middleware
from flask import Flask

app = Flask(__name__)

enforcer = casbin.Enforcer("authz_model.conf", "policy.csv")
app.wsgi_app = Middleware(app.wsgi_app, enforcer)


@app.route("/")
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
