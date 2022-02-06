"Math Module Functions"
import math
import random



a = input('\n\n')

print("\t\t\tTrigonometric Functions")
print("\n\n")

a = random.randint(1,10)



print(f'The sine of {a} is : sin({a}) <==> {math.sin(a)}\n\n')
print(f'The cosine of {a} is : cos({a}) <==> {math.cos(a)}\n\n')
print(f'The tan of {a} is : tan({a}) <==> {math.tan(a)}\n\n')
print("><"*80)


b = input('\n\n')
print("\t\t\tInverse Trigonometric Functions")
print("\n\n")
b = random.random()

print(f'The arcsine of {b} is : sin({b}) <==> {math.asin(b)}\n\n')
print(f'The arccosine of {b} is : cos({b}) <==> {math.acos(b)}\n\n')
print(f'The arctan of {b} is : tan({b}) <==> {math.atan(b)}\n\n')
print("><"*80)

c = input("\n\n")
print("\t\t\tHyperbolic Functions")
print("\n\n")
c = random.random()

print(f'The hyperbolic sine of {a} is : sinh({a}) <==> {math.sinh(a)}\n\n')
print(f'The hyperbolic cosine of {a} is : cosh({a}) <==> {math.cosh(a)}\n\n')
print(f'The hyperbolic tan of {a} is : tanh({a}) <==> {math.tanh(a)}\n\n')
print("><"*80)


c = input("\n\n")
print("\t\t\tInverse Hyperbolic Functions")
print("\n\n")

c = random.uniform(10,100)

print(f'The inverse hyperbolic sine of {a} is : asinh({a}) <==> {math.asinh(a)}\n\n')
print(f'The inverse hyperbolic cosine of {a} is : acosh({a}) <==> {math.acosh(a)}\n\n')
print(f'The inverse hyperbolic tan of 0.23 is : atanh(0.23) = {math.atanh(0.23)}\n\n')
print("><"*80)







c = input("\n\n")
print("\t\t\tNumber- theoretic and representation Functions")
print("\n\n")
e , f = random.uniform(1,100),random.uniform(1,100)

print(f"The ceiling of number {e} is : ceil({e}) <==> {math.ceil(e)}\n\n")

print(f"The floor of number {e} is : floor({e}) <==> {math.floor(e)}\n\n")


print(f"The GCD of {math.floor(e)} and {math.floor(f)} is : GCD({math.floor(e)},{math.floor(f)}) <===> {math.gcd(math.floor(e),math.floor(f))}\n\n")

print(f"The LCM of {math.floor(e)} and {math.floor(f)} is : LCM({math.floor(e)},{math.floor(f)}) <===> {math.lcm(math.floor(e),math.floor(f))}\n\n")



print(f"The Remainder when {math.floor(e)} is divided by {math.floor(f)} is : Remainder({math.floor(e)},{math.floor(f)}) <===> {math.remainder(math.floor(e),math.floor(f))}\n\n")

print("><"*80)














x = input("\n\n")
print("\t\t\t\tPower and Logarithmic Functions")
print("\n\n")

print(f" The Exp of number {e} is : Expo({e}) <==> {math.exp(e)}\n\n")

print(f" The Log of number {e} with respect to base {f} is : Log({e},{f}) <==> {math.log(e,f)}\n\n")

print(f"{e} raised to the power {f} is : Pow({e},{f}) : <===> {math.pow(e,f)}\n\n")

print(f"The Square root of {math.floor(e)} is : SQRT({math.floor(e)}) <===> {math.sqrt(math.floor(e))}\n\n")

print("><"*80)

x = input("\n\n")
print("\t\t\tDistance Function")
print("\n\n")

print(f"The distance between {(a,b)} and ({e,f}) is : Distance({(a,b)},{(e,f)}) <==> math.dist({(a,b)},{(e,f)})\n\n")

print("><"*80)

x = input("\n\n")
print("\t\t\tAngular Conversion")
print("\n\n")
print(f" Angle {e} in radians: Radians({e}) <==> {math.radians(e)}")
print(f" Angle {e} in degrees: Radians({e}) <==> {math.radians(e)}")

print("><"*80)
x = input("\n\n")
print("\t\t\tMath COnstants")
print("\n\n")
print(f" Pi : Math(pi) <===> {math.pi}")
print(f" euler's constant, e  : Math(e) <===> {math.e}")
print("><"*80)



