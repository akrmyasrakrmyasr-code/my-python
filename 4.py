import marshal
with open ('asr1.py','rb')as fali:
    fali.seek(16)
    en_code=marshal.loads(fali.read())

import dis
code_str=dis.code_info(en_code)
print(code_str)