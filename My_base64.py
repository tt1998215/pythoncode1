import base64
def safe_base64_decode(s):
    if len(s)%4!=0:
        s=s+bytes('=',encoding='utf-8')*(4-len(s)%4)
    if not isinstance(s,bytes):
        s=bytes(s,encoding='utf-8')
    base64_str=base64.b64decode(s)
    return base64_str
assert b'abcd' == safe_base64_decode(b'YWJjZA=='),safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'),safe_base64_decode('YWJjZA')
print('Pass')
