set1={2,3,4,5}
set2={3,6,7,9}
print(set1|set2) #union
print(set1&set2) #intersection
print(set1-set2) # difference 2,5
print(set1^set2) # 2,4,5,6,7,9
print(set1.issubset(set2)) # false
print(set2.issuperset(set1)) # false