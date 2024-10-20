def m():
    while True:
        n=int(input("Enter any number:")); t=int(input("Enter the no of terms:")); 
        [print(n,"*",i,"=",n*i) for i in range(1,t+1)]; c=input("[Y/N]").capitalize();
        if c=='N': break
m()