age = 24
print("My age is %d years" % age)

major = "years"
minor = "months"
# %d for integer value, %s for string value and %f for a floating point
print("My age is %d %s, %d %s" % (age, major, 6, minor))
print("PI is approximately %f" % (22 / 7))
# add precision inbetween % and f like so %12.50f
print("PI is approximately %60.50f" % (22 / 7))
# %x to display numbers in hexadecimals, %o to display octal numbers anf %e for scientific notation
# more in python docs for string formatting operations  N.B only for python 2 not 3
