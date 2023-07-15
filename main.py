import random

length = input('Enter password length: ')
length = int(length)
while length<6:
    length = input('Please re-enter with length of at least 6 characters: ')
    length = int(length)

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678901234567890~!@#$%^&*()_+{}|:"<>?`-=[]\;,./'
caps = 'QWERTYUIOPASDFGHJKLZXCVBNM'
num = '1234567890'
sym = '~!@#$%^&*()_+{}|:"<>?`-=[]\;,./'

password = ''

password += random.choice(num)
password += random.choice(caps)
password += random.choice(sym)

for i in range(length-3):
    password += random.choice(chars)

print(''.join(random.sample(password,len(password))))