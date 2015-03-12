#coding:utf-8
import bobo, webob

from controller import Controller

@bobo.subroute('/user', scan=True)
class UserController(Controller):

    def __init__(self, request):
        self.request = request
        
    @bobo.query('')
    def base(self):
        return "Hello!"



