# Code created by Pepijn Weitzel
# Prompt user for file name
file = input("File name: ").lower()


match file:
    case str(x) if ".gif" in x:
        print("image/gif")
    case str(x) if ".jpg" in x:
        print("image/jpeg")
    case str(x) if ".jpeg" in x:
        print("image/jpeg")
    case str(x) if ".png" in x:
        print("image/png")
    case str(x) if ".pdg" in x:
        print("image/pdg")
    case str(x) if ".txt" in x:
        print("application/txt")
    case str(x) if ".zip" in x:
        print("application/zip")
    case _:
        print("application/octet-stream")