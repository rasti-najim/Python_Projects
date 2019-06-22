# Pig Latin is a game of alterations played on the English language game.
# To create the Pig Latin form of an English word the initial consonant sound
#  is transposed to the end of the word and an ay is affixed
#  (Ex.: "banana" would yield anana-bay).
# You can read Wikipedia for more information on rules.


n = list(input())
vowels = ['a', 'e', 'i', 'o', 'u']


if n[0] in vowels:
    n.append('ay')


elif n[0] not in vowels:
    while n[0] not in vowels:

        consonant = n.pop(n.index(n[0]))
        n.append(consonant)

    n.append('ay')

pig_latin = ''.join(n)
print(pig_latin)
