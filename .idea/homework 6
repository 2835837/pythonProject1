def cubicequation(a, b, c, d):
    brucket1 = ((-b ** 3) / (27*(a) ** 3)) + ((b * c) / 6 * (a ** 2)) - (d / (2 * a))
    brucket2 = (c / 3 * a) - (b ** 2 / 9 * a ** 2)
    brucket3 = b / 3 * a
    x = ((brucket1 + brucket1 ** 2 + brucket2 ** 3) ** 1 / 3) + ((brucket1 - brucket1 ** 2 + brucket2 ** 3) ** 1 / 3) -  brucket3
    return x
# Ask the user their name and cubic
name= input ("what is your name")
a= input("what is your a")
b= input("what is your b")
c= input("what is your c")
d= input("what is your d")

#Give the answer
print("Hello",name,"I will solve x**3-6*x**2+11*x-6=0")
print("The root of the cubic is", cubicequation(a, b, c, d))

#END
quit()
