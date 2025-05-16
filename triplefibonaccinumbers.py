def triplefibonaccinumbers(n):
    if(n == 1 or n== 2 or n == 3):
        fn = 1
    else:
        x = triplefibonaccinumbers(n-1)
        y = triplefibonaccinumbers(n-2)
        z = triplefibonaccinumbers(n-3)
        fn = x + y + z
    print(fn)
    return fn
   
triplefibonaccinumbers(10)
