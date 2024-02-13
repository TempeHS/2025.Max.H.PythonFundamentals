def main():
    mediafile = input("could i have your file ").strip().lower()
    if mediafile.endswith(".pdf"):
        print("application/pdf")
    elif mediafile.endswith(".jpg"):
        print("image/jpeg")
    else:
        print("application/octet-stream")


main()
