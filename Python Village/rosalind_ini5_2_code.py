f = open('rosalind_ini5.txt', 'r')
k = open('output.txt', 'w')
i = 0
lines = f.readlines()
z = len(lines)
for string in lines:
    if i % 2 == 1:
        k.write(string)
    i = i + 1
k.close()