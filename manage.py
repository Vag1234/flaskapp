from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Home(Resource):
    def get(self):
        return {'message':'homepage'}

api.add_resource(HelloWorld, '/welcome')
api.add_resource(Home, '/home')

if __name__ == '__main__':
    app.run(debug=True)