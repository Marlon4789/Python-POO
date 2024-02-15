# Method resolution order

class A:
    def hablar(self):
        print('hola desde A')

class B(A):
    def hablar(self):
        print('hola desde B')

class C(B):
    def hablar(self):
        print('hola desde C')

class D(B, A):
    def hablar(self):
        print('hola desde D')

d = D()

C.hablar(d)