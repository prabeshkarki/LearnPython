# looping through a string 

for x in 'banana':
    print(x)

# string length
a="hello, world!"
print(len(a))

# check string 
txt="the best thing in life are free!"
if 'free' in txt:
 print("yes, 'free' is present")

# check if not 
txt="the best thing in life are free!"
print("no" not in txt)

# modify string 
a="prabesh"
print(a.upper())

# remove whitespace 
a="   hello,world! "
print(a.strip())

# replace string 
a='hello, world!'
print(a.replace('h','H'))

# split string 
a="hello, world"
print(a.split(','))

# concatinate string 
a="hello"
b="world"
c=a+" "+b
print(c)

# format string 
# f string 
age=22
txt=f"my name is prabesh and i am {age} yrs old"
print(txt)

# escape character 
txt = "we are so called \"Vikings\" from the north."
print(txt)

# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value