import sys
import socket


#Aqui estamos criando
try:
	sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print ("Falha ao criar socket")
	sys.exit()
print("Conexão estabelecida.")

host = "lucvsbraga"
port = 5558
sckt.connect((host, port))

print("Conexão criada")
print("Você está utilizando a porta: " , port)

while True:
	zap = sckt.recv(1024)
	print(zap.decode('ascii'))

	nickname = input("Nome: ")

	#manda a requisição 
	zap = 'GET / HTTP/1.1\n/' + nickname 
	sckt.sendall(zap.encode('ascii'))

	zap = sckt.recv(1024)
	print(zap.decode('ascii'))

	sckt.shutdown(socket.SHUT_RDWR)
	sckt.close()
	break