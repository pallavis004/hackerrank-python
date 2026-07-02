def timeConversion(s):
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return '00' + s[2:8]
        return s[:8]
    else:
        if s[:2] == '12':
            return s[:8]
        return str(int(s[:2]) + 12) + s[2:8]


if __name__ == '__main__':
    s = input().strip()
    print(timeConversion(s))