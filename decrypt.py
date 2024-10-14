file = open("encryptedData.txt", "r")
lines = []

while True:
    content = file.readline()
    if not content:
        break
    
    # break line in to list of letters and remove the new line char
    contentArray = content.split(" ")
    contentArray.pop()
    
    # create list of lines with letters as ints
    line = []
    for hex in contentArray:
        line.append(int(hex, 16))
    lines.append(line)
    
file.close()

def isValidLetter(c):
    return ord('a') <= c <= ord('z') or ord('A') <= c <= ord('Z')

# XOR each cipher c with all spaces. When the message m is a space, c XOR a space will be the key for that char.
ciphersXorSpace = []
for r in range(11):
    cXorS = []
    for c in range(33):
        xor = ord(" ") ^ lines[r][c]
        if(isValidLetter(xor)):
            cXorS.append(chr(xor))
        else:
            cXorS.append(" ")
    ciphersXorSpace.append(cXorS)
    print(cXorS)

# consolodate all the key chars that we know.
key = [' '] * 33
for c in range(33):
    for r in range(11):
        if ciphersXorSpace[r][c] != ' ':
            key[c] = ciphersXorSpace[r][c]
# fortunatly the key is english so we make an asssumption and see if it works.
print("The key recovered is the following where space is used for unknown:")
print("".join(key)) # _hisOTPKeyIs_erfectlySecureAlways

print()
print("The key follows asssuming it is proper english following the pattern:")
key = "ThisOTPKeyIsPerfectlySecureAlways"
print(key)
print()

print("The 11 mesages for that key follows:")
result = []
for r in range(11):
    cXorK = []
    for c in range(33):
        xor = lines[r][c] ^ ord(key[c])
        cXorK.append(chr(xor))
    result.append(cXorK)
    print("".join(cXorK))
