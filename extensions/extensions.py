ext = input("File name: ").lower().strip()

if ".gif" in ext:
    print("image/gif")
elif ".jpg" in ext or ".jpeg" in ext:
    print("image/jpeg")
elif ".png" in ext:
    print("image/png")
elif ".pdf" in ext:
    print("application/pdf")
elif "txt" in ext:
    print("text/plain")
elif ".zip" in ext:
    print("application/zip")
else:
    print("application/octet-stream")
