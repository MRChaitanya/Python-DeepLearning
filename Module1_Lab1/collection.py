from pip._vendor.distlib.compat import raw_input

def SuperSet(arr, n):
    list = []

    for i in range(2 ** n):
        subset = ""

        for j in range(n):

            if (i & (1 << j)) != 0:
                subset += str(arr[j]) + "|"

        if subset not in list and len(subset) > 0:
            list.append(subset)

    for subset in list:
        arr = subset.split('|')
        for string in arr:
            print(string, end=" ")
        print()

if __name__ == '__main__':
    arr = []
numbers = int(raw_input("How many numbers you want to enter?"))
for i in range(0, numbers):
    arr.append(int(raw_input("Enter the number :")))
n = len(arr)
SuperSet(arr, n)
