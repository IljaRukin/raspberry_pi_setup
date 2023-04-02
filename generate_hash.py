import hashlib, uuid
salt = uuid.uuid4().hex
password = input('type in your password: ')
hashed_password = hashlib.sha512((password+salt).encode('utf-8')).hexdigest()
print('hashed password: ',str(hashed_password))
input('type any key to abort program')
