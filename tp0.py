import time, sys, math

### {30n + 11, 30n + 13, 30n + 17, 30n + 19} esto me generá potenciales grupos pero no me asegura que cada uno de sus elementos sea primo. Esta estructura es necesaria para asegurar que ninguno de los cuatro números primos sea divisible por 2, 3 o por 5).
## Como sé que no es divisile por 2, 3 o 5. Con esto se descartan los multiplos de 2, 3 y 5, empiezo desde 7.
def esprimo(n: int, is_prime: bytearray) -> bool:
    return bool(is_prime[n])


### 30n + 19 <= 1.000.000 => n <= (1.000.000-19) /30 = L33.332,7 => 33.332
def getNumOfIterations(n: int) -> int:
    return math.floor((n - 19) // 30)


def sieve_for_quadruplets(limit: int) -> bytearray:
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0] = 0
    if limit >= 1:
        is_prime[1] = 0
    for p in range(7, int(limit**0.5) + 1):
        if is_prime[p]:
            count = (limit - p*p) // p + 1
            is_prime[p*p::p] = bytearray(count)
    return is_prime


### {30n + 11, 30n + 13, 30n + 17, 30n + 19} esto me generá potenciales grupos pero no me asegura que cada uno de sus elementos sea primo. Esta estructura es necesaria para asegurar que ninguno de los cuatro números primos sea divisible por 2, 3 o por 5).
def prog(nIter: int, is_prime: bytearray) -> None:
    t1 = time.time()
    for i in range(0, nIter + 1):
        c = 30 * i
        n1 = c + 11
        n2 = c + 13
        n3 = c + 17
        n4 = c + 19
        if esprimo(n1, is_prime) and esprimo(n2, is_prime) and esprimo(n3, is_prime) and esprimo(n4, is_prime):
            print(n1, n2, n3, n4)
    t2 = time.time()
    print(t2-t1)

if __name__ == "__main__":
    args = sys.argv
    num = 1.000.000
    if len(args) == 2:
        num = int(args[1])

    num_iterations = getNumOfIterations(num)

    is_prime = sieve_for_quadruplets(num)
    
    prog(num_iterations, is_prime)



    ### Fork join se me cae porque se estarian repitiendo calculos, por lo tanto es necesario una memoria compartida
    ### Prog dinamica es una gran opcion
### https://en.wikipedia.org/wiki/Prime_quadruplet
    ### https://oeis.org/A007530
            ### {30n + 11, 30n + 13, 30n + 17, 30n + 19} esto me generá potenciales grupos pero no me asegura que cada uno de sus elementos sea primo. Esta estructura es necesaria para asegurar que ninguno de los cuatro números primos sea divisible por 2, 3 o por 5).
    ### https://t5k.org/glossary/page.php?sort=WheelFactorization
    ### https://www.primesdemystified.com/
    ### Usaria eso + dinamica.
    ### https://en.wikipedia.org/wiki/Primality_test -> explica lo de raiz de n 
    ### 30n + 19 <= 1.000.000 => n <= (1.000.000-19) /30 = L33.332,7 => 33.332
