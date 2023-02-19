#access files remotely
# * Gain access to different directories
# * View files
# * Download files
# * Remove files
# * Remove directories
# * Send files

import os
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print("")
print("Server is currently running 0", host)
print("")
print("Waiting for connections...")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, "Has connected to the server sucessfully")

#connection has been completed

#command handling
while 1:
    print("")
    command = input(str("Command >>"))
    if command == "view_cwd":
        conn.send(command.encode())
        print("Command sent waiting for execution...")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command output: ", files)

    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("Custom dir: "))
        conn.send(user_input.encode())
        print("")
        print("Command has been sent.")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Custom dir result: ", files)

    elif command == "download_file":
            conn.send(command.encode())
            print("")
            filepath = input(str("Please eneter the file path including file name: "))
            conn.send(filepath.encode())
            file = conn.recv(10000)
            print("")
            filename = input(str("Please enter the received file name including the extension: "))
            new_file = open(filename,"wb")
            new_file.write(file)
            new_file.close()
            print("")
            print(filename," has been downloaded and saved ")
            print("")

    elif command == "remove_file":
        conn.send(command.encode())
        fileanddir = input(str("Please enter file name and directory: "))
        conn.send(fileanddir.encode())
        print("")
        print("Command has been executed sucessfully: File removed")

    elif command == "send_file":
        conn.send(command.encode())
        file = input(str("Please eneter the filename and directory of the file: "))
        filename=input(str("Enter the file name for the file being sent: "))
        data=open(file,"rb")
        file_data=data.read(7000)
        conn.send(file_data)
        print(file, " has been sent sucessfully")
        conn.send(filename.encode())
    
    else:
        print("")
        print("Command not recognized.")