def extension(filename:str):
    if type(filename) is str:
        splitt = filename.split(".")
        if(len(splitt)>1):
            print(splitt[-1])
        else:
            print("This filename has no extension")
    else:
        print("Please enter correct filename")
extension("fdg.ert")