import marshal
with open ('new.py','rb')as fali:
    en_code=marshal.loads(fali.read())
with open ('s1.py','w')as fali:
    fali.write(str(en_code))