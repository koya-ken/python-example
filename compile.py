import dis
s = '''
a = (1, 2)
b = (2, 3)
c = (3, 4)

z = (a[0] + b[0] + c[0])

t = 0
t += a[0]
t += b[0]
t += c[0]
'''

x = compile(s, '', 'exec')

dis.dis(x)