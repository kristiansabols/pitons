def tests(parametrs):
    a=parametrs #darbības ar paramteriem
    return(a) #funkcijas rezultāts

print(tests("ķaķis"))

def pirmais(par1, par2):
    reizinajums=par1*par2
    summa=par1+par2
    if reizinajums<1000 :
        return reizinajums
    else:
        return summa
    
print("The result is", pirmais(40,30))

def otrais():
    for i in range(10):
        print("current number", i, "previous number", i-1, "sum:", i+i-1)
        return
    
otrais()
esosais = 0
ieprieksejais=0
for i in range(10):
    ieprieksejais=esosais
    esosais=i
    esosais=ieprieksejais
    print("current number", esosais, "previous number", ieprieksejais, "sum:", i+i-1)