lst = list("a,b,c,d,e")

print(lst)


lst =["a","b","c"]
print(lst)

lst = list("abcdefghijk")
print(lst[1:5])
print(lst[ : : -1])
print(lst * 2)
print(lst + [1,3,5,7])

lst += [1,2,3,4]
print(lst)

print("a" in lst)
print("q" not in lst)
print("q" in lst)

lst = list("solomon,moses,shade,tola,funmi")
print(lst)

list_of_lists =[1,2,[3,4,5],6]
print(list_of_lists[2][0])
print(list_of_lists[2])

my_dict = { "name" : "segun",
            "age" : 12,
            "sex" : "male",
            "hobby": ["python", "java"],
            "is_wife_beater" : False
            }
print(len(my_dict))
for key, value in my_dict.items():
 print(key, "---->", value)
 print(my_dict.items())

 prof = dict(name="segun", age=12)
 print(prof)

lst = ["segun", "is ", "going", "to", "school"]
lst.append("knowledgeable")
print(lst)

fruits = ["apple", "banana", "cucumber", "pear"]
fruits.reverse()
fruits.sort()
fruits.reverse()

print(fruits)

fruits.extend("orange")
fruits.append(("orange", "stone"))
fruits.insert(1, "grape")
fruits.insert(-1, "grape")
fruits.remove("apple")
fruits.count("apple")

fruits.insert(len(fruits), "grape")
print(fruits.pop(1))
print(fruits.clear())
print(fruits)


lst = []
for i in range (1,10):
    lst.append(i)
    print(i)

lst = []
for i in range (1,10):
    if i%2 !=0:
        lst.append(i)
    print (i)

lst = [chr(i) for i in range (65,91)]
print(lst)
