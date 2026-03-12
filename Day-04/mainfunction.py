# code about main function
#define the function
def is_leap(year):
  return (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
while True :
  year = int(input("enter the year (enter 0 to exit): "))
  if year == 0 :
    break
  if is_leap(year):
   print("this is leap year :" , year)
  else:
   print("this is not leap year :" , year)
