def compute_hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if( x % i == 0) and (y % i == 0):
            hcf = i
    return hcf
#num1 = 54
#num2 = 24
num1 = int(input(" Enter a number: "))
num2 = int(input(" Enter a number: "))
print(" The HCF is",compute_hcf(num1, num2))