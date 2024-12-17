import json 
from socket import gethostbyname, gethostname
from urllib.request import urlopen

with urlopen ('https://ipwho.is/?fields=ip') as response:
     body = json.loads(response.read())
     
ip = body[ 'ip']
indice= ip.find('.')
msb = ip [:indice]
ip = ip.replace(msb,'x'*len(msb))

print('ip interna :',gethostbyname(gethostname()))
print('ip externa: ', ip )