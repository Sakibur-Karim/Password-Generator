import random

s = input('Enter password length: ')
s = int(s)
while s<6:
    s = input('Please re-enter with length of at least 6 characters: ')
    s = int(s)

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
caps = 'QWERTYUIOPASDFGHJKLZXCVBNM'
num = '1234567890'
sym = '~!@#$%^&*()_+{}|:"<>?`-=[]\;,./'

password = ''

password += random.choice(num)
password += random.choice(caps)
password += random.choice(sym)

for i in range(s-3):
    password += random.choice(chars)

print(''.join(random.sample(password,len(password))))