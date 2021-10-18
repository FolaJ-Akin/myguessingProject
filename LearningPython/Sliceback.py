letters = "abcdefghijklmnopqrstuwxyz"

backwards = letters[25::-1]
sdrawkcab = backwards[::-1]
# [::-1] is a python idiom - recurs frequently and has a single semantic(meaning) role
# start value must be greater than the stop value
print(backwards)
print(sdrawkcab)
# produce qpo
challenge1 = letters[16:13:-1]
# produce edcba
challenge2 = letters[4::-1]
# produce last 8 characters
challenge3 = letters[25:16:-1]

print(challenge1)
print(challenge2)
print(challenge3)

# [:1] idiom doesn't return an error id the string is empty
