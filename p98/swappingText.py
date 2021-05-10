def swappingFiles():
    inputA = input('Enter one file to swap with')
    inputB = input('Enter another file to swap with')
    
    with open(inputA,'r') as a:
        dataA = a.read()
    
    with open(inputB,'r') as b:
        dataB = b.read()
    
    with open(dataA, 'w') as a:
        a.write(dataB)
    
    with open(dataB, 'w') as b:
        b.write(dataA)    
    
    print(dataA,', is dataB')
    print(dataB,', is dataA')
    
swappingFiles()