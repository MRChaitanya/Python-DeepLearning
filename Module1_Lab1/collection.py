from pip._vendor.distlib.compat import raw_input


def SuperSet(arr, n):
    _list = []

    for i in range(2 ** n):
        subset = ""

        for j in range(n):

            if (i & (1 << j)) != 0:
                subset += str(arr[j]) + "|"

        if subset not in _list and len(subset) > 0:
            _list.append(subset)

    for subset in _list:
        arr = subset.split('|')
        for string in arr:
            print(string, end=" ")
        print()


if __name__ == '__main__':
    arr = []
elem = int(raw_input("insert how many elements you want:"))
for i in range(0, elem):
    arr.append(int(raw_input("Enter next number :")))
n = len(arr)
SuperSet(arr, n)
