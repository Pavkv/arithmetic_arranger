def checkError(arr1):
    try:
        int(arr1.split(' ')[0]) == int(arr1.split(' ')[2])
    except ValueError:
        return 'Error: Numbers must only contain digits'
    if arr1.split(' ')[1] != '+' and arr1.split(' ')[1] != '-':
        return "Error: Operator must be '+' or '-'"
    if len(arr1.split(' ')[0]) > 4 and len(arr1.split(' ')[2]) > 4:
        return 'Error: Numbers cannot be more than four digits'


def checkNums(*args):
    arr1 = args[0]
    rowf = args[1]
    rows = args[2]
    rowt = args[3]
    first = arr1.split(' ')[0]
    second = arr1.split(' ')[2]
    if len(first) >= len(second):
        num = len(first)
    else:
        num = len(second)
    if num < 2:
        num = 3
    elif num < 3:
        num = 4
    elif num < 4:
        num = 5
    else:
        num = 6
    rows.append(' ' * (num - len(first)) + first)
    rowf.append(arr1.split(' ')[1] + ' ' * (num - len(second) - 1) + second)
    rowt.append('-' * num)
    if len(args) > 4:
        rowl = args[4]
        summ = len(str(int(first) + int(second)))
        if summ < 2:
            num = 3
        elif summ < 3:
            num = 4
        elif summ < 4:
            num = 5
        else:
            num = 6
        rowl.append(' ' * (num - summ) + str(int(first) + int(second)))


def arithmetic_arranger(*args):
    f = False
    if len(args) > 1:
        f = args[1]
    arr = args[0]
    if len(arr) > 5:
        return 'Error: Too many problems'
    for elem in arr:
        if checkError(elem):
            return checkError(elem)
    frow = []
    srow = []
    trow = []
    lrow = []
    if f:
        for elem in arr:
            checkNums(elem, frow, srow, trow, lrow)
        return '\n'.join(map('    '.join, [frow, srow, trow, lrow]))
    else:
        for elem in arr:
            checkNums(elem, frow, srow, trow)
        return '\n'.join(map('    '.join, [frow, srow, trow]))


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))