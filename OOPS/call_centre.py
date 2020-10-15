from enum import Enum

class Rank(Enum):
    responder = 'Responder'
    manager = 'Manager'
    director = 'Director'

class Employee(object):
    def dispatchCall(self):
        raise NotImplementedError("Not pmplemented.")
    
    def aaccept_call(self, call)


class Responder(Employee):
    def __init__(self, name):
        self.role = Rank.responder

class Manager(Employee):
    def __init__(self, name):
        self.role = Rank.manager

class Distributer(Employee):
    def __init__(self):
        self.role = Rank.director
    
    

class CallCenter(object)