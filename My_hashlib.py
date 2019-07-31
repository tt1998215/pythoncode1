import hashlib
# md5=hashlib.md5()
# md5.update('how to use md5 in '.encode('utf-8'))
# md5.update('python hashlib'.encode('utf-8'))
# print(md5.hexdigest())
def calc_mad(password):
    password_md5=hashlib.md5(password.encode('utf-8')).hexdigest()
    return password_md5
k=calc_mad('password')
print(k)
