from flask_restful import Resource, Api

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Home(Resource):
    def get(self):
        return {'message': 'homepage'}

class MyName(Resource):
    def get(self,name):
        return {'message': f'hello {name}, welcome to flask'}

class MyAge(Resource):
    def get(self,age):
        return {'message': f'hello guys ,my age is {age}'}

