import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

domain_name = "governorsindh.com"
ip_address = get_ip_address(domain_name)

if ip_address:
    print(f"The IP address of {domain_name} is: {ip_address}")
else:
    print(f"Unable to retrieve the IP address of {domain_name}")
