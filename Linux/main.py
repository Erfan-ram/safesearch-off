with open("/etc/hosts", "r") as check:
    # data = check.read()
    lines = check.readlines()

    print(lines)
    for line in lines:
        if 'google.com' in line.lower() or 'www.google.com' in line.lower():
            print("found some settings")
        else:
            print("nothing found")


# with open("/etc/hosts", "a+") as file:
#     file.seek(0)
#     print(file.read())

#     file.write("\n# mamnually written")
#     file.write("\n142.250.184.206 google.com")
#     file.write("\n142.250.184.206 www.google.com")
