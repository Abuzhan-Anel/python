txt = input("Input a string: ")
txt = txt.strip()
if len(txt) < 1:
    print("ERROR")
else:
    if all (txt[i] in "0123456789" for i in range(len(txt))):
        print("The string is an integer.")
    else:
        print("The string is not an integer.")