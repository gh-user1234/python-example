#coding:utf-8
from mako.template import Template
from config.template import TemplateConfig

class View(object):
    def __init__(self, name, **kwargs):
        conf = TemplateConfig()
        filename = conf.get(name)
        self.__template = Template(filename=filename , output_encoding='utf-8', input_encoding='utf-8')
        self.__params = kwargs

    def render(self):
        return self.__template.render(**self.__params)


if __name__ == "__main__":
    params = {
        "user_name":"user1",
    }
    view = View("ERROR", **params)
    print view.render()

