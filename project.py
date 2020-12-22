import cryptography
from cryptography.fernet import Fernet

key = Fernet.generate_key()
file = open('key.key', 'wb')  # Open the file as wb to write bytes
file.write(key)  # The key is type bytes still
file.close()
file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()

# get the password
password = input('enter your password:')

# encode the password
encode = password.encode()

# encrypt password
f = Fernet(key)
encrypted = f.encrypt(encode)
x = ""
for i in range(len(encrypted)):
    x += "*"

# confirm_password
confirm_password = input('confirm your password:')
if confirm_password == password:
    print(x)
    print('your password is stored succesfully')
if confirm_password != password:
    print('wrong password')
    print('your both password does not match')
    print('please re-enter your password')

# decrypt password
f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)

# decode the password
password_last = decrypted.decode()

veiw_password = 0
if confirm_password == password:
    veiw_password = input('do you want to veiw the password ?')
if veiw_password == 'yes':
    print(password_last)
