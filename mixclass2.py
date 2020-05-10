# https://stackoverflow.com/questions/6098970/are-mixin-class-init-functions-not-automatically-called
class BaseClass:
    def __init__(self,*args,**kwargs):
        pass
    def methoda(self):
        pass
    def methodb(self,*args,**kwargs):
        print(args,kwargs)
    def methodc(self,*args):
        print(args)
class BaseClass2:
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def methoda(self):
        pass
class A(BaseClass):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        print('A class init')
    def methoda(self):
        super().methoda()
        print('A methoda')
    def methodb(self,*args,**kwargs):
        super().methodb(args[1],**kwargs)
        # super().methodb(*args)
        # super().methodb()
        print('A methodb')
    def methodc(self,arg1,arg2):
        super().methodc((arg1,arg2))
        print('A methodc',arg1,arg2)

class B(BaseClass):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.a = 'B class a'
        self.b = 'B class b'
        print('B class init')
    def methoda(self):
        super().methoda()
        print('B methoda')
    def methodb(self,*args,**kwargs):
        super().methodb(args[0],**kwargs)
        print('B methodb')
    def methodc(self,arg2):
        super().methodc((arg2,))
        print('B methodc',arg2)

class C(A,B):
    def __init__(self,*args,**kwargs):
        """[summary]

        Arguments:
            A {[type]} -- [description]
        """
        super().__init__(*args,**kwargs)
# superの__init__を明示的に呼び出さなければ
# 片方(先に継承したほう)しか実施されない
c = C()
# 継承を考慮してキーワード引数を親クラスの__init__にわたす場合は
# object.__init__を呼び出す際に空になっている必要がある
# もしくはobjectを継承しているクラスでは呼び出す必要はない
c = C(a='aaa')
# mixinしたクラスが同じクラスを継承していた場合
# methodでsuper()を呼び出していれば、どちらも呼ばれる
# 同じメソッドを持つクラスでは呼び出されない
c.methoda()
# 可変長引数があった場合
# super()で呼び出したときに渡した数で少ない方と同じ数の引数が渡され
# あとで呼び出された方の値が優先される
print(c.a)
print(c.b)
c.methodc(1,2)
# 継承先のクラスでメソッドの引数が変わった場合
# 引数の数が多いクラスではそれぞれの値が引数として渡され
# 引数の数が少ないクラスではタプルとして渡される
# 片方に存在しない引数名があっても、どちらか片方にあればエラーにならない
# あとに継承したクラスのほうが引数が多い場合はエラーになる
c.methodc(arg1=(1,2),arg2=2)
c.methodc(arg2=(1,2),arg1=2)