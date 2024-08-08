#manifestation day
#if sum of year is equal to date and month then it's a Manifestation Day
day = input("Enter date here (format: 882024)")
day1 = list(day)
day2 = day1[-1:-5:-1]
# print(day2)
day3 = [] #empty list
for i in day2:
     day3.append(int(i))
day4 = sum(day3)
print(f"Manifestation day {day1[0]} {day1[1]} {day4}")
