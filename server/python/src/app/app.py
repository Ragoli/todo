import falcon

class Todos():
    def __init__(self):
        pass

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Hola mundo'

todos = Todos()

app = falcon.API()

app.add_route('/todos', todos)
