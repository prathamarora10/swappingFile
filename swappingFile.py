def swapFileData():
    fileName1 = input('Enter a file name: ')
    fileName2 = input('Enter a file name: ')
    f1 = open(fileName1, 'r')
    f2 = open(fileName2, 'r')
    data_a = f1.read()
    data_b = f2.read()
    f1 = open(fileName1, 'w')
    f1.write(data_b)
    f2 = open(fileName2, 'w')
    f2.write(data_a)

swapFileData()