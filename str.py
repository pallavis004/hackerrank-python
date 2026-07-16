import os
def minimumNumber(n, password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-+" for c in password)
    missing = 4 - (has_lower + has_upper + has_digit + has_special)
    return max(missing, 6 - n)
if __name__ == '__main__':
    n = int(input().strip())
    password = input()
    answer = minimumNumber(n, password)
    print(answer)