grades=[73,67,38,39,33]

for x in range(0,len(grades)):
    if grades[x] % 5 > 2 and grades[x] >= 38:
        grades[x] = grades[x]+(5-grades[x]%5)
    else:
        grades[x] = grades[x]

print(grades)