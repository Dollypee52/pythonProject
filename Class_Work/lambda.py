add = lambda x,y: x+y
sub = lambda x,y: x-y
print(add.__name__)
print(sub.__name__)


def operate(x,y, func):
    return func(x,y)

def add(a,b):
    return a+b

def sub(c,d):
    return c-d

def mul(f,g):
    return f*g

def operate(x,y, func):
    return func(x,y)

val_add = operate(24, 5, add)
val_sub = operate(24,5, sub)
val_mul = operate(3,4, mul)
div = operate(5,25, lambda x,y: y/x)
add = operate(5,25, lambda x,y: y+x)
sub = operate(5,25, lambda x,y: y-x)

print(val_add)
print(val_sub)
print(val_mul)
print(div)
print(add)
print(sub)

def multiple(x,fn):
     return x**x

def double(y,fn):
    return y*y


def multiple(y, fn):
    return fn(y)


double = multiple(6,lambda y: y*y)

print(double)

print(any([True,False,True]))

names = ["Amake", "Segun", "comb", "Samson", "foil"]

print(all(name.istitle() for name in names))

peoples = [  {"name": "Omosetan Omorele", "age": 30, "year_of_exp": 4, "language": ["Python", "Java"]},
            {"name": "John Doe", "age": 25, "year_of_exp": 2, "language": ["JavaScript", "C#"]},
            {"name": "Amaka Stephen", "age": 19, "year_of_exp": 5, "language": ["Python"]},
            {"name": "Florence Dolapo", "age": 28, "year_of_exp": 15, "language": ["Python", "Html"]},
            {"name": "Ernest Adeola", "age": 30, "year_of_exp": 4, "language": ["Python", "Kotlin"]}]

print([people["age"] <= 28 and people ["language"] for people in peoples])
print(any(people["age"] <= 28 and "Python" in people ["language"] for people in peoples))
print([people["name"] for people in peoples if people ["age"] <= 28 and "Python" in people["language"]])

map_object = map(lambda x: x**2, range(1, 10))
map_object = map(lambda x: x**2 if x % 2 == 0 else x, range(1, 10))
lst1 = list(map_object)
lst2 = list(map_object)
print("1", lst1)
print("2", lst2)

def isEven(x):
    return x % 2 == 0
filter_obj = list(filter(isEven, range(1,10)))
print(filter_obj)

from functools import reduce
fruits = ["Apple", "Pear","Pineapples", "orange", "watermelon", "Banana", "Cucumber"]
longest = reduce(lambda x,y:x if len(x) > len(y) else y, fruits)
print(longest)
print(max(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print(sorted(fruits, key=lambda x: x[-1]))