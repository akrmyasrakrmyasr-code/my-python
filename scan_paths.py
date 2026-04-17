import requests

def scan_paths():
    url=input('Enter link : \n')
    paths=['1.txt','awd.php','awd7y.html','admin.php']
    for path in paths:
        full_url=f"{url}/{path}"
        response=requests.get(full_url)
        if response.status_code==200:
            print(f'[+]found : {url} | {path} |{response.status_code}')
        else:
            print(f'not found :{full_url}')