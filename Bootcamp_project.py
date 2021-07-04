import hashlib

string = input('enter the string that you want to encrypt\n')
result = hashlib.md5(string.encode())

print('You have entered:')
print(string)

print("Your resulting hash code is : \n", end ="")
print(result.hexdigest())