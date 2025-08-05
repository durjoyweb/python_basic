#Join two set in python

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}





set3 = {1, 2, 3}
set4 = {4, 5, 6}

result = set3 | set4
print(result)  # Output: {1, 2, 3, 4, 5, 6}




set5 = {1, 2}
set6 = {2, 3}

set5.update(set6)
print(set1)  # Output: {1, 2, 3}
