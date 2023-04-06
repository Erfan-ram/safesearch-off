with open("/etc/hosts", "a+") as file:
    file.seek(0)                # set cursor to the beginning of the file
    print(file.read())          # read and print all text in the file

    file.write("\n# mamnually written")
    file.write("\n142.250.184.206 google.com")
    file.write("\n142.250.184.206 www.google.com")
