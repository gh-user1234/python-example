#coding:utf-8
class ConfigFactory(object):
    @staticmethod
    def createSystemConfig():
        from system import SystemConfig
        return SystemConfig()
    
    @staticmethod
    def createViewConfig():
        from view import ViewConfig
        return ViewConfig()

    @staticmethod
    def createTemplateConfig():
        from template import TemplateConfig
        return TemplateConfig()
