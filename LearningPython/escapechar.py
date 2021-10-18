#ESCAPE CHARACTER
splitstring = " This\n string\n has\n been\n split"
print(splitstring)
tabbedstring = "1\t2\t3\t4\t5\t6"
print(tabbedstring)
#prefixing a special character with "\" turns it into an ordinary character.
print('fola said "no, no, she\'s got to go".')
#or you can code
print("fola said \"no, no, she's got to go\".")
#alternatively python recognises """ and knows string isn't finished till the string ends in """
print("""fola said "no, no, she's got to go".""")
anothersplitstring="""gotta learn this coding thing \
step \
by\
 step"""
#backlash is used the escape the end of the line
print(anothersplitstring)

#Using a backlash within the Code
# Method 1/2 : use a double backslah which is the preferred method when coding
print("C:\\Users\\timbuchalka\\notes.txt")
# Method 2/2: use a "r" at the beginnning (before quotation marks) to make sure
# the code line is taken in its raw format
print(r"C:\Users\timbuchalka\notes.txt")
