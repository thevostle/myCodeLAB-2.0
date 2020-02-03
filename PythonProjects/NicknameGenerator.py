# ΗəȽŁ0! iƬ'ʂ A ϟiʗκ ɢξϟəƦаʇΘR 2008 εǷiƮ1őϗ
# ŴȑǏƬξ ƴȭɄȒ Ϟ1ʗKϟ4mε ȺϟǷ ƫΗε ρƦ0grɐʍ ψǏƪL ʗ0ϟvξrʇ ίʇ ƫΌ 4ή Θƪɖ ƨcǶΌőL ϟIʗʞή4MΞ

import random

# all readable letters
alphabetEng = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '

# all writing methods for each letter
A = "Δ", "ą", "ɐ", "Ⱥ", "ǟ", "4", "а", "A"
B = "Ϧ", "Ƀ", "Ɓ", "b"
C = "ʗ", "ʗ", "ɔ", "c", "C"
D = "Ƿ", "ɖ", "ɗ", "ɖ", "ɗ", "D"
E = "ξ", "ε", "Ξ", "ə", "3"
F = "ƭ", "ƒ", "Ƒ", "ϝ", "Ϝ"
G = "Ǥ", "ǥ", "ɢ", "g"
H = "Ƕ", "Η", "h"
I = "Ǐ", "ǃ", "1", "ί", "i", "I"
J = "ʝ", "Ϳ", "j", "Ĵ"
K = "κ", "ʞ", "K", "k"
L = "ƪ", "ʟ", "Ƚ", "L", "Ł"
M = "ʍ", "ɱ", "M", "m"
N = "ϗ", "Ϟ", "ή", "Ɲ", "Ŋ", "ϟ", "Ƞ"
O = "Θ", "Ό", "ȭ", "0", "ő"
P = "ρ", "p", "Р", "ƿ", "Ƥ"
Q = "Ɋ", "ɋ", "q", "Q"
R = "ʁ", "Ȓ", "ȑ", "Ʀ", "r", "R"
S = "Ƨ", "$", "ʂ", "ƨ", "s"
T = "Ͳ", "ʇ", "Ț", "ƫ", "Ʈ", "Ƭ", "Ŧ"
U = "ʊ", "ʋ", "ʉ", "Ʉ"
V = "ν", "v", "V"
W = "ω", "ψ", "Ϣ", "Ɯ", "Ŵ"
X = "χ", "X", "x", "}{"
Y = "Ϋ", "Ƴ", "ƴ", "Ɣ", "Ƴ"
Z = "ʑ", "ʐ", "Ȥ", "Ž", "Ζ"
space = " "

alp = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, space]

while True:
    wordOut = ""  
    selectLetter = ""

    wordIn = str(input("Write your nickname: \n>>> ")).lower()
    letterIndex = 0;

    for letterCount in range(len(wordIn)):
        letterIndex = alphabetEng.index(wordIn[letterCount])
        selectLetter = random.choice(alp[letterIndex])
        wordOut += selectLetter

    print(wordOut + '\n')

