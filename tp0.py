import time, sys, math, threading
 ### {30n + 11, 30n + 13, 30n + 17, 30n + 19} esto me generá potenciales grupos pero no me asegura que cada uno de sus elementos sea primo. Esta estructura es necesaria para asegurar que ninguno de los cuatro números primos sea divisible por 2, 3 o por 5).
## Como sé que no es divisile por 2, 3 o 5. Con esto se descartan los multiplos de 2, 3 y 5, empiezo desde 7.
def esprimo(n: int, primos: list):    

    # print("Numero:", n, "primos: ", primos)
    for p in primos: 
        if n % p == 0: 
            return False

    primos.add(n)
#    print(primos)
    return True

### 30n + 19 <= 1.000.000 => n <= (1.000.000-19) /30 = L33.332,7 => 33.332 
def getNumOfIterations(n: int) -> int :
    return math.floor((n - 19) * 1/30)


def get_primes_in_range(start, end):
    if end < 2 or start > end:
        return []
    
    # Step 1: Clamp start to the lowest possible prime
    start = max(2, start)
    
    # Step 2: Find all base primes up to sqrt(end)
    limit = int(end**0.5) + 1
    is_prime = [True] * limit
    base_primes = []
    for p in range(2, limit):
        if is_prime[p]:
            base_primes.append(p)
            for i in range(p * p, limit, p):
                is_prime[i] = False

    # Step 3: Sieve the target range [start, end]
    range_size = end - start + 1
    segment = [True] * range_size

    for p in base_primes:
        # Find the first multiple of p greater than or equal to start
        start_idx = (start + p - 1) // p * p
        # Ensure we don't accidentally mark p itself as false if it's in our range
        start_idx = max(start_idx, p * p) 
        
        for j in range(start_idx, end + 1, p):
            segment[j - start] = False

    # Collect the results
    return {num for num in range(start, end + 1) if segment[num - start]}



### {30n + 11, 30n + 13, 30n + 17, 30n + 19} esto me generá potenciales grupos pero no me asegura que cada uno de sus elementos sea primo. Esta estructura es necesaria para asegurar que ninguno de los cuatro números primos sea divisible por 2, 3 o por 5).
def prog(nIter: int):
    t1=time.time()
    primos = {7} # Empiezo con un primo ya conocido
    for i in range (0, nIter + 1):
        c = 30 *i
        n1 = c + 11
        n2 = c + 13
        n3 = c + 17
        n4 = c + 19
        if (i > 0 and nIter != i): 
            #print(" El rango siguiente seria: ", primos[len(primos) -1], " hasta ", n1)
            primos|= get_primes_in_range(max(primos), n1 - 1)
#            print("ACA", primos)

        #print("Iteracion numero ", i)
#        print(n1, n2,n3,n4)
        if esprimo(n1, primos) and esprimo(n2, primos) and esprimo(n3, primos) and esprimo(n4, primos):
           print(n1, n2, n3, n4)
    t2=time.time()
    print(t2-t1)

def prog_range(start_i: int, end_i: int, results: list, index: int):
    t1 = time.time()
    primos = {7}
    local = []
    for i in range(start_i, end_i + 1):
        c = 30 * i
        n1 = c + 11
        n2 = c + 13
        n3 = c + 17
        n4 = c + 19
        if i > start_i and end_i != i:
            primos |= get_primes_in_range(max(primos), n1 - 1)
        if esprimo(n1, primos) and esprimo(n2, primos) and esprimo(n3, primos) and esprimo(n4, primos):
            local.append((n1, n2, n3, n4))
    results[index] = local
    t2 = time.time()
    print(f"thread {index} [{start_i}, {end_i}]: {t2 - t1}s")


def fork_join_prog(nIter: int, num_threads: int = 4):
    t1 = time.time()

    chunk = (nIter + 1) // num_threads
    ranges = []
    start = 0
    for k in range(num_threads):
        end = start + chunk - 1 if k < num_threads - 1 else nIter
        ranges.append((start, end))
        start = end + 1

    results = [None] * num_threads
    threads = []
    for idx, (start_i, end_i) in enumerate(ranges):
        th = threading.Thread(target=prog_range, args=(start_i, end_i, results, idx))
        threads.append(th)
        th.start()

    for th in threads:
        th.join()

    for local in results:
        for n1, n2, n3, n4 in local:
            print(n1, n2, n3, n4)

    t2 = time.time()
    print(t2 - t1)


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
    fork_join_prog(num_iterations, 4)



    ### Fork join se me cae porque se estarian repitiendo calculos, por lo tanto es necesario una memoria compartida 
    ### Prog dinamica es una gran opcion
    ### https://es.wikipedia.org/wiki/Cuadruplete_primo
    ### https://oeis.org/A007530
            ### {30n + 11, 30n + 13, 30n + 17, 30n + 19} esto me generá potenciales grupos pero no me asegura que cada uno de sus elementos sea primo. Esta estructura es necesaria para asegurar que ninguno de los cuatro números primos sea divisible por 2, 3 o por 5).
    ### https://t5k.org/glossary/page.php?sort=WheelFactorization
    ### https://www.primesdemystified.com/
    ### Usaria eso + dinamica.
    ### 30n + 19 <= 1.000.000 => n <= (1.000.000-19) /30 = L33.332,7 => 33.332 
