import re
email1='someone@gmail.com'
email2='bill.gates@microsoft.com'
re_email= re.compile(r'^[a-zA-Z\.]+@[a-zA-Z0-9]+\.\w{3}$')
def is_valid_email(addr):
    if re_email.match(addr):
        print('ture')
        m=re.match(r'^([a-zA-Z0-9\.]+)@[a-zA-Z0-9]+\.\w{3}$',addr)
        print(m.group(1))
    else:
        print('false')
is_valid_email(email2)