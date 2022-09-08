from datetime import date

def calculte_days_between_dates(date1,date2):
    if(type(date1) is date and type(date2) is date):
        delta =date1-date2
        print(abs(delta.days))
    else:
        print("Please enter date value")

d0 = date(2008, 8, 18)
d1 = date(2008, 8, 22)
calculte_days_between_dates(d0,d1)