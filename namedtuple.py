from collections import namedtuple

Employee = namedtuple('Employee',['name','id'])
a = Employee('Kenji',1)
print(a.name)


from abc import ABCMeta
from abc import abstractmethod

class Meta(metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        print('call Meta')
    
    @abstractmethod
    def force_method(self):
        pass


class Parent:
    def __init__(self):
        super().__init__()
        print('call parent')
    
    def sample(self):
        pass

    def force_method(self):
        pass

class Sub(Parent,Meta):
    pass

a = Sub()