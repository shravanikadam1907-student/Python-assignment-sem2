#create and access set elements
set={'apple','cherry', 'mango'}
for x in set:
    print(set)


#union of the elements
set1={1,2,3,4,5,6,7}
set2={5,6,7,8,9,10}
u=set1.union(set2)
print(u)


#intersection of the elements
set1={1,2,3,4,5,6,7}
set2={5,6,7,8,9,10}
I=set1.intersection(set2)
print(I)


#difference of the elements
set1={1,2,3,4,5,6,7}
set2={5,6,7,8,9,10}
d=set1.difference(set2)
print(d)
