file1 = open("solutions.txt", "r")
file2 = open("words.txt", "r")
solutions = file1.read()
words = file2.read()

individualsolutionletters = []

counter = 0
while counter < 13853:        
    individualsolutionletters.append(solutions[counter])
    counter += 1

for letter in individualsolutionletters:
    if letter == '\n':
        individualsolutionletters.remove(letter)


individualwordssolution = []

wordcount = 0

while wordcount <= 2308:
    individualwordssolution.append([individualsolutionletters[5 * wordcount], individualsolutionletters[5 * wordcount + 1], individualsolutionletters[5 * wordcount + 2], individualsolutionletters[5*wordcount + 3], individualsolutionletters[5*wordcount + 4]])
    wordcount += 1

###########

individualallletters = []

counter = 0
while counter < 77681:        
    individualallletters.append(words[counter])
    counter += 1
    
for letter1 in individualallletters:
   if letter1 == '\n':
        individualallletters.remove(letter1)




individualwordsall = []

wordcount = 0

while wordcount <= 12946:
    individualwordsall.append([individualallletters[5 * wordcount], individualallletters[5 * wordcount + 1], individualallletters[5 * wordcount + 2], individualallletters[5*wordcount + 3], individualallletters[5*wordcount + 4]])
    wordcount += 1

totalfile = open("total.txt", "w")
totalfile.writelines(str(individualwordsall))
totalfile.close()

for word in individualwordsall:
    if word in individualwordssolution:
        individualwordsall.remove(word)

wordsupdatedfile = open("wordsupdated.txt", "w")
wordsupdatedfile.writelines(str(individualwordsall))
wordsupdatedfile.close()

with open("wordsupdated.txt") as f:
    wordsupdated = eval(f.read())

solutionsupdatedfile = open("solutionsupdated.txt", "w")
solutionsupdatedfile.writelines(str(individualwordssolution))
solutionsupdatedfile.close()

with open("solutionsupdated.txt") as f:
    solutionsupdated = eval(f.read())
    
print("Succesfully updated!")


