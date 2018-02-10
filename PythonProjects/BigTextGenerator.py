print("#   # #####\n#   #   #\n#####   #\n#   #   #\n#   #   #\n#   # #####\n\n##### ##### #   #       #####       #   # ##### #     #####       #   # ##### #   #")
print("#     #   # ##  #         #         #   # #     #     #   #        # #  #   # #   #\n#     #   # # # #         #         ##### ##### #     #####         #   #   # #   #")
print("#     ##### #  ##         #         #   # #     #     #             #   #   # #   #\n#     #   # #   #         #         #   # #     #     #             #   #   # #   #\n##### #   # #   #       #####       #   # ##### ##### #             #   ##### #####\n\n")

wordIn = str(input("Введите текст: ")).lower()
letterLenght = 5 # int(input("Введите требуемую длину букв: "))
letterWeight = 6 # letterLenght / 2
letterCount = len(wordIn)
wordOut = ""

for y in range(letterWeight):
    for x in range(letterCount):

        if y == 0:
            if wordIn[x] == 'a' or wordIn[x] == 'c' or wordIn[x] == 'e' or wordIn[x] == 'f' or wordIn[x] == 'g' or wordIn[x] == 'i' or wordIn[x] == 'o':
                wordOut = wordOut + (('#'*letterLenght) + " ")
            elif  wordIn[x] == 'p' or wordIn[x] == 's' or wordIn[x] == 't' or wordIn[x] == 'z':
                wordOut = wordOut + (('#'*letterLenght) + " ")

            elif  wordIn[x] == 'b' or wordIn[x] == 'd' or wordIn[x] == 'q':
                wordOut = wordOut + (('#'*(letterLenght-1)) + "  ")

            elif  wordIn[x] == 'h' or wordIn[x] == 'k' or wordIn[x] == 'm' or wordIn[x] == 'n' or wordIn[x] == 'u' or wordIn[x] == 'v' or wordIn[x] == 'w':
                wordOut = wordOut + ("#   #" + " ")
            elif  wordIn[x] == 'x' or wordIn[x] == 'y':
                wordOut = wordOut + ("#   #" + " ")
            elif wordIn[x] == 'r':
                wordOut = wordOut + ("###  " + " ")
            elif wordIn[x] == 'l':
                wordOut = wordOut + ("#    " + " ")
            elif wordIn[x] == 'j':
                wordOut = wordOut + ("    #" + " ")
            elif wordIn[x] == ' ':
                wordOut = wordOut + ("     " + " ")

        if y == 1:
            if  wordIn[x] == 'c' or wordIn[x] == 'e'or wordIn[x] == 'f'or wordIn[x] == 'g'or wordIn[x] == 'l'or wordIn[x] == 'g'or wordIn[x] == 's':
                wordOut = wordOut + (('#') + "     ")
            elif wordIn[x] == 'a'or wordIn[x]=='b'or wordIn[x]=='d'or wordIn[x]=='h'or wordIn[x] == 'o' or wordIn[x] == 'p'or wordIn[x] == 'u'or wordIn[x]=='v'or wordIn[x] == 'w':
                wordOut = wordOut + ('#' + "   " + '#' + " ")
            elif wordIn[x] == 't' or wordIn[x] == 'i':
                wordOut = wordOut + ('  ' + "#" + '  ' + " ")
            elif wordIn[x] == 'j':
                wordOut = wordOut + ("    " + '#' + " ")
            elif wordIn[x] == 'k':
                wordOut = wordOut + ("# ## " + " ")
            elif wordIn[x] == 'm':
                wordOut = wordOut + ("## ##" + " ")
            elif wordIn[x] == 'r' or wordIn[x] == 'q':
                wordOut = wordOut + ("#  # " + " ")
            elif wordIn[x] == 'x' or wordIn[x] == 'y':
                wordOut = wordOut + (" # # " + " ")
            elif wordIn[x] == 'z':
                wordOut = wordOut + ("   # " + " ")
            elif wordIn[x] == 'n':
                wordOut = wordOut + ("##  #" + " ")
            elif wordIn[x] == ' ':
                wordOut = wordOut + ("     " + " ")

        if y == 2:
            if  wordIn[x] == 'c'or wordIn[x] == 'g'or wordIn[x] == 'l':
                wordOut = wordOut + (('#') + "     ")
            elif  wordIn[x] == 'e'or wordIn[x] == 'f'or wordIn[x] == 'h'or wordIn[x] == 'p'or wordIn[x] == 's':
                wordOut = wordOut + (('#'*letterLenght) + " ")
            elif  wordIn[x] == 'a' or wordIn[x] == 'd' or wordIn[x] == 'h' or wordIn[x] == 'o' or wordIn[x] == 'u'or wordIn[x] == 'v'or wordIn[x] == 'w':
                wordOut = wordOut + ('#' + "   " + '#' + " ")
            elif  wordIn[x] == 'b':
                wordOut = wordOut + (('#'*(letterLenght-1)) + "  ")
            elif wordIn[x] == 'j':
                wordOut = wordOut + ("    " + '#' + " ")
            elif wordIn[x] == 'k':
                wordOut = wordOut + ("##   "+ " ")
            elif wordIn[x] == 'm' or wordIn[x] == 'n':
                wordOut = wordOut + ("# # #"+ " ")
            elif wordIn[x] == 'q' or wordIn[x] == 'r':
                wordOut = wordOut + ("#  # " + " ")
            elif wordIn[x] == 't' or wordIn[x] == 'i'or wordIn[x] == 'x'or wordIn[x] == 'y'or wordIn[x] == 'z':
                wordOut = wordOut + ('  ' + "#" + '  ' + " ")
            elif wordIn[x] == ' ':
                wordOut = wordOut + ("     " + " ")

        if y == 3:
            if  wordIn[x] == 'c' or wordIn[x] == 'e'or wordIn[x] == 'f'or wordIn[x] == 'l'or wordIn[x] == 'p':
                wordOut = wordOut + (('#') + "     ")
            elif  wordIn[x] == 'a':
                wordOut = wordOut + (('#'*letterLenght) + " ")
            elif  wordIn[x] == 'b' or wordIn[x] == 'd'or wordIn[x] == 'h'or wordIn[x] == 'm'or wordIn[x] == 'o'or wordIn[x] == 'u'or wordIn[x] == 'v':
                wordOut = wordOut + ('#' + "   " + '#' + " ")
            elif wordIn[x] == 'j'or wordIn[x] == 's':
                wordOut = wordOut + ("    " + '#' + " ")
            elif wordIn[x] == 'w':
                wordOut = wordOut + ("# # #"+ " ")
            elif wordIn[x] == 't' or wordIn[x] == 'i'or wordIn[x] == 'y':
                wordOut = wordOut + ('  ' + "#" + '  ' + " ")
            elif wordIn[x] == 'z':
                wordOut = wordOut + (" #   "+ " ")
            elif wordIn[x] == 'r':
                wordOut = wordOut + ("###  "+ " ")
            elif wordIn[x] == 'k':
                wordOut = wordOut + ("# #  "+ " ")
            elif wordIn[x] == 'g' or wordIn[x] == 'n':
                wordOut = wordOut + ("#  ##"+ " ")
            elif wordIn[x] == 'q':
                wordOut = wordOut + ("# ## "+ " ")
            elif wordIn[x] == 'x':
                wordOut = wordOut + (" # # "+ " ")
            elif wordIn[x] == ' ':
                wordOut = wordOut + ("     " + " ")

        if y == 4:
            if  wordIn[x] == 'c' or wordIn[x] == 'e'or wordIn[x] == 'f'or wordIn[x] == 'l' or wordIn[x] == 'z' or wordIn[x] == 'p':
                wordOut = wordOut + (('#') + "     ")
            elif  wordIn[x] == 'a' or wordIn[x] == 'j'or wordIn[x] == 'd'or wordIn[x] == 'g'or wordIn[x] == 'm'or wordIn[x] == 'n'or wordIn[x] == 'o'or wordIn[x] == 'u' or wordIn[x] == 'x'or wordIn[x] == 'b'or wordIn[x] == 'h':
                wordOut = wordOut + ('#' + "   " + '#' + " ")
            elif  wordIn[x] == 'i'or wordIn[x] == 't'or wordIn[x] == 'y':
                wordOut = wordOut + ("  #  " + " ")
            elif  wordIn[x] == 'k'or wordIn[x] == 'q'or wordIn[x] == 'r':
                wordOut = wordOut + ("#  # " + " ")
            elif  wordIn[x] == 'v':
                wordOut = wordOut + (" # # " + " ")
            elif  wordIn[x] == 'w':
                wordOut = wordOut + ("# # #" + " ")
            elif  wordIn[x] == 's':
                wordOut = wordOut + ("    #" + " ")
            elif wordIn[x] == ' ':
                wordOut = wordOut + ("     " + " ")


        if y == 5:
            if  wordIn[x] == 'c' or wordIn[x] == 'e' or wordIn[x] == 'b'or wordIn[x] == 's'or wordIn[x] == 'g'or wordIn[x] == 'i'or wordIn[x] == 'l'or wordIn[x] == 'o'or wordIn[x] == 's'or wordIn[x] == 'u'or wordIn[x] == 'z'or wordIn[x] == 'q':
                wordOut = wordOut + (('#'*letterLenght) + " ")
            elif  wordIn[x] == 'a'or wordIn[x] == 'x'or wordIn[x] == 'h'or wordIn[x] == 'k'or wordIn[x] == 'm'or wordIn[x] == 'n'or wordIn[x] == 'r':
                wordOut = wordOut + ('#' + "   " + '#' + " ")
            elif  wordIn[x] == 'b'or wordIn[x] == 'd':
                wordOut = wordOut + ("#### " + " ")
            elif  wordIn[x] == 'f'or wordIn[x] == 'p':
                wordOut = wordOut + ("#    " + " ")
            elif  wordIn[x] == 't'or wordIn[x] == 'v'or wordIn[x] == 'y':
                wordOut = wordOut + ("  #  " + " ")
            elif  wordIn[x] == 'w':
                wordOut = wordOut + (" # # " + " ")
            elif  wordIn[x] == 'j':
                wordOut = wordOut + (" ### " + " ")
            elif wordIn[x] == ' ':
                wordOut = wordOut + ("     " + " ")

    wordOut = wordOut + "\n"


print(wordOut)
input()
