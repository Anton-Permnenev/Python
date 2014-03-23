__author__ = 'ASUS'
import shutil
import os
while True:
    str_in = input()
    list_in = str_in.split()
    command = list_in[0]
    if command == "quit":
        break
    elif command == "pwd":
        print(os.getcwd())
    elif command == "chdir":
        newdir = list_in[1]
        os.chdir(newdir)
    elif command == "copy":
        path_from = list_in[1]
        path_to = list_in[2]
        if(os.path.isfile(path_from)):
            shutil.copy(path_from, path_to)
        elif(os.path.isdir(path_from)):
             shutil.copytree(path_from, path_to)
    elif command == "move":
        path_from = list_in[1]
        path_to = list_in[2]
        shutil.move(path_from, path_to)
    elif command == "remove":
        path = list_in[1]
        if(os.path.isfile(path)):
            os.remove(path)
        elif(os.path.isdir(path)):
            shutil.rmtree(path)
    elif command == "createfile":
        path = list_in[1]
        file = open(path, 'w+')
        file.close()
    elif command == "createdir":
        path = list_in[1]
        os.makedirs(path)












