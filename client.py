import requests
import ssl

server_address = 'https://localhost:80'

response = requests.get(server_address, verify='./p1/rootCACert.pem')
print("send a get request to", server_address)

print(response.status_code, response.reason)
if response:
    print('Success!')
else:
    print('An error has occurred.')




