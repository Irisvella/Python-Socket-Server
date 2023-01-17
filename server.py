import socketserver

with open("data.txt") as f:   #this reads the data file and stores each line into a list
    DB = [line.rstrip() for line in f]
    
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        
        if self.data.decode() == '1':
            self.data2 = self.request.recv(1024).strip()
            search = self.data2.decode()
            if any(search in word for word in DB):
                i = 0
                index = 0
                while i < len(DB):
                    if search in DB[i]:
                        index = i
                        self.data2 = DB[index]
                        self.request.sendall(self.data2.encode('utf-8'))
                    i += 1
            else:
                msg = "This customer does not exist."
                self.request.sendall(msg.encode('utf-8'))
                
        if self.data.decode() == '2':
            self.data2 = self.request.recv(1024).strip() #name
            self.data3 = self.request.recv(1024).strip() #age
            self.data4 = self.request.recv(1024).strip() #addr
            self.data5 = self.request.recv(1024).strip() #phone
            search = self.data2.decode()
            if any(search in word for word in DB):
                msg = "This customer already exists"
                self.request.sendall(msg.encode('utf-8'))
            else:
                age = self.data3.decode()
                addr = self.data4.decode()
                phone = self.data5.decode()
                to_add = (search + "|" + age + "|" + addr + "|" + phone)
                DB.append(to_add)
                msg = "The customer was successfully added to the database."
                self.request.sendall(msg.encode('utf-8'))
                
        if self.data.decode() == '3':
            self.data2 = self.request.recv(1024).strip()
            search = self.data2.decode()
            if any(search in word for word in DB):
                i = 0
                index = 0
                while i < len(DB):
                    if search in DB[i]:
                        index = i
                        DB.pop(index)
                    i += 1
                msg = "The customer was successfully deleted."
                self.request.sendall(msg.encode('utf-8'))
            else:
                msg = "This customer does not exist."
                self.request.sendall(msg.encode('utf-8'))

        if self.data.decode() == '4':
            self.data2 = self.request.recv(1024).strip()
            self.data3 = self.request.recv(1024).strip()
            search = self.data2.decode()
            updated_info = self.data3.decode()
            if any(search in word for word in DB):
                i = 0
                index = 0
                while i < len(DB):
                    if search in DB[i]:
                        index = i
                        data = ''.join(DB[i])
                        ddata = data.rsplit('|')
                        ddata[1] = updated_info
                        data = ddata[0] + "|" + str(ddata[1]) + "|" + ddata[2] + "|" + ddata[3]
                        DB.pop(index)
                        DB.append(data)
                    i += 1
                msg = "The customer's information was successfully updated."
                self.request.sendall(msg.encode('utf-8'))
            else:
                msg = "This customer does not exist."
                self.request.sendall(msg.encode('utf-8'))
                
        
        if self.data.decode() == '5':
            self.data2 = self.request.recv(1024).strip()
            self.data3 = self.request.recv(1024).strip()
            search = self.data2.decode()
            updated_info = self.data3.decode()
            if any(search in word for word in DB):
                i = 0
                index = 0
                while i < len(DB):
                    if search in DB[i]:
                        index = i
                        data = ''.join(DB[i])
                        ddata = data.rsplit('|')
                        ddata[2] = updated_info
                        data = ddata[0] + "|" + str(ddata[1]) + "|" + ddata[2] + "|" + ddata[3]
                        DB.pop(index)
                        DB.append(data)
                    i += 1
                msg = "The customer's information was successfully updated."
                self.request.sendall(msg.encode('utf-8'))
            else:
                msg = "This customer does not exist."
                self.request.sendall(msg.encode('utf-8'))
        
        if self.data.decode() == '6':
            self.data2 = self.request.recv(1024).strip()
            self.data3 = self.request.recv(1024).strip()
            search = self.data2.decode()
            updated_info = self.data3.decode()
            if any(search in word for word in DB):
                i = 0
                index = 0
                while i < len(DB):
                    if search in DB[i]:
                        index = i
                        data = ''.join(DB[i])
                        ddata = data.rsplit('|')
                        ddata[3] = updated_info
                        data = ddata[0] + "|" + str(ddata[1]) + "|" + ddata[2] + "|" + ddata[3]
                        DB.pop(index)
                        DB.append(data)
                    i += 1
                msg = "The customer's information was successfully updated."
                self.request.sendall(msg.encode('utf-8'))
            else:
                msg = "This customer does not exist."
                self.request.sendall(msg.encode('utf-8'))
        
        if self.data.decode() == '7':
            DB.sort()
            msg = '\n'.join(DB)
            self.request.sendall(msg.encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()