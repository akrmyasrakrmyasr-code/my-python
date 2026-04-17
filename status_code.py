import requests

def status_code():
    urls=[
        "https://www.google.com",
        "https://localhost/cyber/",
        "https://awyi54g87yhkefi.cidw",
        "http://testphp.vulnweb.com/"
    ]
    for x in urls:
        try:
            respones=requests.get(x)
            if requests.status_codes==200:
                print(f"[+]{x}is UP (200)")
            else:
                pass
        except requests.exceptions.RequestException:
            print(f"[-]{x} is Done")
            