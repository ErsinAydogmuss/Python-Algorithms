def is_leap(year):
    if year <= 10**5 and year >= 1900:
        if year % 4 ==0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
year = int(input())
print(is_leap(year))