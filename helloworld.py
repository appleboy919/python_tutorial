print("hello world")
name = "David Oh"
age = 24
print(name, "age is ", age)

from random import *

print(randrange(1, 46))
print(randint(1, 45))

SSN = "12121515"

print("first four digit: " + SSN[:4])
print("last four digit: " + SSN[-4:])
print(len(SSN))

ex = "test for testing"
print(ex.replace("test", "test1"))

index = ex.index("test")
print(str(index))
index = ex.index("test", index + 1)
print("new " + str(index))

print("I'm %d" % 24)
print("I'm {}".format(24))

print("testing %s" % "python")
print("testing %s and %s" % ("python", "VS CODE"))
print("testing {} and {}".format("python", "VS CODE"))
print("testing {1} and {0}".format("python", "VS CODE"))

print("I'm {age} and I live in {country}".format(age = 24, country = "Korea"))

age = 24
country = "Korea"
print(f"I'm {age} and I live in {country}")
