class Sample:
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,value):
        self.__x = value
    
    def __setattr__(self, name, value):
        print('setattr',name,value)
        return super().__setattr__(name, value)
class Sample2: pass

class PropertyObject:
    def __init__(self,d):
        super().__init__()
        self.__dict__ = d

    def __setattr__(self, name, value):
        if name == '__dict__':
            return super().__setattr__(name, value)
        if isinstance(value,dict):
            self.__dict__['name'] = PropertyObject(value)
            return
        return super().__setattr__(name, value)
a = Sample()
b = {'x': 5,'y':{'b':1}}
print('Sample======')
a.x = 1
a.__dict__ = b
print(a.__dict__)
# a.__dict__ = {'_Sample__x': 2}
print(a.x)
print()
print('Sample2=======')
a = Sample2()
a.__dict__ = b
print(a.x)
print(a.y['b'])

p = PropertyObject(b)
print(p.y.b)