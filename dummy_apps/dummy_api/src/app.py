from flask import Flask, request
from flask_restplus import Resource
from flask_restplus import Api
from authentication import Authenticator

app = Flask(__name__)

api = Api(version="1.0.0",
          title="Dummy API",
          validate=True,
          default="API",
          default_label="Dummy API",
          doc="/swaggerui")


@app.before_request
def require_basic_auth():
    if not app.config.get('AUTHENTICATOR'):
        app.config['AUTHENTICATOR'] = Authenticator()
    if request.endpoint != "healthcheck" and not app.config['AUTHENTICATOR'].authenticate():
        return Authenticator.challenge()


# Does not require authentication
@api.route('/healthcheck')
class Healthcheck(Resource):
    def get(self):
        return {"data": "hello world"}


# Requires authentication
@api.route('/secret')
class Secret(Resource):
    def get(self):
        return {"It could be wrong, ": "could be wrong, but it should have been right",
                "It could be wrong, could": " be wrong, to let our hearts ignite",
                "It could be wrong, could be": " wrong, are we digging a hole?",
                "It could be wrong, could be wrong": ", this is out of control"}


api.init_app(app)
