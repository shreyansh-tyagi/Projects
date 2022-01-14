import wordtodigits 
import time
a = 'Just wAIt for Twenty Four Minute three seconds ONly'
b= '123 hello two'
b=wordtodigits.convert(b)
a=(wordtodigits.convert(a)).lower()
#b=a.lower()
print(a)
print(b)
c=[int(i) for i in a.split() if i.isdigit()]
print(c)
d=20
time.sleep(c[0])
if 'minute' or 'seconds' in a:
    print('having minute and second')
'''
b=a.split()
print(b)
print(b[0])
print(type(b[0]))
c=int(b[0])
print(type(c))
print(b[1])
'''

