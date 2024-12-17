import nmap  # type: ignore

def scan_network():
    nm = nmap.PortScanner()
    ip_range = "192.168.18.0/24"  # Escanear toda la subred
    nm.scan(hosts=ip_range, arguments="-sn")
    
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            ip = nm[host]['addresses']['ipv4']
            mac = nm[host]['addresses']['mac']  # Corregir el error de tipografía

            print("IP:", ip)
            print("MAC:", mac)
        else:
            print("IP:", nm[host]['addresses']['ipv4'])
            print("MAC: No disponible")

scan_network()
