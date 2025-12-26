# write a program to check the wheather the given year is lepear (or) not
year=int(input())
if year%4==0 and year%100!=0:
    print("leap year")
else:
    print("not a leap year")
          