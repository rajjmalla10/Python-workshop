set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

union = set1.union(set2)
print(len(union))

intersection = set1.intersection(set2)
print(intersection)

semmetric_difference = set1 ^ set2
print(semmetric_difference)

set1.add(40)
print(set1)

set2.remove(20)
print(set2)