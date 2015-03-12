#coding:utf-8

class ServiceResult(object):
    def __init__(self):
        self.data = {}

    def get(self, key):
        return self.data[key] 

    def set(self, key, value):
        self.data[key] = value
    
    def remove(self, key):
        self.data.pop(key)

if __name__ == "__main__":
    result = ServiceResult()
    result.set("message", "foooooooooo")
    print result.get("message")
    result.remove("message")
    #print result.get("message")


    
