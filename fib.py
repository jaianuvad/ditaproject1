# -*- coding: utf-8 -*-

a,b = 0,1
#while a<10:
#    print(a)
#    a,b=b, a+b

while a<10:
    print(a, end=',')
    a, b = b, a+b
print('\n')
