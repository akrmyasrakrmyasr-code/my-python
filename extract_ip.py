import socket

def extract_ip():
    print("----------------")
    print("+  IP ADRES    +")
    print("----------------")
    hostname=input('Enter url sits:\n')
    ip_address=socket.gethostbyname(hostname)
    print(f" IP IS :{ip_address}")