Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
word="Hello Python"
#get one char of the word
print (word[0])
H
#get one char of the word (same as above)
print (word[0:1])
H
#get the first three char
print (word[0:3])
Hel
#get the first three char
print (word[:3])
Hel
#get the last three char
print (word[-3:])
hon
#get all but the three first char
print (word[3:])
lo Python
#get all but the three last character
print (word[:-3])
Hello Pyt
KeyboardInterrupt
word.startswith("H")
True
word.endswith("n")
True
word.endswith("N")
False
#changing upper and lower case strings
print word.upper()
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
