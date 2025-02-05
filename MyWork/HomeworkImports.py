import calendar

#calendar.weekday doesnt tell you the day, it tells you a number associated with a day.
#Im fixing that problem for them :)
def WhatWeekDayIsMyBirthday(year, month, day):
    weekday = calendar.weekday(year, month, day)
    match weekday:
        case 0:
            return "Monday"
        case 1:
            return "Tuesday"
        case 2:
            return "Wednesday"
        case 3:
            return "Thursday"
        case 4:
            return "Friday"
        case 5:
            return "Saturday"
        case 6:
            return "Sunday"
        
print("Your birthday was on a " + WhatWeekDayIsMyBirthday(1999,11,7))
     
