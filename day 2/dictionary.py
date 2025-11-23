# dictionary is used to store data in key-value pairs
# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary can be any data type
dic = {
    "name": "rafi",
    "age":23,
    "hasLaptop":"True",
    "books":["A","B","C"]
}

print(dic)
# to print length of dictionary --> len()
print(len(dic))

# to print type --> type()
print(type(dic))

# declare dictionary using constructor - dict()
mydic = dict(name = 'r', age=23, country='b')
print(mydic)

# access value :: dicName['key'] or .get('key')
# to get keys --> .keys()
# to get values --> .values()
# to get items --> .items()
# to check a key is in the dictionary or not --> in keyword
# we can use get like this .get('key',defaultValue).if value not found give defaultValue

print(mydic['name'])
print(mydic.get('age'))
print(mydic.keys())
print(mydic.values())
print(mydic.items())
print('country' in mydic)

# change value
mydic['name'] = 'd'
mydic.update({'age':88})
print(mydic)

# add item same as change values but new keys
mydic['hasComputer'] = True
mydic.update({'height':5})
print(mydic)

# delete items --> pop(), popitem(){to remove the last insertion}, del{can delete a single or entire dictionary}, clear(){delete all the pair in dictionary}
mydic.pop('age')
mydic.popitem()
del mydic['name']
print(mydic)
mydic.clear()
print(mydic)
del mydic
# print(mydic) # error : mydic not found

# loop dictionary
loopdic = dict(name = 'r', age=23, country='b',roll='21')

# method 1
for x in loopdic:
    print(x)
    print(loopdic[x])

# method 2
for x in loopdic.keys():
    print(x)
    print(loopdic[x])

# method 3
for x in loopdic.values():
    print(x)

# method 4
for x,y in loopdic.items():
    print(x,y)

# copy dictionary : .copy(),.dict()
mydic = loopdic.copy()
hisdic = dict(loopdic)
print(mydic)
print(hisdic)

# nested dictionary
hisdic.update({'his':"hh"});
nestdic={
    "my":mydic,
    "his":hisdic
}

print(nestdic)
print(nestdic['his']['his'])


for x,y in nestdic.items():
    print(x)
    for p in y:
        print(y[p])

