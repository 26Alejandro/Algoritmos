from scapy.all import ARP, Ether, srp

# Dirección de red local
red_local = "172.17.32.20/24"  # Cambiado a una red en formato CIDR

# Dirección MAC de broadcast
mac_broadcast = "ff:ff:ff:ff:ff:ff"

# Crear un paquete ARP
paquete_arp = ARP(pdst=red_local)
# Crear un paquete Ethernet
paquete_eth = Ether(dst=mac_broadcast)
# Combinar ambos paquetes
paquete = paquete_eth / paquete_arp

# Enviar el paquete y recibir la respuesta
respuesta, sin_responder = srp(paquete, timeout=2, verbose=0)

# Imprimir direcciones IP encontradas
print("Direcciones IP encontradas:")
for sent, recibido in respuesta:
    print(recibido.psrc)
