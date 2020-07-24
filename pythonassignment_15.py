
##Counting elements in a sentence
sentence = input("Please enter a sentence : ")
letters = dict()
for i in sentence:
    if i not in letters:
        letters[i] = 1
    else:
        letters[i] += 1
print(letters)
