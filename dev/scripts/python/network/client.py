import socket, pickle

book = ['test', 'test1', 'test2', 'test4']
host = socket.gethostname()    
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data_a = pickle.dumps(book)
s.sendall(data_a)
data = s.recv(1024)
s.close()
print('Received', pickle.loads(data))
