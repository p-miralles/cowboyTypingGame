import socket
import sys  

#host = '25.57.178.133'
#host = '25.52.119.35' #tomas
host = '192.168.100.6' #noblex lan
port = 4004

# create socket
print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('# Getting remote IP address') 
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    

try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

# Connect to remote server
print('# Connecting to server, '+'(' + remote_ip + ')')
s.connect((remote_ip , port))

# Send data to remote server
print('# Sending data to server')
try:
    getRoomsCMD = '{"cmd":"getRooms"}'
    s.send(getRoomsCMD.encode())

except socket.error:
    print('Send failed')
    sys.exit()

# Receive data
print('# Receive data from server')
reply = s.recv(4004)
print(reply)