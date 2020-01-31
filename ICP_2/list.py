my_list = []
list2 = []
n = int(input("enter number of students:"))
print("enter weights")
for i in range(0,n):
    a = int(input())
    my_list.append(a)
print("the list in lbs is:\n")
print(my_list)
for element in my_list:
    e = (element*0.45)
    list2.append(e)
print("\nthe list in kgs is:\n")
print(list2)