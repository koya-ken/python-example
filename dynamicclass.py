# https://www.python-course.eu/python3_classes_and_type.php
class A:
    pass
class B:
    pass

c = type('C',(A,B),{})()
print(type(c))