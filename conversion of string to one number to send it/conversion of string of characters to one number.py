
chars =  "".join(str(n) for n in range(10))+"abcdefghijklmnopqrstuvwxyz "
print(len(chars))
def str2int(s, chars):
    i = 0
    for c in reversed(s):
        i *= len(chars)
        i += chars.index(c)
    return i

def int2str(i, chars):
    s = ""
    while i:
        s += chars[i % len(chars)]
        i //= len(chars)
    return s
num=str2int("0235abg02efgrtertredsaddwdawdafesfsegtrhehadwdwadhtnuyh6hhtui", chars)
x=int2str(num, chars)
print(num)
print(x)
#num1=str2int(x, chars)
#print(num1)
