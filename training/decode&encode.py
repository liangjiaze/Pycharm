import base64

str1 = "this is string example....wow!!!"
# str3 转成bytes 的string
str3 = str1.encode(encoding='utf-8', errors='strict');
print("str3:"), print(str3), print('')
# bytes 再进行 base64 编码
str4 = base64.b64encode(str3)
print("str4:"), print(str4), print('')
# 再base64 decode 一下
print("str4_decode:"), print(str4.decode()), print('')
# base64 解码
enstr = base64.b64decode(str4.decode())
print("enstr_decode:"), print(enstr.decode())
