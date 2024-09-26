ending = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}


def main():
    file_name = input("File Name: ").lower().strip()
    print(convert_name(file_name))

def convert_name(file):
    for end in ending:
        if file.endswith(end):
            return ending[end]
     return "application/octet-stream"


main()

