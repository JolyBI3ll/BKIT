import json
from print_result import print_result
from cm_timer import cm_timer_1
from random import randrange
from unique import Unique
from Field import field
import sys



path='data_light.json'
with open(path,encoding = "utf8") as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(list(set([el['job-name'] for el in arg])), key=lambda x: x.lower())


@print_result
def f2(arg):
    return [x for x in arg if x.split()[0].lower() =='программист']

@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python',arg))


@print_result
def f4(arg):
    a = list(map(lambda x: x + ' с зарплатой ',arg))
    b=[]
    for i in range(len(arg)):
        b.append(str(randrange(100000,200000)))
    return list(zip(a,b))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
