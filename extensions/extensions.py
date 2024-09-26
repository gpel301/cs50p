def main():
    file = input("File Name: ")
    print(convert(file))


def convert(x):
    x = x.lower().strip()
    if x.endswith(".gif"):
        return "image/gif"
    elif x.endswith(".jpg"):
        return "image/jpeg"
    elif x.endswith(".jpeg"):
        return "image/jpeg"
    elif x.endswith(".png"):
        return "image/png"
    elif x.endswith(".pdf"):
        return "application/pdf"
    elif x.endswith(".txt"):
        return "text/plain"
    elif x.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()
