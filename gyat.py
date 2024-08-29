import os
a = ""
while a != "nein" or a != "ja":
    a = input("Wer Gänsehaut, schlägt auch Enten. Ja oder nein? ")
if a == "ja":
    print("Dönerbeule")
else:
    os.system("shutdown /p")