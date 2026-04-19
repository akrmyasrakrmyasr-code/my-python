import os 
path= os.getenv("PATH")

paths=path.split(os.pathsep)


for p in paths:
    print('-',p)