import os
a = ""
while True:
    a = input("Wer Gänsehaut, schlägt auch Enten. Ja oder nein? ")
    if a == "ja":
        print("Dönerbeule")
        break
    else:
        os.system("shutdown /p")
        break