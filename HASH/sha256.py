import hashlib
from random import randint

#Input integer
# message = randint(60,100)
# string = str(message)

#Input string
string = "MBC laboratory"

#Encode
encoded = string.encode()
result = hashlib.sha256(encoded)

#Display
print("String\t\t\t: ", end ="")
print(string)
print("Hash Value\t\t: ", end ="")
print(result)
print("Hexadecimal equivalent\t:",result.hexdigest())
print("Digest Size\t\t: ", end ="")
print(result.digest_size)
print("Block Size\t\t: ", end ="")
print(result.block_size)