import time, sys, math

def esprimo(n):    
    i = 2
    cd=0
    while i<=n-1:
        if n%i == 0:
            cd = cd+1
        i = i+1
    if cd == 0:
        return True
    else:
        return False

### 30n + 19 <= 1.000.000 => n <= (1.000.000-19) /30 = L33.332,7 => 33.332 
def getNumOfIterations(n: int) -> int :
    return math.floor((n - 19) * 1/30)

def prog(num: int):
    t1=time.time()
    for i in range (11, num):
        if esprimo(i) and esprimo(i+2) and esprimo(i+6) and esprimo(i+8):
            print (i, i+2, i+6,i+8)
    t2=time.time()
    print(t2-t1)

if __name__ == "__main__": 
    args = sys.argv
    if len(args) - 2 < 0:
        print("Argumentos insuficientes")
        exit()

    
    num = int(args[1])
    
    if (num < 19): 
        num = 19

    num_iterations = getNumOfIterations(num)
    print(num_iterations)
  ##  prog(num)



    ### Fork join se me cae porque se estarian repitiendo calculos, por lo tanto es necesario una memoria compartida 
    ### Prog dinamica es una gran opcion
    ### https://es.wikipedia.org/wiki/Cuadruplete_primo
    ### https://oeis.org/A007530
            ### {30n + 11, 30n + 13, 30n + 17, 30n + 19} esto me generá potenciales grupos pero no me asegura que cada uno de sus elementos sea primo. Esta estructura es necesaria para asegurar que ninguno de los cuatro números primos sea divisible por 2, 3 o por 5).
    ### https://t5k.org/glossary/page.php?sort=WheelFactorization
    ### https://www.primesdemystified.com/
    ### Usaria eso + dinamica.
    ### 30n + 19 <= 1.000.000 => n <= (1.000.000-19) /30 = L33.332,7 => 33.332 
