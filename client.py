import socket

HOST, PORT = "localhost", 9999

selection = '9'
while selection != '8':
        menu = """\nPython DB Menu
        
        1. Find customer
        2. Add customer
        3. Delete customer
        4. Update customer age
        5. Update customer address
        6. Update customer phone
        7. Print report
        8. Exit
        """
        print(menu)
        selection = input("Select:")
        
        if selection == '1':
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, PORT))
                sock.send(selection.encode('utf-8'))
                find_customer = input("Please enter the customer name to search: ")
                if find_customer == '':
                    find_customer = " "
                sock.send(find_customer.encode('utf-8'))
                received = str(sock.recv(1024), 'utf-8')
                print(received)

        if selection == '2':
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, PORT))
                sock.send(selection.encode('utf-8'))
                
                add = input("Please input the name of the customer to add: ")
                if add == '':
                    add = " "
                sock.send(add.encode('utf-8'))
                add_age = input("Please input the customer's age: ")
                if add_age == '':
                    add_age = " "
                sock.send(add_age.encode('utf-8'))
                add_addr = input("Please input the customer's address: ")
                if add_addr == '':
                    add_addr = " "
                sock.send(add_addr.encode('utf-8'))
                add_phone = input("Please input the customer's phone number: ")
                if add_phone == '':
                    add_phone = " "
                sock.send(add_phone.encode('utf-8'))
                received = str(sock.recv(1024), 'utf-8')
                print(received)
                
        if selection == '3':
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, PORT))
                sock.send(selection.encode('utf-8'))
                del_customer = input("Please input the name of the customer to delete: ")
                if del_customer == '':
                    del_customer = ' '
                sock.send(del_customer.encode('utf-8'))
                received = str(sock.recv(1024), 'utf-8')
                print(received)
            
        if selection == '4':
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, PORT))
                sock.send(selection.encode('utf-8'))
                update_customer = input("Please input the name of the customer to update: ")
                if update_customer == '':
                    update_customer = ' '
                sock.send(update_customer.encode('utf-8'))
                update_age = input ("Please input the updated age: ")
                if update_age == '':
                    update_age = ' '
                sock.send(update_age.encode('utf-8'))
                received = str(sock.recv(1024), 'utf-8')
                print(received)
                
        if selection == '5':
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, PORT))
                sock.send(selection.encode('utf-8'))
                update_customer = input("Please input the name of the customer to update: ")
                if update_customer == '':
                    update_customer = ' '
                sock.send(update_customer.encode('utf-8'))
                update_addr = input ("Please input the updated address: ")
                if update_addr == '':
                    update_addr = ' '
                sock.send(update_addr.encode('utf-8'))
                received = str(sock.recv(1024), 'utf-8')
                print(received)                

        if selection == '6':
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, PORT))
                sock.send(selection.encode('utf-8'))
                update_customer = input("Please input the name of the customer to update: ")
                if update_customer == '':
                    update_customer = ' '
                sock.send(update_customer.encode('utf-8'))
                update_phone = input ("Please input the updated phone number: ")
                if update_phone == '':
                    update_phone = ' '
                sock.send(update_phone.encode('utf-8'))
                received = str(sock.recv(1024), 'utf-8')
                print(received) 
                
        if selection == '7':
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, PORT))
                sock.send(selection.encode('utf-8'))
                received = str(sock.recv(1024), 'utf-8')
                print("***Python DB Contents***")
                print(received)     
                
        if selection == '8':
            print("Goodbye!")            