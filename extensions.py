def extension(filename):
    splitt = filename.split(".")
    if(len(splitt)>1):
        print(splitt[-1])
    else:
        print("This filename has no extension")

extension("example.py")