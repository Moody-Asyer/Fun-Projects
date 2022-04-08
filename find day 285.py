#Nyari hari ke-265
#tahun 1700-1817 pake kalender julian
#1918-dst kalender gregorian pas hari ke 32(1 feb = 14 feb)
year = int(input().strip())
def tahun(year):
    if year == 1918:
        return '26.09.%s' % year
    elif year % 4 == 0 and (year < 1918 or year % 100 != 0 or year % 400 == 0):
        return '12.09.%s' % year
    else:
        return '13.09.%s' % year
print(tahun(year))
#https://www.hackerrank.com/challenges/day-of-the-programmer/problem