# Calculates the n-th fibonacci number
def fibonaccinumbers(n):
    if (n == 1 or n == 2):
        fn = 1
    else:
        x = fibonaccinumbers(n-1)
        y = fibonaccinumbers(n-2)
        fn = x + y
    return fn
   
fn = fibonaccinumbers(15)
print(fn)
