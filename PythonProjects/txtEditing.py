
with open("sample3.txt", mode="a", encoding="utf-8") as newFile:
    newFile.write("\nThe End")

with open("sample3.txt", encoding="utf-8") as newFile:
    print(newFile.read())