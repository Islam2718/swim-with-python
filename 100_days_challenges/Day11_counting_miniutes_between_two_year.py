fromYear = int(input("Count Leapear Min from : "))
toYear = int(input("Count Leapear Min To : "))
print("-------------------------------------")
days = 0
while fromYear <= toYear:
  if fromYear %4== 0 and fromYear %100 != 0 or fromYear %400 == 0:
    print(fromYear, " is leapyear - 366 days")
    days += 366
  else:
    print(fromYear, " is not leapyear - 365 days")
    days = days + 365
    
  fromYear +=1

totalMiniute = days * 1440
print("-----------------------------------")
print("Total Days = ", days)
print("Total Miniutes = ", totalMiniute)