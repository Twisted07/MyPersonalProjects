'''
Name: Idris Abdullateef Adebowale
Matric No: 16/30GN041
Department: Materials and Metallurgical Engineering
Course code: MEE 505
Assignment: Taylor's Series Expansion
'''
import math

#Define taylor's series of sin as 'ts_sin'
def ts_sin(x, n):
    sin_x = 0
    for i in range(n):
        sin_x += ((-1)**i) * (x**(2*i+1)) / math.factorial(2*i + 1)
    return sin_x

#Define taylor's series of cos as 'ts_cos'
def ts_cos(x, n):
    cos_x = 0
    for i in range(n):
        cos_x += ((-1)**i) * (x**(2*i)) / math.factorial(2*i)
    return cos_x

#Define taylor's series of tan as 'ts_tan'
def ts_tan(x, n):
    sin_x = ts_sin(x, n)
    cos_x = ts_cos(x, n)
    tan_x = sin_x / cos_x
    return tan_x

#Define taylor's series of sinh as 'ts_sinh'
def ts_sinh(x, n):
    sinh_x = 0
    for i in range(n):
        sinh_x += (x**(2*i + 1)) / math.factorial(2*i + 1)
    return sinh_x

#Define taylor's series of cosh as 'ts_cosh'
def ts_cosh(x, n):
    cosh_x = 0
    for i in range(n):
        cosh_x += (x**(2*i)) / math.factorial(2*i)
    return cosh_x

#Define taylor's series of tanh as 'ts_tanh'
def ts_tanh(x, n):
    sinh_x = ts_sinh(x, n)
    cosh_x = ts_cosh(x, n)
    tanh_x = sinh_x / cosh_x
    return tanh_x

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms in the Taylor series: "))

print("The value of sin(x) = ", ts_sin(x, n))
print("The value of cos(x) = ", ts_cos(x, n))
print("The value of tan(x) = ", ts_tan(x, n))
print("The value of sinh(x) = ", ts_sinh(x, n))
print("The value of cosh(x) = ", ts_cosh(x, n))
print("The value of tanh(x) = ", ts_tanh(x, n))
