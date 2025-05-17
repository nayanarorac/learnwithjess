def fibonaccinumbers(n):
    if (n == 1 or n== 2):
        fn = 1
    else:
        x = fibonaccinumbers(n-1)
        y = fibonaccinumbers(n-2)
        fn = x + y
    print(fn)
    return fn
   
fibonaccinumbers(15)
