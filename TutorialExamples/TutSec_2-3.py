# Demonstration of concepts in sections 3 of the online
# Python 3.5.1 Tutorial Documentation. Tutorial is available at
# https://docs.python.org/3/tutorial/

print("Hello, World.")
print("""
Obviously the programs aren't flowing out as quickly as they should.
But let's get them started now with some demonstrations. The following
code demonstrates some of the concepts from the Python 3.5.1 Tutorial
sections 2 and 3.\n""")

print("""
First up, Python as a calculator. To make things a bit more interesting
we'll go ahead and assign some values to variables 'a' and 'b'. We'll
set 'a' to 9 and 'b' to 5.\n""")
print(">>> a = 9")
a = 9
print(">>> b = 5")
b = 5
print(">>> print(a + b)")
print(a + b)
print(">>> print(a - b)")
print(a - b)
print(">>> print(a * b)")
print(a * b)
print(">>> print(a / b)")
print(a / b)
print(">>> print(a // b)   #floor division")
print(a // b)
print(">>> print(a % b)   #modulus division")
print(a % b)
print(">>> print(a ** b)  #power calculation")
print(a ** b)

print("""
As a note, when running interactive mode, you can use '_' as a variable
that holds the last value. Given this is a script, I can't demonstrate
that functionality, but try it out on your own some time.\n""")

print("""
String functionality in Python is comprehensive but simple.
I'll use 'racecar', 'na', and 'BATMAN!!!' as example string variables.""")

print(">>> exStr1 = \'racecar\'")
exStr1 = 'racecar'
print(">>> exStr2 = \'na\'")
exStr2 = 'na'
print(">>> exStr3 = \'BATMAN!!!\'")
exStr3 = 'BATMAN!!!'

print("""
\'+\' concatenates strings together.
\'*\' repeats a string.
Placing literals next to eachother automatically concatenates them.
""")

print(">>> print(exStr1 + exStr1)")
print(exStr1 + exStr1)
print(">>> print(3 * exStr2)")
print(3 * exStr2)
print(">>> print(15 * exStr2 + \" \" + exStr3)")
print(15 * exStr2 + " " + exStr3)

print("""
Strings in Python are indexed. Individual characters can be referenced
using

    <string>[index]

and will be returned as a String -- there is no character primitive in
Python. Indexing is possible from the first and last chararcter. The
first character is index 0, and the last is index -1.
As a demonstration let's find the first, second, last, and third from
last character in 'racecar'.""")

print('>>> print(exStr1[0])')
print(exStr1[0])
print('>>> print(exStr1[1])')
print(exStr1[1])
print('>>> print(exStr[-1])')
print(exStr1[-1])
print('>>> print(exStra[-3])')
print(exStr1[-3])
print('>>> print(\'Bob\'s Burgers\'[7])')
print('Bob\'s Burgers'[7])

print("""
Python supports slicing strings into substrings.

    <string>[start index:end index]

A substring will be returned based on the specified indexes. The
starting index is included, while the ending index is excluded. If the
starting index is excluded, it will default to zero. If the ending
indexing is excluded, it defaults to the length of the string.\n""")

print('>>> print(exStr1[2:5])')
print(exStr1[2:5])
print('>>> print(exStr1[:4])')
print(exStr1[:4])
print('>>> print(exStr1[3:])')
print(exStr1[3:])
print('>>> print(exStr1[:3] + exStr1[3:])')
print(exStr1[:3] + exStr1[3:])

print("""
Attempting to index to a string at an index that is too large will
result in an error. However, a slice fails gracefully when an index
is out of range.\n""")

print('>>> print(exStr1[4:42])')
print(exStr1[4:42])
print('>>> print(exStr1[42:])')
print(exStr1[42:])
print('^The above line is a print statement containing an empty string.')
print('To avoid indexing errors, it may be useful to find their length.\n')

print('>>> print(len(exStr3))')
print(len(exStr3))

print("""
Lists are a built-in data structure for Python. They're represented as
comma-separated values between square brackets. Being a list and not a
set, a list can contain values of differing types.
Lists are indexed and support both slicing and concatenation. Unlike
strings, list are immutable. New values can be appended, while old values
can be overwritten.\n""")

print(">>> odds = [1, 3, 5, 'seven', 1001, B]")
odds = [1, 3, 5, 'seven', 1001, 'B']
print(">>> print(odds)")
print(odds)
print(">>> odds.append(13)")
odds.append(13)
print(">>> print(odds)")
print(odds)
print(">>> odds[3] = 7");
odds[3] = 7
print(">>> odds[4:5] = [9, 11]")
odds[4:5] = [9,11]
print(">>> print(odds)")
print(odds)
print(">>> odds[6] = []")
odds[6] = [];
print(">>> print(odds)")
print(odds)
print(">>> odds[6:7] = []")
odds[6:7] = []
print('>>> print(odds)')
print(odds)
print(">>> odds[2:2] = [3.1, 3.2, 3.3, 3.4]")
odds[2:2] = [3.1, 3.2, 3.3, 3.4]
print(">>> print(odds)")
print(odds)
print(">>> len(odds)")
print(len(odds))
print("odds[:] = []")
odds[:] = []
print("print(odds)")
print(odds)

print("One last thing to cover in the script -- while loops")

print("""
A = 0
while A < 3:
    print('Let\'s not do this again!')
    A += 1
""")
print("And time to run it...")
A = 0
while A < 3:
    print('Let\'s not do this again!')
    A += 1
print("Yea, I'm definitely finding a different way to demonstrate this.")
