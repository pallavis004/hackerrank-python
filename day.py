def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    if year < 1918:
        leap = year % 4 == 0
    else:
        leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    day = 12 if leap else 13
    return f"{day:02d}.09.{year}"
if __name__ == "__main__":
    print(dayOfProgrammer(2016)) 