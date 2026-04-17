import requests

from rich import print
def update_sickr():
    url='http://localhost/cyber/sickr2.py'

    response=requests.get(url)
    if response.status_code==200:
        with open(__file__,"wb")as f:
            f.write(response.content)


        print("[blue][+] HAVE NEW UPDETE V2!")

    else:
        print("[red][-]NO UPDET FOUNDE!!")

update_sickr()

name=input('Enter the name \n')

print(f"The name is:{name}")
