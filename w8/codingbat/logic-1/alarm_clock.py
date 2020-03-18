def alarm_clock(day, vacation):
    if vacation:
        return '10:00' if (1<=day<=5) else 'off'
    return '7:00' if (1<=day<=5) else '10:00'