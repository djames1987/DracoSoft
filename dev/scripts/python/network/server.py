import socket, pickle, SQLite

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()

print('Connection from: ', addr)
while True:
    in_data = conn.recv(1024)
    if not in_data: break
    sql_data = pickle.loads(in_data)
    print('Adding the Following to the DataBase: ', sql_data)
    SQLite.add_to_db('server', [sql_data[0], sql_data[1], sql_data[2], sql_data[3]])
    SQLite.close_conn()
    conn.sendall(in_data)
conn.close()
