def add_time(start, duration, startDay = ""):

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    lowercase_days = [day.lower() for day in days]
  
    startHour = start.rsplit(":")[0]
    startMinute = start.rsplit(":")[1].rsplit(" ")[0]
    isAM = start.rsplit(" ")[1] == "AM"

    if (startDay != ""):
        startDayIndex = lowercase_days.index(startDay.lower())
        
    
  
    if not isAM:
        startHour = int(startHour) + 12
    startInMinutes =  60 * int(startHour) + int(startMinute)

  
    durationHour = duration.rsplit(":")[0]
    durationMinute = duration.rsplit(":")[1].rsplit(" ")[0]
    durationInMinutes = 60 * int(durationHour) + int(durationMinute)

    endInMinutes = startInMinutes + durationInMinutes
  
    daysPassed = endInMinutes // (24 * 60)
    endInMinutes -= daysPassed * (24*60)
    endHour = endInMinutes // 60
    endInMinutes -= endHour * 60
    endMinute = endInMinutes;

    if endHour == 0:
        endHour += 12
        isAM = True
    elif endHour < 12:
        isAM = True
    elif endHour == 12:
        isAM = False
    elif endHour > 12:
        endHour -= 12
        isAM = False
  
    result = '{0:d}:{1:02d}'.format(endHour, endMinute)
    if isAM:
        result += (" AM")
    else:
        result += (" PM")

    if (startDay != ""):
        endDayIndex = startDayIndex + daysPassed;
        result += (", " + days[endDayIndex % 7])
  
    if daysPassed == 1:
        result += (" (next day)")
    if daysPassed > 1:
        result += f" ({daysPassed} days later)"
  
    return result
