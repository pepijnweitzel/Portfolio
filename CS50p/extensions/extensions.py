# Code created by Pepijn Weitzel
# Prompt user for file name
file = input("File name: ").lower().strip()


match file:
    case str(x) if ".gif" in x:
        print("image/gif")
    case str(x) if ".jpg" in x:
        print("image/jpeg")
    case str(x) if ".jpeg" in x:
        print("image/jpeg")
    case str(x) if ".png" in x:
        print("image/png")
    case str(x) if ".pdf" in x:
        print("application/pdf")
    case str(x) if ".txt" in x:
        print("application/txt")
    case str(x) if ".zip" in x:
        print("application/zip")
    case _:
        print("application/octet-stream")