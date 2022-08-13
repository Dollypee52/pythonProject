# from dataclasses import dataclass, field
#
#
# @dataclass(order=True)
# class Person:
#     __slots__ = ['name','age']
#     name: str
#     age: int = field(default=16, init=False)
#     children: list = field(default_factory=lambda: [])
#
#     def is_minor(self):
#         return self.age < 18
#
#
#     p1 = Person("Adeola", age)
#     p2 = Person("Adeola")
#
#



from datetime import datetime, timedelta

d1= datetime.now()
d2=datetime(2021, 5, 27)
diff = d1 - d2
print(diff)

# print(d.year)


date_from_str = datetime.strptime("2022-02-06", "%Y-%m-%d")
print(date_from_str.year)

d = datetime.now()
print(d.strftime("%A"))
print(d.strftime("%B"))
print(d.strftime("%A %d %B %Y"))
s = "Hello"
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

for lst in [1, 2, 3, 4, 5, 6]:
    print(lst)


def custom_for(iterables, func):
    it = iter(iterables)

    while True:
        try:
            func(next(it))
        except StopIteration:
            break


custom_for([1, 2, 3, 4, 5, 6], print)


def cube(num):
    print(num ** 3)


custom_for([1, 2, 3, 4, 5], cube)

def gen():
    count = 0
    while True:
        yield count
        count += 1



tiger = gen()
print(next(tiger))
print(next(tiger))
print(next(tiger))
print(next(tiger))
print(next(tiger))
print(next(tiger))

# for i in gen():
#     print(i)


def counter(low, high, step=1):
    while low <= high:
        yield low
        low +=step
for i in counter(2, 10):
    print(i)
print(list(counter(2, 6, 2)))


import collections


a1 = collections.Counter("hello world")
print(a1)
a2 = collections.Counter("hi you")
print(a2)
a1.subtract(a2)
print(a1)

Person = collections.namedtuple("Person", "name age")
p1 =Person(name="Adeola", age=16)

print(p1.name)
