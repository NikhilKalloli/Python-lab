try:
    print(a)
except NameError:
    print("name error")

try:
    print(3//0)
except ZeroDivisionError:
    print("zero div")

try:
    list=[1,3,4]
    print(list[9])
except IndexError:
    print("index issue")

try:
    dict = {'a':5,'b':6}
    print(dict['k'])
except KeyError:
    print("key issue")