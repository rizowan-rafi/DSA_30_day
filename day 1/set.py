# set is one of the build-in data type in python to store multiple items in a single variable 
# set is unordered, unchangeable, unindexed and can't have duplicate.
# although we can't change the value in set, we can add or remove a value from set 
# set can be any data type
firstSet = {'hello',4,4.5,False,True,0,1}
print(firstSet) # {False, True, 4, 4.5, 'hello'}. False and 0 are same for set.same as True and 1.no duplicate allowed

# access item in set
# as there is no index, then we can use loop or use in keyword to access or check if a value is in the set or not
for x in firstSet:
    print(x)

# the find length of set -- len(setName)

print(4 in firstSet)
print(4 not in firstSet)

# add items - 
# add() --> add a item 
# update() --> add any iterative object
addSet = {1,2,3}
addSet.add(6)
print(addSet)
updateSet = {'hello','hi','bye'}
addSet.update(updateSet)
print(addSet)

# we can add any iterative object like tuples,list dictionary in set
iList = [False,True]
addSet.update(iList)
print(addSet)

# delete items --> 
# remove()(will show error if not found the value), 
# discard()(will n't show error), 
# pop()(delete a random value from set and return it),
# clear()(delete all the element in set)
# del ( delete the entire set completely)

delSet = {1,2,3,4,5,6}
delSet.remove(2)
print(delSet)
delSet.discard(3)
print(delSet)
delSet.clear()
print(delSet)
# del delSet
# print(delSet) # error : delSet not found


# join sets
# union() and | and update --> to join both set with all the element but union() and | return a new set and update() change the original set
# intersection() and & and intersection_update() --> to join both set with common value.intersection() and & return a new set and intersection_update() change the original set
# difference() and difference_update() --> remove the common values from first set and return it.difference()  return a new set and difference_update() change the original set
# symmetric_difference() --> join both set will uncommon values.has symmetric_difference_update().

joinSet = {1,2,3}
joinSet1 = {4,5,6,3}
print(joinSet.union(joinSet1))
print(joinSet.intersection(joinSet1))
print(joinSet.difference(joinSet1))
print(joinSet.symmetric_difference(joinSet1))


# frozenset --> to disable the add or remove item from set
frozeSet = frozenset({2,3,4})
print(frozeSet)
# frozenset.add(4) # error : 'frozenset' has no attribute 'add'

# extra method
# isdisjoint() --> check two set are disjoint or not
# issubset() --> check another set is a subset of the set or not
# issuperset() --> check this set is a subset of another set or not
m = {1,2,3}
b = {1,2,3,4,45,6}
c={4,5,6}
print(m.isdisjoint(c))
print(m.issubset(b))
print(m.issuperset(b))
print(b.issuperset(m))

# covert any iterative object to set --> set()
cc = [2,3,4]
bb = set(cc)
print(bb)

