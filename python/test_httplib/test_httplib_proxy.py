import httplib
import os

conn = httplib.HTTPSConnection('google.com', 443)

conn.set_tunnel("127.0.0.1", 7890)

conn.request('GET', '/')

response = conn.getresponse()

print(response.status)
