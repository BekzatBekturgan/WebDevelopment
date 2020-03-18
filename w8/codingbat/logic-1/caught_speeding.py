def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    elif speed <= 60:
        return 0
    else:
     return 1 if 61 <= speed <= 80 else 2