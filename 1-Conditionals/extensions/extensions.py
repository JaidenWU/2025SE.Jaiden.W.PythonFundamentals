def main():
    name = input("What's the name of the file? ").casefold().strip()
    if name.endswith(".jpg") | name.endswith(".jpeg"):
        print("image/jpeg")
    elif name.endswith(".gif"):
        print("image/gif")
    elif name.endswith(".png"):
        print("image/png")
    elif name.endswith(".pdf"):
        print("application/gif")
    elif name.endswith(".txt"):
        print("text/plain")
    elif name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()
