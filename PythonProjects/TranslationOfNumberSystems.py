while True:
    print("\n\nВведите исходную систему счисления")
    typeIn = int(input("int - 1, bin - 2, oct - 3, hex - 4\n>>> "))
    if typeIn == "":
        sys.exit()
    textIn = input("\nВведите число:\n>>> ")
    if typeIn == 1:
        newtextIn = str(textIn)
        newtextIn = int(textIn, 10)
        print("\nint: " + str(int(newtextIn)) + "\nbin: " + str(bin(newtextIn)) + "\noct: " + str(oct(newtextIn)) + "\nhex: " + str(hex(newtextIn)))

    if typeIn == 2:
        textIn = str(textIn)
        textIn = int(textIn, 2)
        print("\nint: " + str(int(textIn)) + "\nbin: " + str(bin(textIn)) + "\noct: " + str(oct(textIn)) + "\nhex: " + str(hex(textIn)))

    if typeIn == 3:
        textIn = str(textIn)
        textIn = int(textIn, 8)
        print("\nint: " + str(int(textIn)) + "\nbin: " + str(bin(textIn)) + "\noct: " + str(oct(textIn)) + "\nhex: " + str(hex(textIn)))

    if typeIn == 4:
        textIn = str(textIn)
        textIn = int(textIn, 16)
        print("\nint: " + str(int(textIn)) + "\nbin: " + str(bin(textIn)) + "\noct: " + str(oct(textIn)) + "\nhex: " + str(hex(textIn)))
