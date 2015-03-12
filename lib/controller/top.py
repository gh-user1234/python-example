#coding:utf-8
import bobo, webob
from controller import Controller
from service.top.display import TopDisplayService
from view.view import View

@bobo.subroute('', scan=True)
class TopController(Controller):

    def __init__(self, request):
        self.request = request
        
    @bobo.query('')
    @bobo.query('/')
    def base(self):
        service = TopDisplayService()
        result = service.execute()
        view  = View("TOP", **result)
        return view.render()


    @bobo.query('/add')
    def get_add(self):
        return "(^^)"


    @bobo.query('/error')
    def login(self):
        params = {
            "user_name":"user1",
        }
        view  = View("ERROR", **params)
        return view.render()
