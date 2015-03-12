#coding:utf-8
import bobo, webob
from controller import Controller

@bobo.subroute('/project', scan=True)
class ProjectController(Controller):

    def __init__(self, request):
        self.request = request
        
    @bobo.query('')
    @bobo.query('/')
    def get_base(self):
        return "PROJECT"

    @bobo.query('/add')
    def get_add(self):
        return "(^^)"

    @bobo.post('/add')
    def post_add(self):
        return "(^^)"

