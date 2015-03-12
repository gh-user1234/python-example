#coding:utf-8
import bobo
import webob
import traceback
from controller import Controller
from service.project.display import ProjectDisplayService
from service.task.display import TaskDisplayService
from service.task.create import TaskCreateService
from service.task.update import TaskUpdateService
from view.view import View

@bobo.subroute('/task', scan=True)
class TaskController(Controller):

    def __init__(self, request):
        self.request = request
        
    @bobo.query('')
    @bobo.query('/')
    def get_base(self):
        return bobo.redirect("/", 303)

    @bobo.post('/:project/add')
    def httppost_add_task(self, project, bobo_request):
        try:
            params = {
                "project.name" : project,
                "task.title" :  bobo_request.params['title'],
                "task.timelimit": bobo_request.params['timelimit'],
                "task.note": bobo_request.params['note'],
                "user.id" :1,
            }
            print params
            return "aaa"
            #service = TaskCreateService(**params)
            #result = service.execute()
            #view = View("TASK_CREATE", **result)
            #return view.render()
        except Exception as ex:
            print ex
            raise


    @bobo.post('/add')
    def httppost_add_task_sub(self, bobo_request):
        try:
            params = {
                "project.name" : "project1",
                "task.title" :  bobo_request.params['title'],
                "task.timelimit": bobo_request.params['timelimit'],
                "task.note": bobo_request.params['note'],
                "user.id" :1,
            }
            print params
            service = TaskCreateService(**params)
            service.execute()
            return bobo.redirect("/", 303)
        except Exception as ex:
            print ex
            raise


    @bobo.query('/add')
    def httpget_taskadd(self):
        try:
            print "task ADD!"
            params = {}
            view = View("TASK_CREATE", **params)
            return view.render()
        except Exception as ex:
            print ex
            return ex


    @bobo.query('/:project')
    @bobo.query('/:project/')
    def httpget_project(self, project):
        service = ProjectDisplayService()
        result = service.execute()
        view = View("PROJECT_VIEW", **result)
        return view.render()

    @bobo.post('/:project')
    @bobo.post('/:project/')
    def httppost_project(self, project):
        try:
            pass
        except:
            pass


    @bobo.post('/:project/:task')
    def httppost_task(self, project, task, bobo_request):
        try:
            print "task update!"
            params = {
                "project_name" : project, 
                "task.id" : task,
                "task.timelimit" : bobo_request.params["timelimit"],
                "task.note" : bobo_request.params["note"],
                "task.status" : bobo_request.params["status"],
            }
            service = TaskUpdateService(**params)
            service.execute()
            redirect = "/task/%s/%s" % (project,task,)
            return bobo.redirect(redirect, 303)
        except Exception as ex:
            print traceback.format_exc()
            params = {}
            view = View("ERROR", **params)
            return view.render()

    @bobo.query('/:project/:task')
    def get_task(self, project, task):
        try:
            params = {
                "project_name" : project,
                "task_id" : task,
            }
            service = TaskDisplayService(params)
            result = service.execute()
            view = View("TASK_DETAIL", **result)
            return view.render()
        except Exception as ex:
            print ex
            params = {}
            view = View("ERROR", **params)
            return view.render()



