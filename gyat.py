import os
a = ""
while a != "ja" or a != "nein":
    a = input("Wer Gänsehaut, schlägt auch Enten. Ja oder nein? ")
if a == "ja":
    print("Dönerbeule")
else:
    os.system("shutdown /p")