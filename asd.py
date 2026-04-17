import marshal
with open ('asr.py','r',encoding='utf-8')as fali:
    code=fali.read()
en_code=marshal.dumps(compile(code,'<string>','exec'))
with open ('new.py','wb')as fali:
    fali.write(en_code)
print("DONE!")