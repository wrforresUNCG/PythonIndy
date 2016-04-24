# If-Statements in python

x = int(input("Let's enter an int to check some if statements: "))

if x < 0:
    print("Well that's a negative number. Typical.\n")
elif x == 0:
    print("I supposed 0 is an int. Seems a bit like a default answer, though.\n")
elif x > 0:
    print("So larger than zero? I see we're quite the optimist.\n")
else:
    print("Do I print this line when an int isn't received?") #apparently not
    #got a syntax error for non int input, rather than seeing the else statement. Good to know
# else and elif are optional, go figure

#For Statements
#Not like for statements in C-likes --> user does not define iteration step and halt condition
#Python for statement interates over the items of any sequence(list or string) in the order that
#they appear

#words = ['okay', 'this', 'seems', 'weird', 7]
#whoops. 7 does not have a length, so the following for loop did not work -- TypeError
#let's generate a new list

words = ['what', 'about', 'this', 'one', 'Python']
for w in words:
    print(w, len(w))
#does the variable matter? can I change w to WOOPWOOPWOOP, 'cause why not Zoidberg?
for woopwoopwoop in words:
    print(woopwoopwoop, len(woopwoopwoop))
print("Apparently woopwoopwoop does work. Nice\n")

#what about doing some numeric functions?
numbersToChange = [1, 2, 3, 4, 5]
print(numbersToChange)
print("Well let\'s just go ahead and make it N^N. 'cause why not?")
for num in numbersToChange:
    print(num, "num ** num", num ** num)
print("Okay, but that didn't seem to store changes. Let's do a permanent change.")
for num in numbersToChange:
    numOld = num
    num = num ** num
    print(numOld, num)
print(numbersToChange)
print("\n")
#Okay, that apparently did not change the numbers either, so I'm doing something wrong
print(numbersToChange)
ctr = 0
for num in numbersToChange[:]:  #it was suggested to make a copy using a slice
    numbersToChange[ctr:ctr + 1] = [num * num]
    ctr += 1
print(numbersToChange)
print("HEY! THAT WORKED! Rad, figured out the for syntax.")
