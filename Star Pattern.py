def p():
    while True:
        n=int(input('Enter the no of rows:')); print('Pyramid Pattern')
        for i in range(n):
                [print(" ",end=" ")  for j in range(n-i-1)]
                [print('*',end=" ") for k in range(2*i+1)];
                print()
        c=input('[Y/N]').capitalize(); 
        if c == "N": break
p()