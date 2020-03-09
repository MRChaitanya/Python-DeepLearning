n1 = int(input("enter number of items in dictionary 1:"))
dict1 = {}

for i in range(n1):
    keys = int(input())
    values = input()
    dict1[keys] = values
print("User input for the dictionary 1:", dict1)

n2 = int(input("enter number of items in dictionary 2:"))
dict2 = {}

for i in range(n2):
    keys = int(input())
    values = input()
    dict2[keys] = values
print("User input for the dictionary 2:", dict2)

d = dict(dict1)
d.update(dict2)
print("Unsorted:", d)
ordered = sorted(d.items(), key=lambda x: x[1])
print("Sorted Dictionary:", ordered)