class A:
    def __init__(self):
        print('A __init__')

    def methoda(self):
        print('A method a')
class B(A):
    def __init__(self):
        print('B __init__')

    def methoda(self):
        print('B method a')
class C(A):
    def __init__(self):
        super().__init__()
        print('C __init__')
    def methoda(self):
        print('C method a')
class D(C):
    def __init__(self):
        super().__init__()
        print('D __init__')
    def methoda(self):
        print('D method a')

class MethodA1():
    def methoda(self):
        print('methoda1')
class MethodA2():
    def methoda(self):
        print('methoda2')
class MethodA3():
    def methoda(self):
        print('methoda3')
class MergeMethodA1(MethodA1,MethodA2):
    pass
class MergeMethodA2(MethodA2,MethodA1):
    pass
class MergeMethodA3(MergeMethodA1,MethodA3):
    pass
# 継承順が異なる場合継承ができない
# class MergeMethodA4(MergeMethodA1,MergeMethodA2):
#     pass
# 継承順が同じなら継承できる、ただし同じクラスを継承はできない
# 先祖が同じ場合は可能
class MergeMethodA5(MergeMethodA1,MethodA1,MethodA2):
    pass
# error ################### 
# class D2(C,C):
#     def __init__(self):
#         super().__init__()
#         print('D2 __init__')
#     def methoda(self):
#         print('D2 method a')
print('B init ========')
a = B()
print()

print('C init ========')
a = C()
print()

print('D init ========')
a = D()
print()
# error ################### 
# print('D2 init ========')
# a = D2()
# print()
print('MergeMethodA1 init ========')
# 同じメソッドが定義されているクラスを多重継承した場合
# 先に継承したクラスのものが呼び出される
a = MergeMethodA1()
a.methoda()
MethodA2.methoda(a)
print()
print('MergeMethodA2 init ========')
a = MergeMethodA2()
a.methoda()
MethodA2.methoda(a)
print()
print('MergeMethodA3 init ========')
a = MergeMethodA3()
a.methoda()
MethodA2.methoda(a)
print()
# print('MergeMethodA4 init ========')
# a = MergeMethodA4()
# a.methoda()
# MethodA2.methoda(a)
# print()
print('MergeMethodA5 init ========')
a = MergeMethodA5()
a.methoda()
MethodA2.methoda(a)
print()