file1 = open("text.txt", "w")
file1.write("This course is a special course.\n")
file1.write("We take lectures from our homes.\n")
file1.write("The reason for that is CORONA virus\n")
file1.write("Don't worry. Everything will be better.\n")
file1.close()

file1 = open("text.txt", "r")
print(file1.read())
file1.close()

file1 = open("text.txt", "a")
file1.write("\ntala-123456789")
file1.close()

file1 = open("text.txt", "r")
print(file1.read())
file1.close()

file2 = open("text.txt", "r")
lines = file2.readlines()
file2.close()

file3 = open("text1.txt", "w")
for line in lines:
    line = line.rstrip("\n")
    file3.write(line[::-1] + "\n")
    print(line[::-1])
file3.close()

file3 = open("text1.txt", "r")
print(file3.read())
file3.close()

file4 = open("text.txt", "r")
lines = file4.readlines()
file4.close()

file5 = open("text3.txt", "w")
l = 1

for char in lines:
    c = 0
    for ch in char:
        if ch.islower():
            c += 1

    file5.write("line" + str(l) + ":" + str(c) + "\n")
    l += 1

file5.close()

word = input("Enter a word: ")
c = 0

file6 = open("text.txt", "r")
for line in file6:
    for w in line.split():
        if w.lower() == word.lower():
            c += 1

file6.close()

print("'" + word + "' appeared " + str(c) + " times")

file7 = open("text.txt", "r")
for line in file7:
    line = line.rstrip("\n")
    print(line[:5])

file7.close()
