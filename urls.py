from sevices import HelloWorld,Home,MyName,MyAge

def all_urls(api):
    api.add_resource(HelloWorld, '/welcome')
    api.add_resource(Home, '/home')
    api.add_resource(MyName, '/myname/<string:name>')
    api.add_resource(MyAge, '/myage/<int:age>')
