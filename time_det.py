from datetime import datetime

def day_num(year1, month1, day1): #첫 날이 무슨 요일인지 확인
     month_first = "{}-{}-{}".format(year1, month1, 1)
     month_first  = datetime.strptime(month_first, '%Y-%m-%d')
     month_week = month_first.weekday()
     return month_week, month_first

def week_num(day):
     week = day//7
     day = day%7
     return week, day

day1 = datetime.now() #오늘
year1 = day1.year
month1 = day1.month
day1 = day1.day

for i in range(1, 31):
   first_day, month_first = day_num(2024, 8, i)
   week_num1, day_num1 = week_num(i+first_day)
   day_num2 = week_num1*5 +day_num1 - (5 - max(5-first_day, 0)) #일요일 때문에 -6이 되지 않도록 만듬
   print("=======================")
   if not ((day_num1 == 0) or (day_num1 == 6)):
    print("{}주차, {}".format(week_num1, day_num1))
    print("++++{}번+++++".format(day_num2))
    print(i)