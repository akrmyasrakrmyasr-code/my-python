import os

BASE='akrm-yasr'
TREE={
    "":['mam.py','kl.py','asd.py'],
    "ali":['sql.py','msi.py'],
    "akrm":['al.txt','ak.txt','adf.txt'],
    "abod":['frt.html','grt.pdf'],
    'folse/assets':['dde.js','erd.css']
}
for fol,fel in TREE.items():
    path=os.path.join(BASE,fol)
    os.makedirs(path,exist_ok=True)
    for f in fel:
        open(os.path.join(path,f),'a').close()
print("fanish")