'''4.Write a Python program to check whether an alphabetis avowel(гласная) or consonant(согласная).
ExpectedOutput:Input a letter of the alphabet: kk is a consonant.'''
alp = input()
avo = ["a", "e", "i", "o", "u"]
if(alp in avo):
    print(alp, 'is a avowel')
else:
    print(alp, "is a consonant")